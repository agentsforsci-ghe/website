#!/usr/bin/env python3
"""Collect structured data about the learner repositories of the
Agents for Scientists workshop (29 September 2026).

Reads the sibling clones of the agentsforsci-ghe learner repositories
(their main branch, dev branch and tags) and the GitHub REST API (issues,
pull requests, releases) and writes the CSV files next to this script.

Usage, from the website repository root:

    python3 evaluation/learner-repos/collect.py --clones .. --gh-cache <dir>

--gh-cache is a directory of cached ``gh api`` responses named
``<repo>.issues.json``, ``<repo>.pulls.json``, ``<repo>.releases.json``
and ``<repo>.repo.json``. Missing files are fetched with ``gh api``.
Only the Python standard library is used.
"""

import argparse
import csv
import json
import os
import re
import subprocess
from collections import Counter, defaultdict
from datetime import datetime

ORG = "agentsforsci-ghe"
WORKSHOP_DAY = "2026-09-29"
LUNCH = "12:00"  # local time; commits before this count as sprint 1

REPOS = [
    "bcmeter-example", "beaver-ss", "biogas-malawi", "caves-currents",
    "cybersecurity-ownership", "ghg-bsfl", "implementation-mzuzu",
    "myco-sanitation", "sensor-validation", "tdabc-mzuzu", "urine-durban",
    "washschools-nigeria", "water-quality-col",
]

