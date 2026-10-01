# Learner repositories: structured record of the workshop day

Structured data about the thirteen learner repositories of the Agents for
Scientists workshop (29 September 2026), collected on 1 October 2026 from
the repositories' `main` and `dev` branches, their tags, and the GitHub
REST API (issues, pull requests, releases). The two reports that read this
data are `report.md` (long) and `summary.md` (one page).

Everything in the CSV files is computed by `collect.py`, except the
hand-written `domain`, `data_kind`, `toolchain`, `questions_answered`,
`outcome` and `open_items` columns of `repos.csv`, which live in the
`CURATED` table at the top of the script.

## Rerun

```
python3 evaluation/learner-repos/collect.py --clones <dir with one clone per repo> --gh-cache <dir>
```

The clones need `main`, `origin/dev` and the tags fetched. `--gh-cache`
holds the `gh api` responses (`<repo>.issues.json`, `.pulls.json`,
`.releases.json`, `.repo.json`); missing files are fetched. Only the Python
standard library is used.

## Files

| File | One row per | Rows |
|---|---|---|
| `repos.csv` | repository | 13 |
| `commits.csv` | commit on `main` | 176 |
| `prompts.csv` | archived prompt under `prompts/` | 111 |
| `issues.csv` | GitHub issue (pull requests excluded) | 50 |
| `pulls.csv` | pull request | 23 |
| `releases.csv` | GitHub release | 18 |
| `milestones.csv` | repository × workshop-day milestone | 234 |

Times in `*_time*` columns and in `first_commit_day` / `last_commit_day`
are local (Europe/Zurich, +02:00) as written by git. The GitHub timestamps
(`created_at`, `merged_at`, `closed_at`) are UTC, two hours behind.

### repos.csv

| Column | Meaning |
|---|---|
| `repo`, `owner_login`, `visibility`, `repo_created`, `last_push` | From the GitHub API. `owner_login` is the author of the pre-work issue, since all repos belong to the organisation. |
| `participated_on_day` | 1 if any commit on `main` is dated 29 September 2026. |
| `domain`, `data_kind`, `toolchain` | Hand-written. |
| `tracked_files`, `tracked_mb` | Files and bytes in the `main` tree. |
| `n_commits_main`, `n_commits_workshop_day`, `n_commits_sprint1`, `n_commits_sprint2` | Commit counts; sprint 1 is before 12:00 local on the day, sprint 2 after. |
| `first_commit_day`, `last_commit_day` | Local time of the first and last commit on the day. |
| `n_human`, `n_assisted`, `n_co_authored`, `n_merge` | Author path of each commit: `assisted` has an `Assisted-by: Claude <model>` trailer (the commit skill), `co-authored` has the older `Co-Authored-By: Claude …` line, `merge` has two parents, `human` has neither. |
| `n_conventional` | Commits whose subject follows Conventional Commits (`type(scope): …`). |
| `models_in_trailers` | Count of `Assisted-by` commits per model id. |
| `n_prompts_archived`, `n_prompts_de`, `prompt_stages` | Prompt archive size, prompts in German, and the count per stage (see `prompts.csv`). |
| `questions_file`, `n_questions`, `questions_answered` | The three-questions file, how many questions it lists, and how many a manuscript answers (hand-checked). |
| `n_qmd`, `n_docx_tracked`, `n_html_tracked`, `n_plan_files` | Quarto sources (notebooks excluded), rendered outputs committed, plan documents in the tree. |
| `claude_md` | Where `CLAUDE.md` exists: `main`, `dev` (only on dev), `tag-only` (only reachable from a tag), `none`. |
| `n_issues_workshop`, `n_issues_closed` | Issues other than the pre-work "Data added" / "Setup complete" issues. |
| `n_prs`, `n_prs_merged`, `n_pr_reviews` | Pull requests; reviews were checked per PR through the API and are zero everywhere. |
| `v010_time`, `v010_assets`, `v020_time`, `v020_assets`, `v020_tag_on` | Release time (UTC), number of attached files, and whether the v0.2.0 tag commit is on `main`, only on `dev`, or `unmerged` (on neither). |
| `declaration_in_v020`, `declaration_chars` | Whether the v0.2.0 notes contain a "Declaration of AI use" section, and its length. |
| `dev_ahead_of_main` | Commits on `origin/dev` not on `main` at collection time. |
| `outcome`, `open_items` | Hand-written, two sentences each. |

### commits.csv

`repo`, `sha`, `author_datetime` (ISO with offset), `date`, `time_local`,
`author`, `subject`, `conventional_type`, `is_merge`, `author_path` (as
above), `assisted_models`, `co_authored_model`, `n_prompts_cited` (entries
in the `Prompts:` trailer), `human_authored_flag` (`Human-authored: true`
trailer), `files_changed`, `insertions`, `deletions`, `on_workshop_day`,
`sprint`.

### prompts.csv

`repo`, `prompt_id`, `timestamp` and `model` (from the file's front
matter; timestamps are the learner's or the skill's estimate, several are
`00:00:00`), `n_files_touched`, `stage`, `sprint`, `language`, `n_words`,
`prompt_text` (first 300 characters, whitespace collapsed).

`stage` is assigned by the first matching regular expression in
`PROMPT_RULES` in `collect.py`:

| Stage | What it marks |
|---|---|
| `framed_run_q1` | The shared frame: "Answer the following question … Quarto manuscript that renders to DOCX". |
| `card1_add_question` … `card9_same_task_twice` | Studio cards recognised from their wording (add question 2; the question the data cannot answer; codebook; one figure, rendered; five Zotero references; README read by a stranger; the same task twice). |
| `plan_only`, `plan_answers`, `plan_to_markdown` | Plan mode: "plan only", answers to the agent's planning questions, "write the plan as md". |
| `issues_from_plan`, `implement_issues` | "Turn the plan into four issues"; "implement issues one and two". |
| `todo_pass` | "Work through the TODOs in the manuscript". |
| `claude_md` | "Write a CLAUDE.md for this repo from what we did today". |
| `data_review`, `context_source`, `extension_analysis`, `steer_followup` | Free-form work: data checks, pointing the agent at a paper or source, more figures, maps, outputs, and one-line steering replies. |
| `other` | Four prompts that fit none of the above. |

### issues.csv, pulls.csv, releases.csv

Flattened API responses. `issues.csv` adds `n_checkboxes` (task-list
items in the body) and `kind` (`pre-work` for "Data added" and "Setup
complete", else `workshop`). `pulls.csv` adds `sprint` (created before
10:00 UTC on the day is sprint 1). `releases.csv` adds `has_declaration`,
`declaration_chars`, `tag_commit` and `tag_on`.

### milestones.csv

Eighteen milestones of the workshop day (M01 pre-work to M18 declaration)
with `status` (`yes`, `no`, `partial`, `not observable`) and the evidence
(issue numbers, prompt ids, commit shas, times). M12 (the run continued
from the phone) leaves no trace in git or GitHub and is `not observable`
everywhere. M15 (partner review as a GitHub review) is `no` everywhere
because no pull request carries a review or a comment; a review may still
have happened in person.

## Caveats

- Git records what was committed, not what was typed. Prompts that led to
  no commit (cards 2, 6, 7, 8 by design) are invisible unless the learner
  archived them anyway.
- Prompt timestamps are approximate. Commit times are reliable.
- `questions_answered` and the `outcome` text are the collector's reading
  of the manuscripts and release notes, not the learners'.
- The four repositories without workshop-day commits are kept in every
  file so the denominator stays thirteen.
