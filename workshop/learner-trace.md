# Learner trace: one learner through the combined day

Date of the dry run: 24 September 2026. Layout: `feat/day-combined` (deck
`workshop/slides.qmd`, run sheet `workshop/lesson-plan.md`, cards
`workshop/studio-cards.qmd`). One person, Claude Code 2.1.281, model
claude-fable-5-1, macOS, at the fork `agentsforsci-dev/fstp-eval-india`.

## In five lines

- One learner, one 180-page PDF, the whole day from `git switch -c dev` to the declaration in the v0.2.0 notes: every step on the deck ran, except the phone, the chat, the partner and the room.
- The agent worked 91 minutes of the run sheet's 172 contact minutes. Four runs did the real work and took 9 to 19 minutes each; the other 21 prompts took under 5.
- One block does not fit: plan mode. The frame alone ran 18.5 minutes in plan mode against a 15 minute countdown for frame, rejection, editable plan, edit and commit.
- Two lines are missing from the deck: leave plan mode before "write the plan as a markdown file" (it fails inside plan mode), and the literal prompt for the issues step.
- Two skill behaviours change the choreography: the open-pr skill ends with a question the slide does not answer, and a hand-edited file makes the commit skill hand the commit back to the learner.

## What stands in for what

| On the day | In this dry run |
|---|---|
| Learner's own repository at `~/Documents/gitrepos/gh-org-agentsforsci-ghe/<repo>` | Fork `agentsforsci-dev/fstp-eval-india`, cloned at `~/Documents/gitrepos/context-agentsforsci/gh-org-agentsforsci-dev/fstp-eval-india` (README plus one 180-page PDF, two commits) |
| Interactive Claude Code in a terminal, auto mode | Headless Claude Code (`claude -p --permission-mode auto`), one session id per `claude` start, `--resume` for each next prompt in the same session. Wall clock measured around each call. |
| `/ghe-skills:commit`, `/ghe-skills:open-pr` (plugin) | `/commit`, `/open-pr` from the same GHE skills repo, symlinked at user level. Same skill text. |
| The learner reads output, the diff, the proposed message, answers the skill's questions | Not timed. Headless runs cannot ask, so the skill took its own defaults. A reading allowance is added per step in the summary. |
| The learner's Claude Code has no CLAUDE.md and two skills | This account has a user-level CLAUDE.md (1.4k tokens: writing style, dev-branch rules, Quarto rule) and about 20 user skills (9.8k tokens). Both were loaded in every nested session. Where a rule visibly shaped the agent's behaviour the step says so. |
| Neighbour who sharpens question 1, review partner, phone, chat in the browser | Not available. Marked per step. The "partner" comments come from the same account. |
| Sticky notes, day sheet on paper, the recall sentence, the zine | Day sheet filled in below; the rest is room time, planned minutes only. |

## The three questions (question bank, 09:30)

Written for the CSE report in the repository, separate from the instructor's
questions on the slide.

1. Known answer, sharpened for column, unit and comparison: *Using the
   state-wise technology tables (Tables 1 to 8) in the report, how many FSTPs
   and how many co-treatment STPs were evaluated in each of the eight states,
   and what is the total installed FSTP capacity in KLD per state?* The
   executive summary says 69 plants, 47 FSTPs, about 1.6 MLD.
2. Unknown answer: *By how many log10 units does faecal coliform (MPN/100 ml)
   fall from inlet to outlet at each FSTP in Annexure II, and does the median
   log reduction differ between DEWATS-based plants and mechanised plants
   (MBBR, electrocoagulation, packaged modules)?*
3. The data cannot answer: *What is the monthly electricity consumption in
   kWh of each mechanised FSTP?* The report has one qualitative line on energy
   and no consumption figures.

Sprint 2 question (13:18, on paper): question 2.

## Kinds of learner action used in the tables

| Kind | Meaning | How it was measured |
|---|---|---|
| room | Movement, talk, listening, paper without a keyboard | Planned minutes from the run sheet only |
| paper | Writing on the question sheet or day sheet | Planned minutes only |
| type-cmd | The learner types a shell or slash command and waits | Wall clock of the command |
| prompt | The learner types a prompt, the agent works | Wall clock of the nested Claude Code call |
| skill | `/ghe-skills:commit` or `/ghe-skills:open-pr` | Wall clock of the nested call |
| read | The learner reads what the agent did or proposes | Estimated, stated per row |
| github | A click on github.com | Done here with `gh`; a click allowance is stated |

## Step table, morning

Planned minutes come from the run sheet's block tables and the slide
countdowns. Measured is wall clock of the agent or command. "Read" is the
allowance for the learner to read what came back, estimated. "Prompt?" marks
whether the step is already a prompt (P), a typed command that could become a
prompt (C to P), a GitHub click that could become a prompt (G to P), or has to
stay with the human (H). Section "Where Claude can be instructed" has the
wording.

### Opening, 09:00 to 09:40 (room and paper)

| Step (slide) | Where | What the learner does | Kind | Planned | Measured | Prompt? |
|---|---|---|---|---|---|---|
| Welcome, two room rules | room | listens | room | 3 | | H |
| Spectrum line | room | stands on the line, two voices | room | 8 | | H |
| Four questions | room | neighbour talk | room | 6 | | H |
| How the day works, the variable, recall | room | listens | room | 6 | | H |
| Objectives, schedule | room | listens | room | 5 | | H |
| Your question bank | paper | writes three questions, swaps, pins the sheet | paper | 10 | not timed; my three questions are above | H |
| The instructor's questions | room | listens | room | 2 | | H |

### Current state, safety rails, the commit rule, 09:40 to 10:15