# Hand-curated description of each repository. Everything else in the
# CSVs is computed. Keys: domain, data_kind, data_description, toolchain,
# questions_answered (of 3), outcome, open_items.
CURATED = {
    "bcmeter-example": dict(
        domain="Air quality (black carbon sensors)",
        data_kind="Sensor time series (18 CSVs, one notes file)",
        toolchain="none",
        questions_answered=0,
        outcome="Data uploaded for the pre-work; no questions file, no analysis, no workshop-day activity.",
        open_items="Repository never left the pre-work state.",
    ),
    "beaver-ss": dict(
        domain="Freshwater ecology (beaver dams and insect size spectra)",
        data_kind="One processed CSV (89k individuals), Quarto notebook with hypotheses",
        toolchain="R / Quarto (notebook only)",
        questions_answered=0,
        outcome="Pre-work complete with a research-question notebook; no workshop-day activity.",
        open_items="Body mass and size-spectrum fitting still not computed.",
    ),
    "biogas-malawi": dict(
        domain="Household biogas (Malawi)",
        data_kind="One Excel workbook",
        toolchain="none",
        questions_answered=0,
        outcome="Data uploaded for the pre-work and an empty dev branch pushed on 28 September; no workshop-day activity.",
        open_items="Repository never left the pre-work state.",
    ),
    "caves-currents": dict(
        domain="Palaeoclimate (speleothem d18O vs deglacial meltwater)",
        data_kind="SISAL database excerpt (23 CSVs), two discharge model series",
        toolchain="R / Quarto to DOCX, Python stdlib app build, HTML/JS explorer",
        questions_answered=2,
        outcome="Two manuscripts (Glas age range; meltwater sources with a 1,000-member age ensemble, kernel correlation, surrogate tests) and an interactive discharge explorer; CLAUDE.md merged.",
        open_items="Question 3 (Lake Gerzensee age range) has no data in the repo.",
    ),
    "cybersecurity-ownership": dict(
        domain="Cybersecurity survey (merged, anonymised)",
        data_kind="One Excel workbook",
        toolchain="none",
        questions_answered=0,
        outcome="Data uploaded for the pre-work; no questions file, no workshop-day activity.",
        open_items="Repository never left the pre-work state.",
    ),
    "ghg-bsfl": dict(
        domain="Greenhouse gas emissions from black soldier fly larvae",
        data_kind="One summary workbook (daily gas volumes, two chambers)",
        toolchain="R / Quarto to DOCX; converted into an R data package with GitHub Actions CI",
        questions_answered=2,
        outcome="Q1 (gases measured) and Q2 (CO2e per chamber, 5.1 and 6.4 kg) answered with literature comparison; repo turned into an R package with CI; CLAUDE.md written but the tagged commit is on neither main nor dev.",
        open_items="Q3 (E. coli) has no data; issues #5 and #6 (documentation, pkgdown site) open; v0.2.0 tag points at an unmerged commit.",
    ),
    "implementation-mzuzu": dict(
        domain="Sanitation policy (pit-emptier formalisation, qualitative interviews)",
        data_kind="Five interview transcripts and a draft constitution (Word)",
        toolchain="R / Quarto manuscript projects to DOCX; Workflow tool for 20 rater agents",
        questions_answered=2,
        outcome="Q1 (city) and Q2 (formalisation indicators) answered; Q2 re-scored by 20 AI raters on four models with agreement analysis and author adjudication of 29 contested scores; CLAUDE.md on dev only.",
        open_items="Q3 (HIV/AIDS rates) cannot be answered from the interviews; CLAUDE.md and a triangulation plan sit on dev, unmerged.",
    ),
    "myco-sanitation": dict(
        domain="Fungal treatment of dry-toilet material",
        data_kind="Six relational CSVs (mass tracking, setup, baseline, colonisation)",
        toolchain="R / Quarto to DOCX (rendered files gitignored)",
        questions_answered=2,
        outcome="Q1 (raw vs sterile) answered twice, once per model, then improved with literature; Q2 (F40 vs AmBm) answered with mixed models, dry-mass balance, k-rate fan and plateau outlook; CLAUDE.md merged.",
        open_items="Q3 (faecal indicator bacteria) open; issue #4 open.",
    ),
    "sensor-validation": dict(
        domain="Biogas flow sensor validation (lab vs digester)",
        data_kind="Two lab campaigns: 173 CSVs, logs, fit outputs, figures (254 MB)",
        toolchain="R / Quarto to DOCX, Python codebook generator",
        questions_answered=3,
        outcome="All three questions answered in one manuscript, then a second independent report; a generated codebook for all of data/; CLAUDE.md on dev only (tagged v0.2.0).",
        open_items="v0.2.0 tag is on dev, not main; two TODO comments remain in the manuscript.",
    ),
    "tdabc-mzuzu": dict(
        domain="Time-driven activity-based costing of pit emptying (Malawi)",
        data_kind="One task-timing CSV (10,784 rows) plus a cleaned version",
        toolchain="R / Quarto manuscript projects to DOCX, R cleaning script",
        questions_answered=2,
        outcome="Q1 (total job time) and Q2 (travel time to disposal) answered, a data review with flagged rows, a cleaning script and cleaned dataset, and a final manuscript combining both; CLAUDE.md on dev only.",
        open_items="Q3 (worker experience) not started; issue #7 (field verification) open; CLAUDE.md unmerged.",
    ),
    "urine-durban": dict(
        domain="Urine collection incentives (South Africa, 2012-2013 field experiment)",
        data_kind="One CSV (1,535 rows, 750 households)",
        toolchain="R / Quarto to DOCX and HTML",
        questions_answered=2,
        outcome="Q1 (areas) and Q2 (urine production per area and phase) answered, then a comparison with the published papers and a diagnosis of dataset-publication differences (Question 4); CLAUDE.md merged.",
        open_items="Q3 (groundwater quality) not started; two discrepancies need the original Stata files.",
    ),
    "washschools-nigeria": dict(
        domain="School WASH (Nigeria, WASH NORM 2019 survey)",
        data_kind="One third-party Excel conversion of a report annex (PDF gitignored)",
        toolchain="Python / Quarto to DOCX and HTML, matplotlib with LaTeX, conda env",
        questions_answered=2,
        outcome="Q1 (country) and Q2 (students with toilet access) answered; annex tables extracted to 21 tidy CSVs with a data package and codebook; 20 exploratory figures; Q3 started (exposure counts, literature parameters); CLAUDE.md merged.",
        open_items="Q3 scenario model and manuscript (issues #6, #7) open; release assets missing on both releases.",
    ),
    "water-quality-col": dict(
        domain="Drinking water quality index (Colombia, IRCA)",
        data_kind="One national CSV of water quality measurements, admin boundaries",
        toolchain="R / Quarto to DOCX and HTML with leaflet map",
        questions_answered=2,
        outcome="Q1 (observational unit) and Q2 (completeness) answered in one manuscript with a municipal IRCA map, then an HTML output with sortable table and interactive map; CLAUDE.md on dev only.",
        open_items="Q3 (coverage of drinking water service) not started; CLAUDE.md and codebook unmerged.",
    ),
}

