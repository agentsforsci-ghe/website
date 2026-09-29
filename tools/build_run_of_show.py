#!/usr/bin/env python3
"""Build the run of show artifact from workshop/lesson-plan.qmd.

The run sheet is the instructor's run of show, written for print. This
script reads it and writes a self-contained web page for the iPad on the
day: the fourteen timed blocks with their minute tables as tick lists, each
row opening the notes of its subsection, a Start button per block that
drives the running time, the time left and the drift against the printed
schedule, and the Before, After and Rules pages from the untimed sections.

  1. Parse the qmd: timed blocks (## Title (HH:MM-HH:MM, N min) [TAGS]),
     their Slides line, | Min | What | table and ### subsections, and the
     untimed sections Operating rules, Materials, Breaks, Before the day and
     After the room empties.
  2. Match every table row to the subsection that holds its notes, by word
     overlap, monotonic within the block. --report prints the table.
  3. Inline the data as JSON with tools/run_of_show.css and
     tools/run_of_show.js into one HTML body fragment.

The page lives as a private claude.ai artifact, not on the site: the
fragment written by --out PATH is what the Artifact tool publishes
(claude.ai wraps it in its own document skeleton; ticks and times are kept
in the artifact's database). Rebuild and republish it whenever the run
sheet's blocks or minutes change, for example after the rehearsal.
Standard library only. Exit 1 only when a heading cannot be parsed.
"""
import argparse
import hashlib
import html
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QMD = ROOT / "workshop" / "lesson-plan.qmd"
JS = ROOT / "tools" / "run_of_show.js"
CSS = ROOT / "tools" / "run_of_show.css"

WORKSHOP_DATE = "2026-09-29"
UTC_OFFSET = "+02:00"
TIME_ZONE = "Europe/Zurich"
TITLE = "agentsforsci-ghe Run Sheet"

BLOCK_RE = re.compile(r"^## (.+?) \((\d\d:\d\d)-(\d\d:\d\d), (\d+) min\)(?: \[(.+)\])?\s*$")
SECTION_RE = re.compile(r"^### (.+?) \((\d+) min(?:, countdown (\d+))?\)(?: \[(.+)\])?\s*$")
ITEM_RE = re.compile(r"^(\s*)(- \[[ xX]\] |- |\d+\. )(.*)$")
STEP_MIN_RE = re.compile(r"\s*\((\d+)\)\s*$")

STOPWORDS = set("the a an and of on to in with then at it its is for by do not that this each one your our my turn slide slides min".split())
MODE_RE = re.compile(r"\b(my|your|our) turn\b")
NO_NOTES_RE = re.compile(r"^(buffer\b|round \d+ slide$)", re.I)


# ---------------------------------------------------------------- inline text