| Step (slide) | Where | What the learner does | Kind | Planned | Measured | Prompt? |
|---|---|---|---|---|---|---|
| Rounds 0 and 1, neighbour minute | room | | room | 3 | | H |
| My turn: chat | room | watches the chat demo | room | 6 | | H |
| A good question | room | | room | 2 | | H |
| Rails 1: open `data/` in RStudio, look | RStudio | looks at one PDF | read | 8 (rails total) | about 30 s | H |
| Rails 2 and 3: terminal in the repo, `git switch -c dev`, `claude` | terminal | types two commands | type-cmd | | under 5 s each | C to P (the branch), H (`claude`) |
| Rails 4: `/status`, `/context` | terminal | types two slash commands, reads | type-cmd | | 4 s each; reading the context table about 60 s | H |
| Who commits, and how often | room | | room | 4 | | H |
| Two skills: `/plugin marketplace add`, `/plugin install`, `/exit`, `claude` | terminal | types four commands | type-cmd | 5 | not repeated (skills already installed); the install takes about 30 s when it works | H |
| Pair your phone: `/remote-control`, scan, "Status?" | terminal, phone | | type-cmd | 3 | not reproducible headless | H |
| Buffer, break slide | room | | room | 4 | | |

### Sprint 1, 10:35 to 12:00

| Step (slide) | Where | What the learner does | Kind | Planned | Measured | Prompt? |
|---|---|---|---|---|---|---|
| Opens with the break question, one last look at `data/` | room | | room | 2 | | H |
| Be the agent | Claude chat | pastes files by hand on the setup repository | prompt | 6 | not reproducible here | H |
| Model, harness, tool call | room | | room | 4 | | H |
| Framed run: "Answer the following question using the data in this repository and write up the result as a Quarto manuscript: *question 1*." | Claude Code | types the frame, watches, does not intervene | prompt | 12 (countdown for run and commit), 15 (block) | **12 min 7 s**, 44 turns, USD 5.88 | P |
| `/ghe-skills:commit`, read the message, log the run | Claude Code, paper | types the skill, answers the archive question, reads the message | skill | | **1 min 27 s**, 3 turns, plus about 60 s to answer and read | P (already a skill) |
| The studio: ten cards, the day sheet | room | listens | room | 2 | | H |
| Card 4: one figure, render to DOCX | Claude Code | types the card prompt with question 1 | prompt | 35 (studio) | 3 min 45 s, 7 turns, USD 1.50, rendered | P |
| `/ghe-skills:commit` | Claude Code | | skill | | 42 s | P |
| Card 3: the codebook | Claude Code | | prompt | | 1 min 15 s, 3 turns, USD 0.53 | P |
| `/ghe-skills:commit` | Claude Code | | skill | | 33 s | P |
| Card 2: the question the data cannot answer (question 3) | Claude Code | | prompt | | 1 min 28 s, 5 turns, USD 0.70, nothing to commit | P |
| Card 6: the README, read by a stranger | Claude Code | | prompt | | 54 s, 2 turns, USD 0.35, nothing to commit | P |
| Card 7: `/context`, then the question | Claude Code | | type-cmd, prompt | | 3 s and 37 s, nothing to commit | P |
| Card 5: five references from Zotero | Claude Code | | prompt | | 4 min 18 s, 23 turns, USD 1.72, nothing to commit | P |
| Cards 1, 8, 9, 10 | | not run: card 1 repeats the frame with question 2 (sprint 2 does it properly), 8 and 10 are free play, 9 needs a second session for the same card | | | | P |
| Stand up | room | | room | 1 | | H |
| Log each card on the day sheet | paper | | paper | | about 30 s per card, 3 min for six rows | H |
| The release path | room | | room | 1 | | H |
| Ship 1: "Push the dev branch." | Claude Code | | prompt | 4 (with the skill) | 39 s, 2 turns | P |
| Ship 1: `/ghe-skills:open-pr` | Claude Code | reads the draft (headless: no draft shown) | skill | | 1 min 16 s, 4 turns; ends by asking whether to run the test plan | P |
| Ship 2: open the PR, one minute on Files changed, merge | GitHub | reads 10 files, 544 additions, clicks merge | github | 3 | 4 s with `gh`; about 90 s of reading and two clicks | G to P (the merge), H (the reading) |
| Ship 3: "Switch to main and pull. Render the manuscript to DOCX." | Claude Code | | prompt | 4 | 39 s, 3 turns | P |
| Ship 4: "Tag v0.1.0 and create a GitHub release. Attach the DOCX if it rendered; if not, say in the release note that the manuscript does not render yet." | Claude Code | | prompt | 4 | 46 s, 2 turns; release up with the DOCX | P |
| Ship 5: "Switch to dev, merge main into it, and push." | Claude Code | | prompt | 2 | 14 s, 2 turns (no-op here, see the note) | P |
| Sticky note when the release page is up | GitHub | opens the release page | github | 1 | about 30 s | H |
| Recall v1, lunch slide | room, paper | | room | 3 | | H |

**Morning agent time.** Framed run and commit 13 min 34 s. Studio 13 min 35 s
for five cards and two commits. Ship 3 min 38 s. Total 30 min 47 s of the 85
minute sprint. The rest is reading, the day sheet, the room, and waiting.

**Morning cost line.** USD 13.7 API-equivalent for the sprint (the day sheet's
"cost line" column). The framed run alone was USD 5.88.

### Between sprints, 13:00 to 13:20 (room and paper)