# Prompt classification. First matching rule wins. The stage names follow
# the workshop day: framed run, studio cards, plan mode, issues, the TODO
# pass, CLAUDE.md.
PROMPT_RULES = [
    ("plan_only", r"plan only|do not run any analysis|don'?t implement yet|make a plan|create a plan|plan how|wr?ite a plan|show me the plan"),
    ("plan_answers", r"askuserquestion|planning questions"),
    ("plan_to_markdown", r"plan as (an? )?(md|markdown)|write the plan as md|plan as md"),
    ("issues_from_plan", r"into four issues|as (a series of )?issues|post the plan"),
    ("implement_issues", r"implement (all )?(the )?(issues|issues? one|issues? 1|the first issue|the remaining issues|plan)|continue with the (next|plan)|execute the plan|go on"),
    ("todo_pass", r"todo"),
    ("claude_md", r"claude\.?md"),
    ("framed_run_q1", r"^answer\w* the (following|first) question.*(quarto|manuscript)|answer the following question using the data in this repo.*(quarto|docx)"),
    ("card9_same_task_twice", r"same (input|task) again|again using"),
    ("card1_add_question", r"add the result to the manuscript|answer question 2|move on to question 2|solve question 2|answer the following question.*question 2"),
    ("card2_unanswerable", r"e\.? ?coli|how much .* present"),
    ("card3_codebook", r"codebook|describe every file"),
    ("card4_figure_render", r"figure.*(chunk|render)|plot.*render"),
    ("card5_references", r"zotero|references"),
    ("card6_readme", r"readme|read me"),
    ("data_review", r"inconsisten|data review|flagged|problematic"),
    ("context_source", r"where does the data come from|see also this paper|what paper|which paper|citation|impulse response|reviewer"),
    ("extension_analysis", r"plot|figure|map|html|unify|harmonize|verfeinern|probier|assumption|recommend|branch called|more accurate|the report itself says|add the numbers|write up a qmd|extract"),
    ("steer_followup", r"^(yes|ok|fix it|rename|go on|continue|i'?ve input|pull main)"),
    ("release", r"release|tag v"),
    ("pull_request", r"\bpr\b|pull request"),
    ("other", r"."),
]

STAGE_SPRINT = {
    "framed_run_q1": "1", "card1_add_question": "1", "card2_unanswerable": "1",
    "card3_codebook": "1", "card4_figure_render": "1", "card5_references": "1",
    "card6_readme": "1", "plan_only": "2", "plan_to_markdown": "2",
    "issues_from_plan": "2", "implement_issues": "2", "todo_pass": "2",
    "claude_md": "2", "plan_answers": "2", "card9_same_task_twice": "1",
    "data_review": "", "context_source": "", "extension_analysis": "",
    "steer_followup": "", "release": "", "pull_request": "", "other": "",
}


def git(repo_dir, *args):
    return subprocess.run(["git", "-C", repo_dir, *args], check=True,
                          capture_output=True, text=True).stdout


def gh_json(cache, repo, kind):
    path = os.path.join(cache, f"{repo}.{kind}.json")
    if not os.path.exists(path):
        url = {
            "issues": f"repos/{ORG}/{repo}/issues?state=all&per_page=100",
            "pulls": f"repos/{ORG}/{repo}/pulls?state=all&per_page=100",
            "releases": f"repos/{ORG}/{repo}/releases?per_page=100",
            "repo": f"repos/{ORG}/{repo}",
        }[kind]
        out = subprocess.run(["gh", "api", url], check=True,
                             capture_output=True, text=True).stdout
        os.makedirs(cache, exist_ok=True)
        with open(path, "w") as fh:
            fh.write(out)
    with open(path) as fh:
        return json.load(fh)


def local_time(iso):
    """'2026-09-29T10:21:05+02:00' -> ('2026-09-29', '10:21')."""
    return iso[:10], iso[11:16]


