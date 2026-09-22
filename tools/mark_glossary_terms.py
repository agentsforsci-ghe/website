#!/usr/bin/env python3
"""Wrap the first prose occurrence of each glossary term on a page in the gl
shortcode, {{< gl term >}} or {{< gl term display="Text" >}}.

One occurrence per term per page. Skipped: YAML front matter, code fences,
inline code, headings, blockquotes (the prompts people copy), tables,
shortcodes, links, attribute spans, and bold runs. Terms whose meaning
shifts between pages are not in the list (prompt, token, tool, session,
model on its own, Git, GitHub, RStudio).

Usage: tools/mark_glossary_terms.py FILE...    (edits in place, prints counts)
"""
import re
import sys

# canonical term -> forms that count as that term (case-insensitive)
TERMS = {
    "agent": ["agent", "agents"],
    "auto mode": ["auto mode"], "manual mode": ["manual mode"], "plan mode": ["plan mode"],
    "classifier": ["classifier"], "skill": ["skill", "skills"], "trailer": ["trailer", "trailers"],
    "data package": ["data package", "data packages"], "declaration": ["declaration"],
    "disclosure": ["disclosure"], "watermark": ["watermark", "watermarks"],
    "content credentials": ["content credentials"], "citation key": ["citation key", "citation keys"],
    "Better BibTeX": ["Better BibTeX"], "Zotero Connector": ["Zotero Connector", "connector"],
    "Quick Copy": ["Quick Copy"], "zotero-mcp": ["zotero-mcp"], "mcptools": ["mcptools"],
    "uv": ["uv"], "Homebrew": ["Homebrew"], "GitHub CLI": ["GitHub CLI"], "PowerShell": ["PowerShell"],
    "terminal": ["terminal"], "shell": ["shell"], "Console": ["Console"],
    "R session": ["R session"], "R profile": ["R profile"], "diff": ["diff", "diffs"],
    "branch": ["branch", "branches"], "pull request": ["pull request", "pull requests"],
    "commit message": ["commit message", "commit messages"], "commit": ["commit", "commits"],
    "push": ["push"], "pull": ["pull"], "stage": ["stage"], "clone": ["clone"], "merge": ["merge"],
    "issue": ["issue", "issues"], "repository": ["repository", "repositories"],
    "README": ["README"], "permission": ["permission"], "history": ["history"],
    "metadata": ["metadata"], "plain text": ["plain text"], "Markdown": ["Markdown"],
    "open source": ["open source"], "version control": ["version control"],
    "credential": ["credentials", "credential"], "personal access token": ["personal access token"],
    "Git pane": ["Git pane"], "render": ["render"], "server": ["server", "servers"],
    "cloud": ["cloud"], "MCP": ["MCP"], "context window": ["context window"],
    "hallucination": ["hallucination", "hallucinations"], "sandbox": ["sandbox"],
}
CASE_SENSITIVE = {"Console", "uv", "MCP", "README"}   # avoid 'console' and 'UV' elsewhere

# terms whose meaning on a given page is not the glossary's
EXCLUDE = {
    "pre-work/01-create-repository.qmd": {"permission"},   # permission to commit = licence
    "pre-work/05-github-cli.qmd": {"pull"},                 # only inside "pull request"
    "pre-work/06-connect-r.qmd": {"server"},                # the MCP server, not a machine
    "pre-work/08-zotero-mcp.qmd": {"server", "pull"},       # same, and pull = fetch
    "background/literacy.qmd": {"skill"},                   # a human skill
}

def protected_ranges(text):
    rs = []
    m = re.match(r"^---\n.*?\n---\n", text, re.S)
    if m: rs.append((0, m.end()))
    for rx in [r"```.*?```", r"`[^`\n]*`", r"\{\{<.*?>\}\}", r"\[[^\]\n]*\]\([^)\n]*\)",
               r"\[[^\]\n]*\]\{[^}\n]*\}", r"\*\*[^*\n]+\*\*", r"<[^>\n]+>"]:
        for m in re.finditer(rx, text, re.S): rs.append((m.start(), m.end()))
    # whole lines: headings, blockquotes, tables, fences, div fences, due line
    for m in re.finditer(r"^(#|>|\||:::|\[Due by).*$", text, re.M): rs.append((m.start(), m.end()))
    return rs

def inside(pos, end, rs):
    return any(a <= pos < b or a < end <= b for a, b in rs)

def mark(path):
    text = open(path, encoding="utf-8").read()
    rs = protected_ranges(text)
    done = 0
    # longer forms first so "pull request" wins over "pull"
    order = sorted(TERMS.items(), key=lambda kv: -max(len(f) for f in kv[1]))
    longer_forms = [f for fs in TERMS.values() for f in fs if " " in f]
    excluded = EXCLUDE.get(path, set())
    for term, forms in order:
        if term in excluded:
            continue
        if re.search(r"\{\{< gl \"?" + re.escape(term) + r"\"?[ >]", text):
            continue   # already marked on this page: the script is safe to re-run
        placed = False
        for form in sorted(forms, key=len, reverse=True):
            flags = 0 if term in CASE_SENSITIVE else re.I
            for m in re.finditer(r"(?<![\w-])" + re.escape(form) + r"(?![\w-])", text, flags):
                if inside(m.start(), m.end(), rs): continue
                # a single word that is part of a longer term here, e.g. "pull" in "pull request"
                if " " not in form and any(
                    re.search(r"(?<![\w-])" + re.escape(lf) + r"(?![\w-])",
                              text[max(0, m.start() - 40):m.end() + 40], re.I)
                    and lf.lower() != form.lower()
                    and re.search(r"(?<![\w-])" + re.escape(form) + r"(?![\w-])", lf, re.I)
                    for lf in longer_forms):
                    continue
                shown = m.group(0)
                key = term if " " not in term else f'"{term}"'
                sc = f"{{{{< gl {key} >}}}}" if shown == term else f'{{{{< gl {key} display="{shown}" >}}}}'
                text = text[:m.start()] + sc + text[m.end():]
                delta = len(sc) - len(shown)
                rs = [(a if a < m.start() else a + delta, b if b <= m.start() else b + delta) for a, b in rs]
                rs.append((m.start(), m.start() + len(sc)))
                done += 1; placed = True
                break
            if placed: break
    open(path, "w", encoding="utf-8").write(text)
    return done

if __name__ == "__main__":
    total = 0
    for p in sys.argv[1:]:
        n = mark(p); total += n; print(f"{n:3d}  {p}")
    print(f"{total:3d}  total")