| Step (slide) | Where | What the learner does | Kind | Planned | Measured | Prompt? |
|---|---|---|---|---|---|---|
| Stakes ladder | room | stands on a rung | room | 5 | | H |
| Reflect on v0.1.0 | room, paper | release page open, day sheet in hand | room | 5 | | H |
| Where repositories live, inside a repository, file names | room | listens | room | 8 | | H |
| Your sprint 2 question | paper | writes where the v0.1.0 files belong and picks question 2 | paper | 2 | | H |

**Reflect on v0.1.0, answered from the day sheet.**

- What did it assume without asking? Three transcription decisions (Puri as an
  STP, Patora's kilolitres per week, two Jhansi units), all named in the answer
  and the commit message. The manuscript project layout (`index.qmd` at the
  root, `_manuscript/` as output). The author name, taken from `git config`
  and the macOS account. In card 5, that it may read the Zotero database file
  when the Zotero tool returns nothing.
- Where did it put files, and how did it name them? Everything at the
  repository root: `index.qmd`, `_quarto.yml`, `references.bib`,
  `.gitignore`. Data beside the PDF in `data/` with underscores:
  `fstp_technology_tables.csv`, `fstp_technology_tables_codebook.csv`. No
  `raw_data`, `derived_data`, `metadata`, `analysis`. The rendered DOCX in an
  ignored `_manuscript/` folder.
- How many commits did sprint 1 produce? Three on dev, then the merge commit.
  Hands up for three or more: yes.
- Would I send v0.1.0 to a co-author? The numbers, yes: the answer is right and
  the one discrepancy with the report is flagged. The repository, no: the
  layout and the file names are the agent's, and the README does not say an
  agent wrote it.
- Where would the v0.1.0 files belong in the template? The PDF in
  `data/raw_data/`, the CSV in `data/derived_data/`, the codebook as
  `data/metadata/codebook.csv`, the manuscript in `analysis/`.

## Step table, afternoon

### Sprint 2: plan mode, issues, partner review, 13:20 to 14:10

| Step (slide) | Where | What the learner does | Kind | Planned | Measured | Prompt? |
|---|---|---|---|---|---|---|
| Round 3 slide, My turn: plan mode demo | room | watches | room | 8 | | H |
| Plan mode 1: Shift+Tab until plan mode | Claude Code | | type-cmd | 15 (whole step) | seconds | H |
| Plan mode 2: the sprint 1 frame with question 2 | Claude Code | types the frame, waits | prompt | | **18 min 29 s**, 9 turns (one subagent), USD 8.34; plan written to `~/.claude/plans/`, ended with two questions | P |
| Plan mode 3: reject with one sentence: "Not like this: the PDF stays in data/raw_data/, the extracted table goes to data/derived_data/, a codebook to data/metadata/codebook.csv, the manuscript to analysis/, and files are named lowercase with dashes and a two-digit prefix for scripts." | Claude Code | | prompt | | 2 min 39 s, 2 turns, USD 1.06; plan rewritten to the template | P |
| Plan mode 4a: "Write the plan as a markdown file I can edit before you do anything." | Claude Code | | prompt | | 2 min 54 s, 3 turns, USD 1.45; **blocked**: plan mode refused the write into the repository, file rewritten in `~/.claude/plans/` | P, but fails in plan mode |
| Plan mode 4b (not on the slide): Shift+Tab out of plan mode, same prompt again | Claude Code | | prompt | | 31 s, 2 turns; `plan-faecal-coliform-log-reduction.md` at the repository root | P |
| Plan mode 4c: edit one line | RStudio | changes decision 3 (rename the PDF) | read | | 1 s with sed; about 60 s by hand | H |
| Plan mode 4d: "Commit the plan." (`/ghe-skills:commit`) | Claude Code | | skill | | 1 min 25 s, 3 turns; **mixed path**: message written to `.git/CLAUDE_COMMIT_MSG`, learner asked to commit | P |
| Plan mode 4e (not on the slide): `! git commit -F .git/CLAUDE_COMMIT_MSG` | Claude Code | types the command | type-cmd | | 1 s; commit 284da9b with `Human-authored: true` and `Assisted-by:` | H by the skill's rule |
| Log it | paper | | paper | | 30 s | H |
| Pair talk, recall v2 | room | | room | 5 | | H |
| Round 4 slide | room | | room | 1 | | H |
| The issues: "Turn the approved plan into four issues on this repository, each with a title, what done looks like, and the files it touches: 1. ... 2. ... 3. ... 4. ..." (wording mine, the deck prints none) | Claude Code | | prompt | 10 | 2 min 2 s, 3 turns, USD 0.96; issues 2 to 5 | P |
| Fork only: enable issues in Settings | GitHub | two clicks | github | | 1 s with `gh` | G to P |
| Find your review partner: read and comment on the partner's issues | GitHub | reads four issues, writes four comments | github | 10 | 6 s to post; reading four issues of this length takes 8 to 10 minutes | H |

**Plan-mode step, agent time.** 26 min 0 s against the 15 minute countdown,
before the learner reads anything. See finding 1.

### Hand-over to the phone and the walk, 14:10 to 14:40

| Step (slide) | Where | What the learner does | Kind | Planned | Measured | Prompt? |
|---|---|---|---|---|---|---|
| "Implement issues 1 and 2 on the dev branch. Run /ghe-skills:commit after each issue, then push. Ask me when you are unsure." | Claude Code | types it, leaves | prompt | 8 plus 20 | **14 min 12 s**, 33 turns, USD 7.14; commits f1377b4 (layout) and 630ddf5 (log reduction manuscript), pushed | P |
| `/remote-control`, scan, "Status?" | Claude Code, phone | | type-cmd | | not reproducible | H |
| Walk, check progress every few minutes | phone | | room | 20 | the run finished with 14 minutes to spare | H |

### Sprint 2: review, CLAUDE.md, rerun, merge, 14:40 to 15:30

| Step (slide) | Where | What the learner does | Kind | Planned | Measured | Prompt? |
|---|---|---|---|---|---|---|
| What did it ask you? | room | one note for the wall: it asked nothing, decided four things alone | room | 3 | | H |
| Finish 1: read the diff | RStudio or GitHub | 13 files, 722 additions | read | 8 (with the two below) | about 2 to 3 min | H |
| Finish 2: "Push the dev branch." | Claude Code | | prompt | | 17 s, no-op (the hand-over prompt had pushed) | P |
| Finish 2: `/ghe-skills:open-pr` | Claude Code | | skill | | 45 s, 3 turns; PR 6 with a seven item test plan; the test plan question again | P |
| Partner review: open the partner's PR, read every line, approve or comment, do not merge | GitHub | | github | 8 | 1 s to post a comment; reading needs the full 8 min; own PR cannot be approved | H |
| Recall v3 | room | | room | 2 | | H |
| CLAUDE.md, CLAUDE.md against a skill, CSV against data package | room | | room | 5 | | H |
| Round 5 slide | room | | room | 1 | | H |
| Round 5.1: "Write a CLAUDE.md for this repository from what we did today: the folder template, the naming rules, where the codebook is, how to render the manuscript. Then fill data/metadata/codebook.csv for the derived table." | Claude Code | | prompt | 20 (whole round) | 1 min 10 s, 2 turns, USD 0.60 | P |
| Round 5.1: commit | Claude Code | | skill | | 29 s; commit c484327 | P |
| Round 5.2: `/exit`, `claude` | Claude Code | | type-cmd | | seconds | H |
| Round 5.3: rerun the sprint 1 frame with question 1, word for word | Claude Code | | prompt | | **9 min 27 s**, 28 turns, USD 4.84; verified the existing answer, added a numbered check script, updated README and CLAUDE.md, rendered, **committed by itself** | P |
| Round 5.3: commit | Claude Code | | skill | | 14 s; nothing left to commit | P |
| Round 5.3: "Push the dev branch." | Claude Code | | prompt | | 16 s; PR 6 now carries CLAUDE.md and the rerun | P |
| Round 5.4: pairs, sprint 1 output next to the rerun | room | | room | | see the comparison below | H |
| Partner merges | GitHub | one click | github | 2 | 2 s with `gh`; issues 2 and 3 closed by the Closes lines | H |
| Clarify | room | | room | 2 | | H |

**Round 5 agent time.** 11 min 36 s against the 20 minute block.

**Sprint 1 output next to the rerun.**

| | Sprint 1 (10:47, no CLAUDE.md) | Round 5 (15:14, CLAUDE.md in place) |
|---|---|---|
| Where files landed | repository root, `data/` with underscores | `analysis/` with a two digit prefix for the new script; nothing new at the root |
| What it produced | manuscript, CSV, bibliography, config, README edit | a check script against the PDF, setup checks in the manuscript, inline numbers, README and CLAUDE.md lines |
| Commit | waited for `/ghe-skills:commit` | committed on its own through the skill, because CLAUDE.md says so |
| Time and cost | 12 min 7 s, USD 5.88 | 9 min 27 s, USD 4.84 |
| Would I merge this? | the numbers | the whole commit |

### Sprint 2: ship v0.2.0, declare both, 15:30 to 16:00

| Step (slide) | Where | What the learner does | Kind | Planned | Measured | Prompt? |
|---|---|---|---|---|---|---|
| Ship 1: "Switch to main and pull. Render the manuscript to DOCX." | Claude Code | | prompt | 4 | 40 s, 4 turns; rendered `plants-per-state.docx`; dev fast-forwarded again by the user-level rule | P |
| Ship 2: "Tag v0.2.0 and create a GitHub release with the DOCX attached." | Claude Code | | prompt | 3 | 1 min 29 s, 6 turns; re-rendered the second manuscript too; two DOCX assets | P |
| Ship 3: "Switch to dev, merge main into it, and push." | Claude Code | | prompt | 2 | 14 s; no-op | P |
| Open the two release pages side by side | GitHub | | github | 1 | about 30 s | H |
| My turn: the declaration demo | room | | room | 5 | | H |
| Your declaration: "Write a declaration of AI use for this repository from the first commit to tag v0.2.0. Read the commit history and its trailers, the prompts folder, the issues, the pull requests and CLAUDE.md. Say which files an agent touched, in response to which instruction, who reviewed what, and what changed between v0.1.0 and v0.2.0. Put it in the release notes of v0.2.0." | Claude Code | | prompt | 8 | **3 min 34 s**, 12 turns, USD 1.72; appended to the v0.2.0 notes | P |
| Two volunteers read a line aloud, recall v4 | room | | room | 2 | | H |

**Ship v0.2.0 agent time.** 2 min 23 s against the 10 minute countdown.

**What the declaration found.** Twelve commits to v0.2.0: two without an
agent, two GitHub merges, eight with `Assisted-by:`, one of them mixed. Ten
prompt files for nine instructions (007 and 008 are the same prompt, archived
once per commit). Every file at v0.2.0 with who touched it; the PDF content
and `.DS_Store` never touched by the agent. Who reviewed what: PR 1 nobody,
issues 2 to 5 and PR 6 one stand-in comment each, and the two things flagged
on PR 6 not fixed before the merge. Two gaps the record cannot close: no
prompt is archived for the release notes, the PR bodies or the issue texts,
because those changed nothing in git and the commit skill archives only at
commit time. The declaration ends by quoting the instruction that produced it.

### Disclosure rules in the making, 16:00 to 16:30 (room and paper)

| Step (slide) | Where | What the learner does | Kind | Planned | Measured | Prompt? |
|---|---|---|---|---|---|---|
| Two sides of the room | room | | room | 6 | | H |
| The 18 tasks, two colours | paper | ticks what the agent touched in each sprint | paper | 8 | see the list below | H |
| Three flipcharts | room | | room | 8 | | H |
| What happens next | room | | room | 2 | | H |

**What the agent touched, from the trace.** Sprint 1: data extraction and
cleaning, data analysis, figures, the manuscript text, the bibliography file,
the README, the commit messages, the PR text, the release note. Sprint 2: the
plan, the issues text, the repository structure, an extraction script, a
second manuscript with statistics, the codebook, CLAUDE.md, a check script,
the PR text, the release note, the declaration itself. Not touched by the
agent: the three questions, the rejection sentence, one line of the plan, the
review comments, every merge, the sticky notes.

### Close: the zine, 16:30 to 17:00 (room and paper)

| Step (slide) | Where | What the learner does | Kind | Planned | Measured | Prompt? |
|---|---|---|---|---|---|---|
| What you learned today | room | | room | 2 | | H |
| Fold a zine | paper | | paper | 3 | | H |
| Eight pages | paper | | paper | 15 | | H |
| The table, survey | paper | | paper | 8 | | H |
| Final recall, thanks, `/plugin uninstall ghe-skills@ghe-skills` | room, terminal | | room | 2 | not run | H |

## Time by kind

Measured wall clock of the nested Claude Code calls and the commands, summed
over the day. Reading, paper and room time are not in these numbers.

| Kind | Steps | Measured | Note |
|---|---|---|---|
| prompt | 25 | 84.6 min | every learner prompt to the agent, including the three ship prompts each time |
| skill | 8 | 6.8 min | six `/ghe-skills:commit`, two `/ghe-skills:open-pr` |
| type-cmd | 5 | 0.2 min | `git switch -c dev`, `/context` twice, the mixed-path commit, a new session |
| github | 6 | 0.3 min | two merges, one issues switch, five comments; the clicks themselves |
| read | 2 | estimated | the diff, the plan edit |
| **agent total (prompt plus skill)** | 33 | **91.5 min** | |

Against the run sheet's "contact time with Claude" table (172 minutes, 35 of
them free): the agent was working for 91 of those minutes. The other 80 are
the learner reading, deciding, logging and waiting, which is the right ratio
for "read everything it does".