def parse_commits(repo, repo_dir):
    sep = "\x1e"
    # Stats first: one record per commit, "sha<sep>shortstat line".
    stats = {}
    raw = git(repo_dir, "log", "main", "--format=%x1e%h", "--shortstat")
    for rec in raw.split(sep)[1:]:
        lines = [l for l in rec.splitlines() if l.strip()]
        stats[lines[0].strip()] = " ".join(lines[1:])
    fmt = f"%H{sep}%h{sep}%aI{sep}%an{sep}%P{sep}%s{sep}%B{sep}"
    raw = git(repo_dir, "log", "main", f"--format={fmt}")
    rows = []
    for block in raw.split(sep + "\n"):
        block = block.strip("\n")
        if not block.strip():
            continue
        parts = block.split(sep)
        if len(parts) < 7:
            continue
        sha, short, date, author, parents, subject, body = parts[:7]
        stat = stats.get(short, "")
        files = ins = dele = 0
        m = re.search(r"(\d+) files? changed", stat)
        if m:
            files = int(m.group(1))
        m = re.search(r"(\d+) insertion", stat)
        if m:
            ins = int(m.group(1))
        m = re.search(r"(\d+) deletion", stat)
        if m:
            dele = int(m.group(1))
        trailers = dict(assisted=[], coauthor=[], prompts=[], human=False)
        for line in body.splitlines():
            if line.startswith("Assisted-by:"):
                trailers["assisted"] += re.findall(r"claude-[a-z0-9-]+", line)
            elif line.startswith("Co-Authored-By: Claude"):
                trailers["coauthor"].append(
                    line.split(":", 1)[1].split("<")[0].strip())
            elif line.strip().startswith("- 2026-") and "prompt" in body.lower():
                trailers["prompts"].append(line.strip()[2:])
            elif line.startswith("Human-authored: true"):
                trailers["human"] = True
        m = re.match(r"^(\w+)(\([^)]*\))?!?: ", subject)
        cc_type = m.group(1) if m else ""
        is_merge = len(parents.split()) > 1
        day, hhmm = local_time(date)
        if is_merge:
            path = "merge"
        elif trailers["assisted"]:
            path = "assisted"
        elif trailers["coauthor"]:
            path = "co-authored"
        else:
            path = "human"
        sprint = ""
        if day == WORKSHOP_DAY:
            sprint = "1" if hhmm < LUNCH else "2"
        rows.append(dict(
            repo=repo, sha=short, author_datetime=date, date=day,
            time_local=hhmm, author=author, subject=subject,
            conventional_type=cc_type, is_merge=int(is_merge),
            author_path=path,
            assisted_models=";".join(sorted(set(trailers["assisted"]))),
            co_authored_model=";".join(trailers["coauthor"]),
            n_prompts_cited=len(trailers["prompts"]),
            human_authored_flag=int(trailers["human"]),
            files_changed=files, insertions=ins, deletions=dele,
            on_workshop_day=int(day == WORKSHOP_DAY), sprint=sprint,
        ))
    rows.reverse()  # oldest first
    return rows


def parse_prompts(repo, repo_dir):
    files = [f for f in git(repo_dir, "ls-tree", "-r", "--name-only", "main").splitlines()
             if f.startswith("prompts/") and f.endswith(".md")]
    rows = []
    for f in sorted(files):
        text = git(repo_dir, "show", f"main:{f}")
        front, body = {}, text
        if text.startswith("---"):
            parts = text.split("---", 2)
            if len(parts) == 3:
                front_txt, body = parts[1], parts[2]
                for line in front_txt.splitlines():
                    if ":" in line and not line.startswith(" "):
                        k, v = line.split(":", 1)
                        front[k.strip()] = v.strip()
                front["n_files"] = sum(1 for l in front_txt.splitlines() if l.strip().startswith("- "))
        body = body.strip()
        stage = "other"
        for name, pat in PROMPT_RULES:
            if re.search(pat, body, re.I):
                stage = name
                break
        lang = "de" if re.search(r"\b(und|der|die|das|nicht|kannst|probier)\b", body, re.I) else "en"
        rows.append(dict(
            repo=repo, prompt_id=front.get("id", os.path.basename(f)[:-3]),
            timestamp=front.get("timestamp", ""), model=front.get("model", ""),
            n_files_touched=front.get("n_files", 0), stage=stage,
            sprint=STAGE_SPRINT.get(stage, ""), language=lang,
            n_words=len(body.split()),
            prompt_text=" ".join(body.split())[:300],
        ))
    return rows


def tag_info(repo_dir):
    out = {}
    for t in git(repo_dir, "tag").split():
        sha = git(repo_dir, "rev-list", "-n1", t).strip()
        date = git(repo_dir, "log", "-1", "--format=%aI", sha).strip()
        def anc(ref):
            return subprocess.run(["git", "-C", repo_dir, "merge-base", "--is-ancestor", sha, ref]).returncode == 0
        where = "main" if anc("main") else ("dev" if anc("origin/dev") else "unmerged")
        out[t] = dict(sha=sha[:7], date=date, where=where)
    return out


