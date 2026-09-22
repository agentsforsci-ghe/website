#!/usr/bin/env python3
"""Build glossary.yml from glossary.qmd, and give every term an anchor.

glossary.qmd is the page people read and the file Lars edits. Each entry is a
definition-list item: a term line, then one or more ":   " paragraphs (the
plain definition), then optionally a ::: {.glossary-technical} block. This
script

  1. makes sure every term line carries an anchor, [term]{#gl-slug}, so the
     popovers can link to the entry, and
  2. writes glossary.yml with the plain definition of every term, plus a few
     aliases, for the gl shortcode (_extensions/ghe/gl).

Run by Quarto before every render (project: pre-render in _quarto.yml).
Standard library only. glossary.yml carries no comment header because pandoc
reads it as a metadata block, which must start with a key.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QMD = ROOT / "glossary.qmd"
YML = ROOT / "glossary.yml"

# alias -> canonical term (lowercase). Aliases resolve in the shortcode.
ALIASES = {
    "pat": "personal access token",
    "main": "default branch",
    "staging area": "stage",
    "staging": "stage",
    "model context protocol": "mcp",
    "mcp server": "mcp",
    "pull requests": "pull request",
    "commits": "commit",
    "repositories": "repository",
    "issues": "issue",
    "prompts": "prompt",
    "agents": "agent",
    "tools": "tool",
    "sessions": "session",
    "tokens": "token",
    "branches": "branch",
    "clones": "clone",
    "cloning": "clone",
    "commit messages": "commit message",
    "tool calls": "tool call",
    "citation keys": "citation key",
    "skills": "skill",
    "trailers": "trailer",
    "diffs": "diff",
    "declarations": "declaration",
    "watermarks": "watermark",
    "terminals": "terminal",
    "models": "model",
    "credentials": "credential",
    "permissions": "permission",
    "data packages": "data package",
    "servers": "server",
    "merges": "merge",
    "pushes": "push",
    "stages": "stage",
}


def slug(term: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", term.lower()).strip("-")
    return s


def canonical(term_line: str) -> str:
    """The bare term: strip an existing anchor span and parentheticals."""
    m = re.match(r"^\[(.+?)\]\{#gl-[^}]+\}$", term_line.strip())
    t = m.group(1) if m else term_line.strip()
    t = re.sub(r"\s*\(.*?\)\s*$", "", t)   # "MCP (Model Context Protocol)" -> "MCP"
    t = t.split(" / ")[0]                   # "stage / staging area" -> "stage"
    return t.strip("` ").strip()


def main() -> int:
    lines = QMD.read_text(encoding="utf-8").split("\n")
    n = len(lines)
    out_lines = list(lines)          # only term lines are rewritten
    entries = {}
    changed = False
    for i, line in enumerate(lines):
        is_term = (
            line.strip()
            and not line.startswith((":", " ", "#", "-", "!", "|", "<", "{"))
            and i + 1 < n
            and lines[i + 1].startswith(":   ")
        )
        if not is_term:
            continue
        term = canonical(line)
        key = term.lower()
        m = re.match(r"^\[(.+?)\]\{#gl-[^}]+\}$", line.strip())
        display = m.group(1) if m else line.strip()
        anchored = f"[{display}]{{#gl-{slug(term)}}}"
        if anchored != line.strip():
            out_lines[i] = anchored
            changed = True
        # plain definition: the first ":   " paragraph, with its continuation lines
        j = i + 1
        cur = [lines[j][4:]]
        j += 1
        while j < n and lines[j].startswith("    ") and not lines[j].strip().startswith(":::"):
            cur.append(lines[j][4:])
            j += 1
        if key in entries:
            print(f"build_glossary: duplicate term '{term}'", file=sys.stderr)
            return 1
        entries[key] = " ".join(x.strip() for x in cur)
    if changed:
        QMD.write_text("\n".join(out_lines), encoding="utf-8")
    y = []
    for key in sorted(entries):
        y.append(f"{key}: |")
        y.append(f"  {entries[key]}")
    for alias, target in sorted(ALIASES.items()):
        if target in entries and alias not in entries:
            y.append(f"{alias}:")
            y.append("  alias: true")
            y.append(f"  of: \"{target}\"")
    YML.write_text("\n".join(y) + "\n", encoding="utf-8")
    print(f"build_glossary: {len(entries)} terms, "
          f"{sum(1 for a, t in ALIASES.items() if t in entries)} aliases -> glossary.yml"
          + (", anchors added to glossary.qmd" if changed else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