### Agent time by block, planned against measured

| Block | Planned for the agent steps | Measured agent time | Fits? |
|---|---|---|---|
| 10:47 framed run and commit | 12 (countdown), 15 (block) | 13.6 | tight; no reading time left inside the countdown |
| 11:02 studio, five cards and two commits | 35 | 13.6 | yes, with 20 min for reading and the sheet |
| 11:40 ship v0.1.0 | 18 (countdown), 20 (block) | 3.6 | yes, generous |
| 13:28 plan mode, edited plan, commit | 15 | 26.0 | **no**: the frame alone took 18.5 |
| 13:48 issues | 10 | 2.0 | yes |
| 13:58 partner review of issues | 10 | 0.1 to post | reading four long issues fills the block |
| 14:10 hand-over and walk | 8 plus 20 | 14.2 | yes |
| 14:43 finish, push, open PR | 8 | 1.0 | yes, the diff reading is the block |
| 14:51 partner review of the PR | 8 | 0.0 to post | reading 13 files fills the block |
| 15:06 round 5 | 20 | 11.6 | yes |
| 15:30 ship v0.2.0 | 10 | 2.4 | yes |
| 15:45 declaration | 8 (countdown), 10 (block) | 3.6 | yes |

### The agent runs, longest first

| Run | Minutes | Turns | Cost line |
|---|---|---|---|
| Plan mode, the frame with question 2 | 18.5 | 9 | USD 8.34 |
| Hand-over, implement issues 1 and 2 | 14.2 | 33 | USD 7.14 |
| Framed run, question 1 | 12.1 | 44 | USD 5.88 |
| Round 5 rerun, question 1 | 9.4 | 28 | USD 4.84 |
| Card 5, Zotero | 4.3 | 23 | USD 1.72 |
| Card 4, figure and render | 3.8 | 7 | USD 1.50 |
| Declaration | 3.6 | 12 | USD 1.72 |
| The other 18 prompts | 0.2 to 2.9 each | 1 to 6 | USD 0.2 to 1.5 |