def inline(text):
    """Escape, then the run sheet's inline markup: `code`, **bold**, [reminder]."""
    s = html.escape(text, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*([^*\s][^*]*?)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\](?!\()", r"<mark>\1</mark>", s)
    return s


def plain(text):
    s = text.replace("`", "")
    s = re.sub(r"\*\*([^*]+)\*\*", r"\1", s)
    return s


# ---------------------------------------------------------------- body parser

def parse_table(lines):
    rows = []
    header = None
    for ln in lines:
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if header is None:
            header = cells
            continue
        if all(re.fullmatch(r":?-+:?", c) for c in cells):
            continue
        rows.append(cells)
    return {"t": "table", "header": header or [], "rows": rows}


def parse_body(lines):
    """Paragraphs, tables and (nested) lists. Returns a list of nodes."""
    nodes = []
    i, n = 0, len(lines)
    while i < n:
        line = lines[i]
        if not line.strip() or line.strip().startswith("{{<"):
            i += 1
            continue
        if line.startswith("|"):
            tbl = []
            while i < n and lines[i].startswith("|"):
                tbl.append(lines[i])
                i += 1
            nodes.append(parse_table(tbl))
            continue
        m = ITEM_RE.match(line)
        if m and m.group(1) == "":
            kind = "ol" if m.group(2)[0].isdigit() else "ul"
            items = []
            while i < n:
                m = ITEM_RE.match(lines[i])
                if not m or m.group(1) != "":
                    break
                k = "ol" if m.group(2)[0].isdigit() else "ul"
                if k != kind:
                    break
                marker = m.group(2)
                indent = len(marker)
                text_lines = [m.group(3)]
                i += 1
                cont = []
                while i < n:
                    if lines[i].strip() == "":
                        j = i
                        while j < n and lines[j].strip() == "":
                            j += 1
                        if j < n and lines[j].startswith(" "):
                            cont.append("")
                            i += 1
                            continue
                        break
                    if lines[i].startswith(" "):
                        cont.append(lines[i])
                        i += 1
                        continue
                    break
                ded = [c[indent:] if c.startswith(" " * indent) else c.lstrip() for c in cont]
                k2 = 0
                while k2 < len(ded):
                    mm = ITEM_RE.match(ded[k2])
                    if mm and mm.group(1) == "":
                        break
                    if ded[k2].strip():
                        text_lines.append(ded[k2].strip())
                    k2 += 1
                children = parse_body(ded[k2:]) if k2 < len(ded) else []
                text = " ".join(text_lines)
                item = {"text": text, "children": children}
                if marker.startswith("- ["):
                    item["checkbox"] = True
                if kind == "ol":
                    item["n"] = int(marker.rstrip(". "))
                    sm = STEP_MIN_RE.search(text)
                    if sm:
                        item["min"] = int(sm.group(1))
                        item["text"] = text[: sm.start()].rstrip()
                items.append(item)
            nodes.append({"t": kind, "items": items})
            continue
        para = []
        while i < n and lines[i].strip() and not lines[i].startswith("|") and not (ITEM_RE.match(lines[i]) and ITEM_RE.match(lines[i]).group(1) == "") and not lines[i].strip().startswith("{{<"):
            para.append(lines[i].strip())
            i += 1
        nodes.append({"t": "p", "text": " ".join(para)})
    return nodes


def node_to_json(node, id_prefix=None, counter=None):
    """Convert a parsed node into the app's JSON shape, giving numbered items ids."""
    if node["t"] == "p":
        return {"t": "p", "html": inline(node["text"])}
    if node["t"] == "table":
        return None
    out_items = []
    for it in node["items"]:
        j = {"html": inline(it["text"]), "text": plain(it["text"]), "children": []}
        if node["t"] == "ol":
            j["n"] = it.get("n")
            j["min"] = it.get("min")
            if id_prefix is not None:
                j["id"] = "%s/i%d" % (id_prefix, counter[0])
                counter[0] += 1
        for c in it["children"]:
            cj = node_to_json(c, id_prefix, counter)
            if cj:
                j["children"].append(cj)
        out_items.append(j)
    return {"t": node["t"], "items": out_items}


# ---------------------------------------------------------------- qmd parser

def split_front_matter(text):
    lines = text.split("\n")
    if lines and lines[0].strip() == "---":
        for k in range(1, len(lines)):
            if lines[k].strip() == "---":
                return lines[k + 1:]
    return lines


def top_sections(lines):
    """Yield (heading_line, body_lines) for every '## ' section."""
    secs = []
    cur = None
    for ln in lines:
        if ln.startswith("## "):
            if cur:
                secs.append(cur)
            cur = [ln, []]
        elif cur is not None:
            cur[1].append(ln)
    if cur:
        secs.append(cur)
    return secs


def split_subsections(body):
    head, subs, cur = [], [], None
    for ln in body:
        if ln.startswith("### "):
            if cur:
                subs.append(cur)
            cur = [ln, []]
        elif cur is None:
            head.append(ln)
        else:
            cur[1].append(ln)
    if cur:
        subs.append(cur)
    return head, subs


def parse_tags(s):
    return [t.strip() for t in s.split(",")] if s else []


# ---------------------------------------------------------------- matching

def norm(text):
    t = re.sub(r"\([^)]*\)", " ", text)
    t = re.sub(r"\[[^\]]*\]", " ", t)
    t = t.lower().replace("`", "")
    m = MODE_RE.search(t)
    mode = m.group(1) if m else None
    t = MODE_RE.sub(" ", t)
    toks = re.findall(r"[a-z0-9.+]+", t)
    toks = [w for w in toks if w not in STOPWORDS]
    toks = [w[:-1] if len(w) > 3 and w.endswith("s") and not w.endswith("ss") else w for w in toks]
    nums = {w for w in toks if re.fullmatch(r"[0-9.]+", w)}
    return set(toks), nums, mode


def score(row, sec):
    R, rn, rm = row
    S, sn, sm = sec
    if not R or not S:
        return 0.0, 0.0
    if rn and sn and rn.isdisjoint(sn):
        return 0.0, 0.0
    inter = R & S
    ov = len(inter) / min(len(R), len(S))
    jac = len(inter) / len(R | S)
    if rm and sm and rm != sm:
        ov *= 0.5
    return ov, jac


def match_rows(rows, sections, prev_question):
    """Attach section ids to rows. Mutates rows; returns (orphans, report_lines)."""
    report = []
    if not sections:
        for r in rows:
            r["sections"] = []
            r["flag"] = "no sections"
        return [], report
    secn = [norm(s["title"]) for s in sections]
    claimed = set()
    matched = []  # (row_index, sec_index)
    last = 0
    for ri, r in enumerate(rows):
        r["sections"] = []
        label = plain(r["label"])
        if NO_NOTES_RE.match(label):
            r["flag"] = "no notes"
            report.append((r, None, 0, 0, "no notes"))
            continue
        rn = norm(label)
        best, bi = (0.0, 0.0), None
        for si in range(last, len(sections)):
            sc = score(rn, secn[si])
            if sc > best:
                best, bi = sc, si
        if bi is not None and best[0] >= 0.5:
            r["sections"].append(sections[bi]["id"])
            claimed.add(bi)
            matched.append((ri, bi))
            last = bi
            flag = "weak" if best[0] < 0.6 else ""
            r["flag"] = flag
            report.append((r, sections[bi], best[0], best[1], flag))
        else:
            flag = "opener" if "opens with" in label.lower() else "unmatched"
            r["flag"] = flag
            report.append((r, None, best[0], best[1], flag))
    # leftover sections: pair with an unmatched row between the same neighbours
    orphans = []
    for si, s in enumerate(sections):
        if si in claimed:
            continue
        prev_row = -1
        next_row = len(rows)
        for (ri, mi) in matched:
            if mi < si:
                prev_row = max(prev_row, ri)
            if mi > si:
                next_row = min(next_row, ri)
        target = None
        for ri in range(prev_row + 1, next_row):
            if rows[ri]["flag"] in ("unmatched", "opener"):
                target = rows[ri]
                break
        if target is not None:
            target["sections"].append(s["id"])
            target["flag"] = (target["flag"] + "+leftover").strip("+")
            for idx, line in enumerate(report):
                if line[0] is target:
                    report[idx] = (target, s, line[2], line[3], target["flag"])
        else:
            orphans.append(s["id"])
    return orphans, report


# ---------------------------------------------------------------- build data

def parse(text):
    lines = split_front_matter(text)
    secs = top_sections(lines)
    data = {
        "title": TITLE,
        "workshopDate": WORKSHOP_DATE,
        "timeZone": TIME_ZONE,
        "blocks": [],
        "lists": {"before": [], "arrival": [], "after": []},
        "rules": [],
        "materials": [],
        "breaks": [],
    }
    reports = []
    untimed = {}
    for heading, body in secs:
        m = BLOCK_RE.match(heading)
        if m:
            data["blocks"].append(parse_block(m, body, reports))
            continue
        name = heading[3:].strip()
        if name.startswith("## "):
            name = name[3:]
        untimed[name] = body
        if not re.match(r"^[A-Za-z].*", name):
            raise SystemExit("cannot parse heading: %r" % heading)

    # untimed sections
    for name, body in untimed.items():
        nodes = parse_body(body)
        low = name.lower()
        if low.startswith("operating rules"):
            data["rules"] = [inline(it["text"]) for nd in nodes if nd["t"] == "ul" for it in nd["items"]]
        elif low.startswith("materials"):
            data["materials"] = [inline(it["text"]) for nd in nodes if nd["t"] == "ul" for it in nd["items"]]
        elif low.startswith("breaks"):
            for nd in nodes:
                if nd["t"] == "table":
                    for cells in nd["rows"]:
                        if len(cells) >= 4:
                            data["breaks"].append({"name": cells[0], "time": cells[1], "question": plain(cells[2]), "opens": plain(cells[3])})
        elif low.startswith("before the day"):
            data["lists"]["before"] = checklist(nodes, "before")
        elif low.startswith("after the room"):
            data["lists"]["after"] = checklist(nodes, "after")
        # Contact time is not shown; the app computes its own numbers.

    # arrival list mirrors the Arrival block's rows
    for b in data["blocks"]:
        if b["title"].lower().startswith("arrival"):
            data["lists"]["arrival"] = [{"id": r["id"], "html": r["html"], "text": r["label"]} for r in b["rows"]]
    # break questions by time range; an "opens with" row carries the question
    # of the break before its block
    by_time = {br["time"]: br for br in data["breaks"]}
    prev_q = None
    for b in data["blocks"]:
        key = "%s-%s" % (b["start"], b["end"])
        br = by_time.get(key)
        b["breakQuestion"] = {"question": br["question"], "opens": br["opens"]} if br else None
        for r in b["rows"]:
            if r.get("flag", "").startswith("opener") and prev_q:
                r["question"] = prev_q
            r.pop("flag", None)
        if br:
            prev_q = br["question"]
    return data, reports


def checklist(nodes, prefix):
    out = []
    k = 0
    for nd in nodes:
        if nd["t"] == "ul":
            for it in nd["items"]:
                out.append({"id": "%s/%d" % (prefix, k), "html": inline(it["text"]), "text": plain(it["text"])})
                k += 1
    return out


def parse_block(m, body, reports):
    title, start, end, mins, tags = m.group(1), m.group(2), m.group(3), int(m.group(4)), parse_tags(m.group(5))
    bid = "b" + start.replace(":", "")
    head, subs = split_subsections(body)
    head_nodes = parse_body(head)
    block = {
        "id": bid, "title": title, "start": start, "end": end, "min": mins, "tags": tags,
        "startIso": "%sT%s:00%s" % (WORKSHOP_DATE, start, UTC_OFFSET),
        "endIso": "%sT%s:00%s" % (WORKSHOP_DATE, end, UTC_OFFSET),
        "slides": [], "intro": [], "rows": [], "sections": [], "orphanSections": [],
    }
    table = None
    checks = []
    for nd in head_nodes:
        if nd["t"] == "p":
            if nd["text"].startswith("Slides:"):
                s = nd["text"][len("Slides:"):].strip().rstrip(".")
                block["slides"] = [x.strip() for x in s.split("->") if x.strip()]
            else:
                block["intro"].append(inline(nd["text"]))
        elif nd["t"] == "table" and table is None:
            table = nd
        elif nd["t"] == "ul" and any(it.get("checkbox") for it in nd["items"]):
            checks.extend(nd["items"])
        elif nd["t"] in ("ul", "ol"):
            block["intro"].append(" ".join(inline(it["text"]) for it in nd["items"]))
    for si, (sh, sbody) in enumerate(subs):
        sm = SECTION_RE.match(sh)
        if not sm:
            raise SystemExit("cannot parse subsection heading in %s: %r" % (title, sh))
        sid = "s%d" % si
        counter = [0]
        content = []
        for nd in parse_body(sbody):
            j = node_to_json(nd, "%s/%s" % (bid, sid), counter)
            if j:
                content.append(j)
        block["sections"].append({
            "id": sid, "title": sm.group(1), "min": int(sm.group(2)),
            "countdown": int(sm.group(3)) if sm.group(3) else None,
            "tags": parse_tags(sm.group(4)), "content": content,
        })
    if table:
        for ri, cells in enumerate(table["rows"]):
            if len(cells) < 2:
                continue
            try:
                rmin = int(cells[0])
            except ValueError:
                rmin = None
            block["rows"].append({"id": "%s/r%d" % (bid, ri), "min": rmin, "label": plain(cells[1]), "html": inline(cells[1])})
    elif checks:
        if bid == "b0830":
            for ri, it in enumerate(checks):
                block["rows"].append({"id": "arrival/%d" % ri, "min": None, "label": plain(it["text"]), "html": inline(it["text"])})
        else:
            for ri, it in enumerate(checks):
                block["rows"].append({"id": "%s/r%d" % (bid, ri), "min": None, "label": plain(it["text"]), "html": inline(it["text"])})
    elif block["sections"]:
        for ri, s in enumerate(block["sections"]):
            block["rows"].append({"id": "%s/r%d" % (bid, ri), "min": s["min"], "label": s["title"], "html": inline(s["title"]), "synthetic": True})
    if table:
        orphans, rep = match_rows(block["rows"], block["sections"], None)
    else:
        for r in block["rows"]:
            r["sections"] = []
            r["flag"] = ""
        if block.get("rows") and block["rows"][0].get("synthetic"):
            for r, s in zip(block["rows"], block["sections"]):
                r["sections"] = [s["id"]]
        orphans, rep = [], [(r, None, 1.0, 1.0, "synthetic" if r.get("synthetic") else "") for r in block["rows"]]
    block["orphanSections"] = orphans
    for r in block["rows"]:
        r.pop("synthetic", None)
    reports.append((block, rep))
    return block


# ---------------------------------------------------------------- output

def build_html(data, css, js, artifact=False):
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    stamp = "lesson-plan.qmd sha256:%s built %s" % (data["source"]["sha256"], data["source"]["builtAt"])
    body = f"""<div id="banner" class="banner" hidden></div>
<header id="hdr">
  <div id="clock" class="num"><span id="clockTime">--:--:--</span><small id="clockDate"></small></div>
  <div class="hdr-main">
    <div id="hdrTitle"></div>
    <div class="hdr-nums">
      <div><span class="lbl">running</span><span id="running" class="big num">--:--</span></div>
      <div><span class="lbl">left</span><span id="left" class="big num">--:--</span></div>
    </div>
    <div id="drift" class="num"></div>
  </div>
  <div class="hdr-right"><span id="wake" class="pill">screen may sleep</span><span id="sync" class="pill">this device</span></div>
</header>
<nav class="tabs" aria-label="Pages">
  <button type="button" data-tab="before">Before</button>
  <button type="button" data-tab="day" aria-selected="true">Day</button>
  <button type="button" data-tab="after">After</button>
  <button type="button" data-tab="rules">Rules</button>
  <button type="button" data-tab="log">Log</button>
</nav>
<div class="wrap">
  <section id="tab-day" class="tab day">
    <aside id="blocks" aria-label="Blocks"></aside>
    <div id="panel"></div>
  </section>
  <section id="tab-before" class="tab" hidden>
    <h2 class="tabh">Before the day</h2>
    <ul id="beforelist" class="checks"></ul>
    <h2 class="tabh">Arrival, 08:30 to 09:00</h2>
    <ul id="arrivallist" class="checks"></ul>
    <h2 class="tabh">Materials</h2>
    <ul id="materialslist" class="plain"></ul>
  </section>
  <section id="tab-after" class="tab" hidden>
    <h2 class="tabh">After the room empties</h2>
    <ul id="afterlist" class="checks"></ul>
  </section>
  <section id="tab-rules" class="tab" hidden>
    <h2 class="tabh">Operating rules</h2>
    <ul id="ruleslist" class="plain"></ul>
    <p id="stamp" class="stamp"></p>
  </section>
  <section id="tab-log" class="tab" hidden>
    <h2 class="tabh">Log</h2>
    <div class="logwrap">
    <table class="log">
      <thead><tr><th>Block</th><th>Planned</th><th>Actual</th><th>Minutes</th><th>End drift</th></tr></thead>
      <tbody id="logbody"></tbody>
    </table>
    </div>
    <p id="tickcount" class="stamp"></p>
    <div class="actions">
      <button type="button" id="copybtn" class="btn secondary">Copy log</button>
      <button type="button" id="resetbtn" class="btn quiet">Reset day</button>
    </div>
    <textarea id="exportbox" hidden readonly aria-label="Log as JSON"></textarea>
  </section>
</div>
<script type="application/json" id="ros-data">{payload}</script>
<script>
{js}
</script>
"""
    if artifact:
        return f"""<title>{html.escape(TITLE)}</title>
<meta name="ros-source" content="{html.escape(stamp)}">
<style>
{css}
</style>
{body}"""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Run sheet">
<meta name="theme-color" content="#0F4C81">
<meta name="ros-source" content="{html.escape(stamp)}">
<title>{html.escape(TITLE)}</title>
<style>
{css}
</style>
</head>
<body>
{body}</body>
</html>
"""


def print_report(data, reports):
    nrows = sum(len(b["rows"]) for b in data["blocks"])
    nsecs = sum(len(b["sections"]) for b in data["blocks"])
    flags = {}
    print("blocks %d, rows %d, sections %d, before %d, arrival %d, after %d, rules %d, breaks %d" % (
        len(data["blocks"]), nrows, nsecs, len(data["lists"]["before"]), len(data["lists"]["arrival"]),
        len(data["lists"]["after"]), len(data["rules"]), len(data["breaks"])))
    for block, rep in reports:
        print("\n%s (%s-%s, %d min) %s" % (block["title"], block["start"], block["end"], block["min"], block["tags"] or ""))
        for r, s, ov, jac, flag in rep:
            flags[flag or "ok"] = flags.get(flag or "ok", 0) + 1
            target = s["title"] if s else "-"
            extra = ""
            if len(r["sections"]) > 1:
                extra = " (+%d more)" % (len(r["sections"]) - 1)
            print("  %3s | %-58s -> %-45s %.2f/%.2f %s%s" % (r["min"] if r["min"] is not None else "", plain(r["label"])[:58], target[:45], ov, jac, flag, extra))
        if block["orphanSections"]:
            print("  more notes: %s" % ", ".join(s["title"] for s in block["sections"] if s["id"] in block["orphanSections"]))
    print("\nflags: %s" % ", ".join("%s %d" % kv for kv in sorted(flags.items())))


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--report", action="store_true", help="print the row to section mapping")
    ap.add_argument("--out", metavar="PATH", help="write the artifact body fragment to PATH (publish it with the Artifact tool)")
    ap.add_argument("--page", metavar="PATH", help="write a full standalone HTML document instead, for a look in a local browser")
    ap.add_argument("--json", metavar="PATH", help="also write the data as JSON")
    args = ap.parse_args(argv)
    if not (args.report or args.out or args.page or args.json):
        ap.print_usage()
        return 0

    text = QMD.read_text(encoding="utf-8")
    data, reports = parse(text)
    sha = hashlib.sha256(text.encode("utf-8")).hexdigest()
    data["source"] = {"sha256": sha, "builtAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")}
    if args.report:
        print_report(data, reports)

    css = CSS.read_text(encoding="utf-8")
    js = JS.read_text(encoding="utf-8")
    if args.out:
        Path(args.out).write_text(build_html(data, css, js, artifact=True), encoding="utf-8")
        print("wrote %s (%d blocks, artifact fragment)" % (args.out, len(data["blocks"])))
    if args.page:
        Path(args.page).write_text(build_html(data, css, js), encoding="utf-8")
        print("wrote %s (%d blocks, standalone page)" % (args.page, len(data["blocks"])))
    if args.json:
        Path(args.json).write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