def file_where(repo_dir, path):
    """Return main/dev/tag/none depending on where a file first exists."""
    def exists(ref):
        return subprocess.run(["git", "-C", repo_dir, "cat-file", "-e", f"{ref}:{path}"],
                              capture_output=True).returncode == 0
    if exists("main"):
        return "main"
    if subprocess.run(["git", "-C", repo_dir, "rev-parse", "-q", "--verify", "origin/dev"],
                      capture_output=True).returncode == 0 and exists("origin/dev"):
        return "dev"
    for t in git(repo_dir, "tag").split():
        if exists(t):
            return "tag-only"
    return "none"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--clones", required=True)
    ap.add_argument("--gh-cache", required=True)
    ap.add_argument("--out", default=os.path.dirname(os.path.abspath(__file__)))
    a = ap.parse_args()

    commits, prompts, issues, pulls, releases, repos, milestones = [], [], [], [], [], [], []

    for repo in REPOS:
        d = os.path.join(a.clones, repo)
        subprocess.run(["git", "-C", d, "fetch", "-q", "origin", "dev", "refs/tags/*:refs/tags/*"],
                       capture_output=True)
        c_rows = parse_commits(repo, d)
        p_rows = parse_prompts(repo, d)
        commits += c_rows
        prompts += p_rows
        tags = tag_info(d)
        meta = gh_json(a.gh_cache, repo, "repo")
        iss = [i for i in gh_json(a.gh_cache, repo, "issues") if not i.get("pull_request")]
        prs = gh_json(a.gh_cache, repo, "pulls")
        rels = gh_json(a.gh_cache, repo, "releases")

        for i in iss:
            body = i.get("body") or ""
            issues.append(dict(
                repo=repo, number=i["number"], state=i["state"], title=i["title"],
                author=i["user"]["login"], created_at=i["created_at"],
                closed_at=i.get("closed_at") or "", n_checkboxes=len(re.findall(r"- \[[ x]\]", body)),
                body_chars=len(body),
                kind="pre-work" if i["title"].lower().strip() in ("data added", "setup complete") else "workshop",
            ))
        for p in prs:
            pulls.append(dict(
                repo=repo, number=p["number"], state=p["state"], title=p["title"],
                author=p["user"]["login"], head=p["head"]["ref"], base=p["base"]["ref"],
                created_at=p["created_at"], merged_at=p.get("merged_at") or "",
                merged=int(bool(p.get("merged_at"))),
                sprint="1" if p["created_at"] < f"{WORKSHOP_DAY}T10:00:00Z" else "2",
                body_chars=len(p.get("body") or ""),
            ))
        for r in rels:
            body = r.get("body") or ""
            releases.append(dict(
                repo=repo, tag=r["tag_name"], name=r.get("name") or "",
                created_at=r["created_at"], author=r["author"]["login"],
                n_assets=len(r.get("assets") or []),
                assets=";".join(x["name"] for x in r.get("assets") or []),
                body_chars=len(body),
                has_declaration=int(bool(re.search(r"declaration of ai use", body, re.I))),
                declaration_chars=(len(body.split("Declaration of AI use", 1)[1])
                                   if "Declaration of AI use" in body else 0),
                tag_commit=tags.get(r["tag_name"], {}).get("sha", ""),
                tag_on=tags.get(r["tag_name"], {}).get("where", ""),
            ))

        cur = CURATED[repo]
        day = [c for c in c_rows if c["on_workshop_day"]]
        paths = Counter(c["author_path"] for c in c_rows)
        models = Counter()
        for c in c_rows:
            for m in c["assisted_models"].split(";"):
                if m:
                    models[m] += 1
        tree = git(d, "ls-tree", "-r", "--name-only", "main").splitlines()
        sizes = sum(int(l.split()[3]) for l in git(d, "ls-tree", "-r", "-l", "main").splitlines())
        qfile = next((f for f in ("questions.md", "QUESTIONS.md", "docs/questions.md") if f in tree), "")
        n_questions = 0
        if qfile:
            qtxt = git(d, "show", f"main:{qfile}")
            n_questions = len([l for l in qtxt.splitlines() if re.match(r"^\s*(\d+\.|-)\s*\S", l) or l.strip().endswith("?")])
            n_questions = min(n_questions, 3) if n_questions else 0
        claude_md = file_where(d, "CLAUDE.md")
        dev_ahead = int(git(d, "rev-list", "--count", "main..origin/dev").strip()) if subprocess.run(
            ["git", "-C", d, "rev-parse", "-q", "--verify", "origin/dev"], capture_output=True).returncode == 0 else 0
        participated = int(bool(day))
        stages = Counter(p["stage"] for p in p_rows)
        rel_by_tag = {r["tag"]: r for r in releases if r["repo"] == repo}
        first = day[0]["time_local"] if day else ""
        last = day[-1]["time_local"] if day else ""

        repos.append(dict(
            repo=repo, owner_login=meta["owner"]["login"] if meta.get("owner", {}).get("type") == "User" else next((i["author"] for i in issues if i["repo"] == repo), ""),
            visibility="private" if meta.get("private") else "public",
            repo_created=meta["created_at"][:10], last_push=meta["pushed_at"][:19],
            participated_on_day=participated,
            domain=cur["domain"], data_kind=cur["data_kind"], toolchain=cur["toolchain"],
            tracked_files=len(tree), tracked_mb=round(sizes / 1048576, 1),
            n_commits_main=len(c_rows), n_commits_workshop_day=len(day),
            n_commits_sprint1=sum(1 for c in day if c["sprint"] == "1"),
            n_commits_sprint2=sum(1 for c in day if c["sprint"] == "2"),
            first_commit_day=first, last_commit_day=last,
            n_human=paths["human"], n_assisted=paths["assisted"],
            n_co_authored=paths["co-authored"], n_merge=paths["merge"],
            n_conventional=sum(1 for c in c_rows if c["conventional_type"]),
            models_in_trailers=";".join(f"{k}:{v}" for k, v in sorted(models.items())),
            n_prompts_archived=len(p_rows),
            n_prompts_de=sum(1 for p in p_rows if p["language"] == "de"),
            prompt_stages=";".join(f"{k}:{v}" for k, v in sorted(stages.items())),
            questions_file=qfile, n_questions=n_questions,
            questions_answered=cur["questions_answered"],
            n_qmd=sum(1 for f in tree if f.endswith(".qmd") and not f.startswith("notebooks/")),
            n_docx_tracked=sum(1 for f in tree if f.endswith(".docx")),
            n_html_tracked=sum(1 for f in tree if f.endswith(".html")),
            n_plan_files=sum(1 for f in tree if not f.startswith("prompts/") and re.search(r"(^|/)plans?/|(^|/)plan[-_a-z0-9]*\.md$|[-_]plan\.md$|PLAN\.md$", f)),
            claude_md=claude_md,
            n_issues_workshop=sum(1 for i in issues if i["repo"] == repo and i["kind"] == "workshop"),
            n_issues_closed=sum(1 for i in issues if i["repo"] == repo and i["kind"] == "workshop" and i["state"] == "closed"),
            n_prs=sum(1 for p in pulls if p["repo"] == repo),
            n_prs_merged=sum(1 for p in pulls if p["repo"] == repo and p["merged"]),
            n_pr_reviews=0,  # checked via the API: no formal reviews on any PR
            v010_time=rel_by_tag.get("v0.1.0", {}).get("created_at", "")[11:16],
            v010_assets=rel_by_tag.get("v0.1.0", {}).get("n_assets", ""),
            v020_time=rel_by_tag.get("v0.2.0", {}).get("created_at", "")[11:16],
            v020_assets=rel_by_tag.get("v0.2.0", {}).get("n_assets", ""),
            v020_tag_on=rel_by_tag.get("v0.2.0", {}).get("tag_on", ""),
            declaration_in_v020=rel_by_tag.get("v0.2.0", {}).get("has_declaration", 0),
            declaration_chars=rel_by_tag.get("v0.2.0", {}).get("declaration_chars", 0),
            dev_ahead_of_main=dev_ahead,
            outcome=cur["outcome"], open_items=cur["open_items"],
        ))

        # Milestones of the workshop day, one row each, with evidence.
        def ms(key, label, status, evidence):
            milestones.append(dict(repo=repo, milestone=key, label=label, status=status, evidence=evidence))
        pre = [i for i in issues if i["repo"] == repo and i["kind"] == "pre-work"]
        ms("M01", "Pre-work: data in repo and 'Data added' issue", "yes" if pre else "partial",
           f"issue #{pre[0]['number']}" if pre else "data committed, no issue")
        ms("M02", "Three questions file", "yes" if qfile else "no", qfile or "")
        fr = [p for p in p_rows if p["stage"] == "framed_run_q1"]
        ms("M03", "Framed run: Q1 as Quarto manuscript", "yes" if fr else ("partial" if any(f.endswith(".qmd") for f in tree) else "no"),
           fr[0]["prompt_id"] if fr else "")
        ms("M04", "Commit skill: Assisted-by trailer and prompt archive", "yes" if paths["assisted"] and p_rows else "no",
           f"{paths['assisted']} assisted commits, {len(p_rows)} prompts")
        cards = sorted({p["stage"] for p in p_rows if p["stage"].startswith("card")})
        ms("M05", "Studio cards (evidenced in prompt archive)", "yes" if cards else "no", ";".join(cards))
        pr1 = [p for p in pulls if p["repo"] == repo and p["sprint"] == "1" and p["merged"]]
        ms("M06", "Sprint 1 pull request dev->main merged", "yes" if pr1 else "no",
           f"PR #{pr1[0]['number']} merged {pr1[0]['merged_at'][11:16]}Z" if pr1 else "")
        r1 = rel_by_tag.get("v0.1.0")
        ms("M07", "Release v0.1.0 with DOCX attached", "yes" if r1 and r1["n_assets"] else ("partial" if r1 else "no"),
           f"{r1['created_at'][11:16]}Z, {r1['n_assets']} assets" if r1 else "")
        pl = [p for p in p_rows if p["stage"] == "plan_only"]
        ms("M08", "Plan mode: 'plan only' prompt", "yes" if pl else "no", pl[0]["prompt_id"] if pl else "")
        ms("M09", "Plan written as markdown in repo", "yes" if repos[-1]["n_plan_files"] else "no", f"{repos[-1]['n_plan_files']} plan files")
        wi = [i for i in issues if i["repo"] == repo and i["kind"] == "workshop"]
        ms("M10", "Issues created from the plan", "yes" if wi else "no",
           f"{len(wi)} issues, {sum(1 for i in wi if i['n_checkboxes'])} with checkboxes")
        ms("M11", "Issues implemented and closed", "yes" if any(i["state"] == "closed" for i in wi) else "no",
           f"{sum(1 for i in wi if i['state']=='closed')} of {len(wi)} closed")
        ms("M12", "Run continued from the phone", "not observable", "no trace in git or GitHub")
        tp = [p for p in p_rows if p["stage"] == "todo_pass"]
        todo_commit = [c for c in c_rows if re.search(r"todo", c["subject"], re.I) and c["author_path"] == "human"]
        ms("M13", "TODO pass: human review comments in source, agent works through them",
           "yes" if (tp or todo_commit) else "no", (todo_commit[0]["sha"] + " + " if todo_commit else "") + (tp[0]["prompt_id"] if tp else ""))
        pr2 = [p for p in pulls if p["repo"] == repo and p["sprint"] == "2" and p["merged"]]
        ms("M14", "Sprint 2 pull request merged", "yes" if pr2 else "no",
           ";".join(f"#{p['number']}" for p in pr2))
        ms("M15", "Partner review as a GitHub review", "no", "0 reviews, 0 review comments on any PR (API)")
        ms("M16", "CLAUDE.md written", "yes" if claude_md != "none" else "no", f"on {claude_md}")
        r2 = rel_by_tag.get("v0.2.0")
        ms("M17", "Release v0.2.0", "yes" if r2 else "no",
           f"{r2['created_at'][11:16]}Z, {r2['n_assets']} assets, tag on {r2['tag_on']}" if r2 else "")
        ms("M18", "Declaration of AI use in the v0.2.0 notes", "yes" if r2 and r2["has_declaration"] else "no",
           f"{r2['declaration_chars']} characters" if r2 and r2["has_declaration"] else "")

    def write(name, rows):
        if not rows:
            return
        with open(os.path.join(a.out, name), "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)

    write("repos.csv", repos)
    write("commits.csv", commits)
    write("prompts.csv", prompts)
    write("issues.csv", issues)
    write("pulls.csv", pulls)
    write("releases.csv", releases)
    write("milestones.csv", milestones)
    print(f"{len(repos)} repos, {len(commits)} commits, {len(prompts)} prompts, "
          f"{len(issues)} issues, {len(pulls)} PRs, {len(releases)} releases, {len(milestones)} milestone rows")


if __name__ == "__main__":
    main()