The run sheet says "agent runs take 3 to 10 minutes each". On a 180-page PDF
the four runs that do real work took 9 to 19 minutes; everything else was
under 5.

**Estimates for the three ways to commit, from this run.**

| Way | Time | What the learner does |
|---|---|---|
| Tell Claude to commit in words ("Commit this.") | about 30 to 40 s (one git status, one commit; the ship prompts of that size took 14 to 46 s) | reads the message afterwards |
| `/ghe-skills:commit` | 29 to 87 s measured, plus about 60 s to answer the archive question and read the draft | answers one question, reads the draft, sees the trailers and the prompt archive appear |
| By hand in RStudio (stage, message, commit) | about 2 to 3 min for a message of the skill's length; 30 s for a one-liner | writes the message; no trailers, no archive |
| Mixed path after a hand edit | the skill's time plus one typed command | runs `! git commit -F .git/CLAUDE_COMMIT_MSG` |

## Where Claude can be instructed

Every place the deck has the learner type a git or gh command, click on
github.com, or edit a file by hand, with a prompt that would do the same, and
whether the prompt was tried in this run.

| Slide step | As printed | As a prompt | Tried? | Verdict |
|---|---|---|---|---|
| Rails 3 | `git switch -c dev` (or `git switch dev`) | "Switch to the dev branch. Create it from main if it does not exist." | Not in this run (the rails were followed as printed). The same wording worked at 11:40 for main and dev. | Keep the typed command here. It is the one moment the learner drives git themselves before the agent does, and the deck's "already have one?" fork is exactly the case a prompt handles better. Either is fine; the typed line teaches the branch, the prompt teaches delegation. |
| Rails 3 | `claude` | none | | H. The agent cannot start itself. |
| Rails 4 | `/status`, `/context` | none | | H. Built-in slash commands, not prompts. `/context` works in a headless session too. |
| Two skills | `/plugin marketplace add ...`, `/plugin install ...` | none | | H. Plugin management is a user command; the agent cannot install its own skills. |
| Pair your phone | `/remote-control` | none | | H. |
| Framed run | prompt | already a prompt | yes | P |
| Cards 1 to 6, 8, 10 | prompts | already prompts | yes (2, 3, 4, 5, 6) | P |
| Card 7 | `/context`, then a prompt | | yes | H then P |
| Card 9 | `/exit`, `claude` | none | | H. A new session is a user action. |
| Ship 1 | "Push the dev branch." | already a prompt | yes, 39 s | P. Could be folded into the skill, but the run sheet wants pushing as its own step. |
| Ship 1 | `/ghe-skills:open-pr` | skill | yes, 76 s | P. The skill ends with "Should I run through the Test plan now?", which the deck leaves unanswered. Add "Answer no" to the slide, or add a line to the skill for sprint 1. |
| Ship 2 | open the PR on GitHub, one minute on Files changed, merge yourself | "Merge pull request 1 into main." (the agent runs `gh pr merge`) | Not as a prompt; merged with `gh pr merge --merge` in 4 s. | G to P is possible, but the deck is right to keep the click: the point of sprint 1 is that the learner reads the diff and merges without a reviewer. The reading cannot be delegated. In sprint 2 the partner merges, so the click stays there too. |
| Ship 3 to 5 | three prompts | already prompts | yes | P. "Switch to main and pull. Render the manuscript to DOCX." did four things in 39 s. |
| Sticky note | open the release page | "Open the release page for v0.1.0 in the browser." (the agent runs `gh release view --web`) | not tried | G to P, harmless. |
| Plan mode 1 | Shift+Tab until plan mode | none | | H. Permission mode is a user setting. Headless: `--permission-mode plan`. |
| Plan mode 3 | one rejection sentence | already a prompt | yes, 159 s | P |
| Plan mode 4 | "Write the plan as a markdown file I can edit before you do anything." | already a prompt, but it does not work in plan mode | yes, 174 s blocked, then 31 s out of plan mode | P with one more line on the slide: leave plan mode first (Shift+Tab), then ask. Or: "Copy the plan into the repository as plan.md" after leaving plan mode. |
| Plan mode 4 | edit one line | by hand in RStudio | done by hand | H on purpose: the hand edit is what makes it the learner's plan and what triggers the skill's mixed path. |
| Plan mode 4 | "Commit the plan." | `/ghe-skills:commit` | yes, 85 s, then the learner runs `! git commit -F .git/CLAUDE_COMMIT_MSG` | P, but the slide should say that a hand-edited file makes the skill hand the commit back to the learner. Two actions, not one. |
| Issues | "Ask the agent to turn the approved plan into three or four issues ..." | the deck gives no literal prompt; used: "Turn the approved plan into four issues on this repository, each with a title, what done looks like, and the files it touches: 1. ... 2. ... 3. ... 4. ..." | yes, 122 s | P. Put the literal prompt on the slide as every other Your turn has one. |
| Issues, fork only | enable issues in Settings | "Enable issues on this repository." (the agent runs `gh repo edit --enable-issues`) | done with `gh` in 1 s | G to P. Only matters for forks; learners' own repositories have issues on. |
| Partner review | comment on the partner's issues on GitHub | none | by hand | H by design. A colleague without agent access shapes the work. |
| Hand-over | "Implement issues 1 and 2 on the dev branch. Run /ghe-skills:commit after each issue, then push. Ask me when you are unsure." | already a prompt | yes | P |
| Hand-over | `/remote-control`, scan, "Status?" | none | not reproducible | H |
| Finish | read the diff | `git diff` in RStudio or on GitHub, or "Show me what changed since the plan commit, file by file." | | H by rule one (read everything it does); a prompt can summarise, the learner still reads. |
| Finish | "Push the dev branch.", `/ghe-skills:open-pr` | already prompts | yes | P |
| Partner review of the PR | approve on GitHub | none | own PR cannot be approved; a comment was left | H by design. |
| Round 5 | CLAUDE.md prompt, commit | already a prompt and the skill | yes | P |
| Round 5 | `/exit`, `claude` | none | | H |
| Round 5 | rerun the frame, commit, "Push the dev branch." | already prompts | yes | P |
| Partner merges | merge on GitHub | "Merge my partner's pull request." would work from the partner's own session | merged with `gh pr merge` | G to P, but the click is the partner's act of review; keep it. |
| Ship v0.2.0 | three prompts | already prompts | yes | P |
| Declaration | prompt | already a prompt | yes | P |
| Thanks | `/plugin uninstall ghe-skills@ghe-skills` | none | not run | H |

**Pattern.** The deck already puts every git action after the rails into a
prompt. What stays typed is either a slash command (status, context, plugin,
remote-control, exit), a permission mode, or a GitHub click that carries a
human judgement (merge, approve, comment). The only typed git command left is
`git switch -c dev` in the rails, and that is defensible. Two places need a
prompt the deck does not print: the issues step (no literal prompt) and the
plan file step (the printed prompt fails inside plan mode).

## The day sheet, filled in

| Run | What happened (one line) | What it assumed | Cost line | Would I merge this? | Committed? |
|---|---|---|---|---|---|
| First run | 12 min. Transcribed Tables 1 to 8 into a CSV, wrote a Quarto manuscript with three charts, rendered DOCX, found the 1.6 MLD claim does not add up. | Manuscript project at the root; author from the machine; Puri is an STP; kilolitres per week to per day. | USD 5.88, 44 turns | The numbers yes, the layout no. | Yes, after the skill (1.5 min). |
| Card 4 | 3.7 min. One two-panel figure added, DOCX rendered. | Kept the three older charts. | USD 1.50 | Yes. | Yes (42 s). |
| Card 3 | 1.3 min. Codebook CSV with ten rows beside the data. | Its own file name, no metadata folder. | USD 0.53 | Yes. | Yes (33 s). |
| Card 2 | 1.5 min. "Cannot be answered from this repository", with the search terms and the nearest data. | Nothing. | USD 0.70 | Not applicable. | Nothing to commit. |
| Card 6 | 54 s. Ten README gaps, two of them about the agent's own record (prompts folder, AI use invisible). | Nothing. | USD 0.35 | Not applicable. | Nothing to commit. |
| Card 7 | 22 percent of the context used; named 150 unread pages. | Nothing. | USD 0.33 | Not applicable. | Nothing to commit. |
| Card 5 | 4.3 min. Zotero tool empty, so it copied the Zotero database and queried it. Five real references. | That reading the database file was fine. | USD 1.72 | The references yes, the method needs a rule. | Nothing to commit. |
| Plan | 26 min of agent time. First plan in plan mode after a provisional analysis; one sentence moved every file into the template; the editable file only landed in the repository after leaving plan mode. | That it should run the analysis to plan it; a separate manuscript folder; that the sprint 1 files move too. | USD 11.2 over four prompts | The rewritten plan yes. | Yes, by hand after the skill's mixed path (1.5 min plus one command). |
| Issues | 2 min. Four issues with context, done checkboxes and files, dependency links. | That "done" can be ten checkboxes long; my name in issue 4. | USD 0.96 | Yes, after the partner trims them. | Not applicable. |
| Issue 1 and 2 (from the phone) | 14 min. Layout moved with git mv, PDF renamed; script, derived table, codebook rows, DOCX manuscript with one figure; two commits, pushed. Asked nothing. | Dropped the plan's second chart; archived the prompt twice; Closes lines. | USD 7.14 | Yes, after two fixes from the review. | Yes, twice, by the agent. |
| CLAUDE.md | 70 s. Template, naming, codebook, render, manuscript and git sections; noted the codebook needed nothing. | That the user-level CLAUDE.md "applies on top"; a machine-specific Quarto path. | USD 0.60 | Yes, minus the machine path. | Yes (29 s). |
| Rerun | 9.4 min in a new session. Found the answer already there, verified 73 rows against the PDF, added a numbered check script, followed CLAUDE.md, committed on its own. | That verifying was the task; that it may commit. | USD 4.84 | Yes. | Yes, by the agent, before I asked. |
| Declaration | 3.6 min. Twelve commits, eight assisted, nine instructions, every file with who touched it, who reviewed what, what changed between the releases, and what the record cannot show. | Nothing; it names the gaps. | USD 1.72 | Yes, as it stands. | On the release, not in git. |

## Findings for the deck and the run sheet

Ordered by how much they change the day.

1. **Plan mode does not fit in 15 minutes on a real dataset.** The frame in
   plan mode ran 18 min 29 s and cost about USD 8 before a plan appeared,
   because the agent did the analysis provisionally (R, a Wilcoxon test) and
   read Quarto's source to settle a project layout question. The whole step
   (frame, reject, markdown plan, edit, commit) measured 26 minutes of agent
   time. Options: add "Do not run any analysis yet, plan only" to the frame
   for sprint 2 and test whether that halves it; or give the step 25 minutes
   and take them from the issues block by shipping the issues prompt with the
   plan prompt; or run the plan-mode frame before the stakes ladder so it works
   while the room is on the floor (13:00 to 13:20), the way the walk covers
   the hand-over. Slide "Your turn: plan mode", run sheet 13:28.
2. **"Write the plan as a markdown file I can edit" fails inside plan mode.**
   Claude Code writes plans to `~/.claude/plans/<slug>.md` and refuses to
   write in the repository while plan mode is on. The learner has to Shift+Tab
   out and ask again (31 s), or ask for a copy. Add that line to step 4 of the
   slide and to the demo script. Run sheet 13:28, step 4.
3. **"Commit the plan" is two actions after a hand edit.** The commit skill's
   mixed path (a file the learner edited) stops before committing, writes
   `.git/CLAUDE_COMMIT_MSG`, and asks the learner to run
   `! git commit -F .git/CLAUDE_COMMIT_MSG`. The slide says "Commit the plan"
   as if it were one line. Say so on the slide, or have the demo show it. Note
   also that the skill ticked a decision in the plan file on its own while
   committing (decision 8, "commit the plan file"), which a learner would not
   see.
4. **The framed run alone used the 12 minute countdown.** 12 min 7 s for the
   run, then 1.5 min for the skill and about a minute of reading. The 15
   minute block holds it with nothing to spare. The run sheet's "agent runs
   take 3 to 10 minutes" is optimistic for a first run on a 180-page PDF:
   the agent transcribed 73 rows and rendered twice. A smaller data file
   (a CSV) would come in under 5 minutes; the deck could say that the first
   run on a PDF is the slow case.
5. **The open-pr skill ends with a question the deck does not answer.** "Should
   I run through the Test plan now?" In sprint 1 the slide sends the learner
   to GitHub, so the question hangs in the terminal. Add "answer no" to the
   slide (sprint 1 is rough on purpose) or make the skill skip the test plan
   when asked to.
6. **The issues step has no literal prompt.** Every other Your turn prints
   the words to type. Suggested: "Turn the approved plan into four issues on
   this repository, each with a title, what done looks like, and the files it
   touches: 1. Organise the repository following the template. 2. The
   analysis inside the Quarto manuscript with format: docx, one figure from a
   code chunk. 3. Five references from my Zotero library. 4. A methods
   paragraph." Measured 2 min 2 s.
7. **The issues are too long for a 10 minute partner review.** Issue 3 had
   ten checkboxes naming plants and page numbers. A partner reading four such
   issues needs the whole block just to read. Either ask for "at most five
   checkboxes each" in the prompt, or make the partner review one issue, the
   one that will be implemented first.
8. **Card 5 is a safety-rails moment, not a Zotero moment.** With the Zotero
   local API off (pre-work step 7 turns it on; here it was off), the MCP
   returned nothing, and the agent copied `zotero.sqlite` to /tmp and queried
   it with SQL without asking. The card's "watch for" should include "did it
   go around the tool, and did it ask first". The pre-work check (step 9,
   `claude mcp list`) does not catch a running Zotero with the API off; add
   one Zotero query to the setup check.
9. **Ship v0.1.0 is generous.** 3 min 38 s of agent time for five prompts in
   an 18 minute countdown. The time is reading the PR and the release page,
   which is right, but the block could give 5 minutes back to the studio or
   the plan step.
10. **Fork-only gotcha, not for learners.** Issues are off on a fork by
    default; learners' own repositories have them on. The demo repository
    for rainbow-train is not a fork, so no change needed.
11. **What the agent decided alone that the room should hear at 14:40.** The
    author name from the machine account; reading the Zotero database file;
    moving the sprint 1 files during the restructure; whether to keep the
    three older charts.
12. **Round 5 changes who commits, without anyone deciding it.** With
    CLAUDE.md saying every change ends with the commit skill, the rerun
    committed on its own before the learner typed `/ghe-skills:commit`. The
    learner's commit found nothing to do. That is rung 3 of the ladder
    ("let the agent commit") reached by documentation alone, which is the
    round 5 lesson; the slide could name it.
13. **The rerun is a verification, not a repeat.** The second run of the same
    frame found the answer already in the repository and spent its 9.5
    minutes checking the transcription against the PDF and adding a check
    script. The pair comparison on the slide ("did it follow the template
    without being told?") holds, and there is a second comparison worth
    asking: what does the agent do when the work is already done?
14. **The declaration names what the record cannot show.** Issue texts, PR
    bodies and release notes change nothing in git, so the commit skill never
    archives the prompts behind them. The declaration flagged this itself.
    If the day wants a complete record, the open-pr skill (and whatever
    creates issues and releases) would have to archive prompts too, or the
    declaration slide should say what the record covers.
15. **"Push the dev branch." is redundant twice.** After the hand-over
    prompt (which ends with "then push") and after the rerun (where CLAUDE.md
    made the agent commit but not push). Harmless; the second one still does
    work. Keep it.
16. **The user-level CLAUDE.md on this machine changed three steps.** The
    ship's "switch to main and pull, render" also synced dev (a rule in that
    file), so "switch to dev, merge main into it, and push" was a no-op both
    times; the project CLAUDE.md the agent wrote says the user-level rules
    "apply on top"; and the Quarto chunk rule was quoted back in card 4. A
    learner's session has none of this. Rehearse on a machine with no user
    CLAUDE.md, or under a separate `CLAUDE_CONFIG_DIR`.
17. **Cost line for the day.** About USD 55 of API-equivalent usage for one
    learner (framed run 5.9, studio 5.1, ship 1.8, plan step 11.2, issues
    1.0, hand-over 7.1, finish 1.2, round 5 6.0, ship 0.8, declaration 1.7,
    plus session overhead). On a Team plan this is quota, not invoice, but
    fifteen learners doing the same day is a number the organiser should
    know before the day.

## Repository record

All on `agentsforsci-dev/fstp-eval-india`.

- Commits on `main` after the day: 12 (2 before the day, 8 agent-assisted, 2 merges). `dev` equals `main`.
- Pull request 1, "Add Quarto manuscript on FSTPs and STPs per state", self-merged, no review: https://github.com/agentsforsci-dev/fstp-eval-india/pull/1
- Release v0.1.0, one DOCX: https://github.com/agentsforsci-dev/fstp-eval-india/releases/tag/v0.1.0
- Issues 2 to 5, one stand-in comment each; 2 and 3 closed by the merge: https://github.com/agentsforsci-dev/fstp-eval-india/issues
- Pull request 6, "Restructure repository and add faecal coliform log reduction manuscript", one stand-in review comment, merged as "the partner": https://github.com/agentsforsci-dev/fstp-eval-india/pull/6
- Release v0.2.0, two DOCX, declaration in the notes: https://github.com/agentsforsci-dev/fstp-eval-india/releases/tag/v0.2.0
- `prompts/`: ten files, nine distinct instructions. `CLAUDE.md` at the root. `plan-faecal-coliform-log-reduction.md` at the root, with the hand edit.
- Left as the day left it: `.DS_Store` still tracked, issues 4 and 5 open, the plan's target tree still naming the old PDF.

## Where the raw material is

The per-call transcripts (stream-json), prompts and elapsed times of every
nested run, and the timing CSV, were kept in the session's scratchpad and are
not committed. The numbers in this file come from that CSV.
