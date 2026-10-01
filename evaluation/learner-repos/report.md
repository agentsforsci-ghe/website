# What the learner repositories show after the workshop day

Agents for Scientists, Global Health Engineering, ETH Zurich. Workshop
day: 29 September 2026. Records read: 1 October 2026. The structured data
behind every number is in `repos.csv`, `commits.csv`, `prompts.csv`,
`issues.csv`, `pulls.csv`, `releases.csv` and `milestones.csv` next to
this file; `README.md` is the codebook.

## 1. Summary

Thirteen repositories were in scope. Nine of them ran the full day. The
other four (bcmeter-example, beaver-ss, biogas-malawi,
cybersecurity-ownership) never left the pre-work state of two to four
commits and show no activity on the day.

The nine active repositories did what the run sheet asked, at the time
the run sheet asked for it. All nine merged a sprint 1 pull request and
tagged v0.1.0 between 11:56 and 12:02 local time. All nine tagged v0.2.0
between 15:45 and 15:49, with a "Declaration of AI use" in the release
notes. Every one of them has a three-questions file, at least one Quarto
manuscript rendered to DOCX, a plan document, GitHub issues written from
the plan, a prompt archive and a CLAUDE.md.

Three things did not happen in the records. No pull request on any
repository carries a GitHub review or a comment, so the partner review
left no trace. The last step of sprint 2 ran out of time for more than
half the cohort: CLAUDE.md reached `main` in four repositories, sits on
`dev` in four, and in one is reachable only from the v0.2.0 tag. And
nothing about the phone hand-over is visible in git.

## 2. What was collected

For each repository the collector reads the `main` branch commit by
commit (date, author, subject, trailers, files and lines changed), the
`prompts/` archive file by file (timestamp, model, files touched, the
prompt text), the tags and the `dev` branch, and the GitHub REST API for
issues, pull requests, releases and reviews. Each prompt is classified
into a stage of the day by its wording (the shared frame, a studio card,
plan mode, issues, the TODO pass, CLAUDE.md, or free-form work). Each
repository is then scored against eighteen milestones of the run sheet,
with the evidence recorded next to the score.

The reading of what each manuscript answers, and the two-sentence outcome
per repository, are the only hand-written parts.

## 3. The cohort at a glance

| Repository | Domain, toolchain | Commits on the day | Prompts archived | Issues | CLAUDE.md on |
|---|---|---|---|---|---|
| caves-currents | Palaeoclimate; R, Quarto, HTML app | 18 | 17 | 4 | main |
| ghg-bsfl | Insect-rearing emissions; R package with CI | 14 | 11 | 4 | tag only |
| implementation-mzuzu | Qualitative interviews; R, Quarto, 20 rater agents | 11 | 10 | 6 | dev |
| myco-sanitation | Fungal waste treatment; R, Quarto | 14 | 11 | 2 | main |
| sensor-validation | Biogas sensor lab data; R, Quarto, Python | 11 | 11 | 4 | dev |
| tdabc-mzuzu | Pit-emptying task timing; R, Quarto | 13 | 17 | 5 | dev |
| urine-durban | Field experiment on urine collection; R, Quarto | 19 | 5 | 4 | main |
| washschools-nigeria | School WASH survey tables; Python, Quarto | 24 | 19 | 4 | main |
| water-quality-col | Drinking water index; R, Quarto, leaflet | 16 | 10 | 4 | dev |

Eight of nine work in R with Quarto; washschools-nigeria works in Python
with Quarto. Every active repository renders to DOCX, and three also
ship HTML (urine-durban, water-quality-col, the caves-currents explorer).
Data ranges from one small CSV or workbook to the 254 MB lab dump of
sensor-validation, which committed 313 files including logs and PNGs.

Across the nine, `main` holds 166 commits, 140 of them on the day. Of the
114 non-merge commits on the day, 86 carry the commit skill's
`Assisted-by: Claude <model>` trailer, 6 carry the older
`Co-Authored-By: Claude` line, and 22 have no AI trailer. The 22
human-only commits are almost all the same three things: the
three-questions file, the "added todos" commit of the afternoon review,
and file moves. The agent wrote the analysis; the humans wrote the
questions and the review comments. That is also what the declarations
say.

The commit skill shaped the history. 87 of the 166 commits follow
Conventional Commits (42 `docs`, 30 `feat`, 7 `fix`), nearly all of them
the assisted ones. 73 of the 86 assisted commits cite at least one
archived prompt; 13 cite none.

## 4. The day, read from the timestamps

The records line up with the schedule to within minutes.

| Block on the run sheet | Planned | In the records |
|---|---|---|
| Question bank | 09:00 to 09:45 | "add my three questions" commits 10:20 to 10:27 |
| Sprint 1 framed run | from 10:35 | first archived prompts 10:50 to 11:02; first manuscript commits 10:58 to 11:11 |
| Ship v0.1.0 | by 12:00 | 9 pull requests merged 11:53 to 12:00; 9 releases 11:56 to 12:02 |
| Plan mode and issues | 13:20 to 14:10 | "plan only" prompts after lunch; 37 issues created 13:43 to 14:18 |
| Phone and walk | 14:10 to 14:40 | implementation commits continue 14:17 onward |
| Review, CLAUDE.md, merge | 14:40 to 15:36 | "added todos" commits 14:41 to 14:49; sprint 2 merges 14:36 to 15:51 |
| Ship v0.2.0 | 15:36 to 16:06 | 9 releases 15:45 to 15:49 |

The question-bank commits land 35 minutes after the block ended, which is
expected: the file was written on paper first and committed once the
terminal was open. The rest is on time. The nine v0.1.0 tags fall within
six minutes of each other and the nine v0.2.0 tags within four. The room
moved as one.

Commits split 60 before lunch and 80 after. Per repository the day ranges
from 11 to 24 commits, with a median of 14.

## 5. Sprint 1: the frame, the cards, the first release

Every learner typed the same frame. Eleven archived prompts start with
"Answer the following question using the data in this repository and
write up the result as a Quarto manuscript that renders to DOCX", with
small variations in spelling. In eight repositories the first run was on
Claude Opus 5.5; water-quality-col ran it on Fable 5.1. After the first
run six of the nine switched to Fable 5.1 and stayed there.
caves-currents used Fable for the middle of the day and went back to Opus
for the afternoon; washschools-nigeria stayed on Opus all day. Over the whole day the
archive records 72 prompts on Fable and 39 on Opus. One learner used the
switch deliberately: myco-sanitation's second prompt is "create the same
input again using fable", which is card 9 with the model as the variable.

The studio cards are visible in the prompt archive of eight repositories.
Card 5 (five Zotero references) is the most used, in five repositories.
Card 1 (add question 2 to the manuscript) appears in four, card 4 (one
figure, rendered) in three, card 3 (the codebook) in two, cards 2, 6 and 9
in one each. Cards 7, 8 and 10 leave nothing to commit and are therefore
invisible. urine-durban shows no card wording; that learner asked for an
HTML output and two scatter plots instead, which is card 4 in spirit.

Card 2 worked as designed where it ran: ghg-bsfl asked "how much ecoli
was present in chamber 1" and the agent answered that the workbook holds
no microbial data, which is now recorded in the README.

The first release went up for all nine. Eight attached one or two DOCX
files; washschools-nigeria attached nothing to either release.

## 6. Sprint 2: plan, issues, review, CLAUDE.md, declaration

Plan mode is in the archive of eight repositories as a "plan only" or
"do not run any analysis or write any file yet" prompt, twelve such
prompts in total. All nine have a plan file in the tree
(`plans/`, `PLAN.md`, `plan-q2-co2e.md` and similar). Nine repositories
hold 37 workshop issues, created between 13:43 and 14:18 local time; 32 of
them have the task-list checkboxes the slide asked for, and 31 are closed.
Most learners made exactly four issues; implementation-mzuzu made six and
myco-sanitation two.

The second question was handled "properly" in the sense of the day, but
the scope grew well past one question in several rooms. ghg-bsfl turned
the repository into an R package with GitHub Actions CI.
implementation-mzuzu ran twenty rater agents on four models over the
interview transcripts, measured agreement, and had the author adjudicate
29 contested scores in a votes file. caves-currents reran its analysis
with a 1,000-member age-model ensemble and built an interactive discharge
explorer. washschools-nigeria extracted a report annex into 21 tidy CSVs
with a data package and codebook and drew 20 exploratory figures.
water-quality-col added a leaflet map. tdabc-mzuzu wrote a data review,
a cleaning script and a cleaned dataset before re-answering both
questions. sensor-validation wrote a generated codebook for 313 raw
files. These are the afternoons where the "plan, issues, implement" loop
ran two or three times rather than once.

The review step took the form the slide offered as the fallback. Eight of
nine repositories show the TODO pass: a human-only commit such as "added
todos", "TODOs added" or "Add TODOS for Claude to work on" between 14:41
and 14:49, followed by a prompt of the form "work through the TODOs in
the manuscript, remove each when done, then run the commit skill". The
partner review as a GitHub review did not happen anywhere: 23 pull
requests, 0 reviews, 0 review comments, 0 conversation comments. The
pull requests were merged quickly, with a median of three minutes between
opening and merging and 21 of 23 under ten minutes. The two exceptions
are tdabc-mzuzu's second PR (56 minutes) and sensor-validation's (27
minutes).

Every learner wrote a CLAUDE.md from the day's work, and here the clock
ran out. Four reached `main` (caves-currents, myco-sanitation,
urine-durban, washschools-nigeria). Four are on `dev` only
(implementation-mzuzu, sensor-validation, tdabc-mzuzu,
water-quality-col), together with other unmerged afternoon work such as
a triangulation plan and a codebook. In ghg-bsfl the CLAUDE.md commit is
on neither branch; only the v0.2.0 tag points at it. Two v0.2.0 tags
therefore sit on commits that are not on `main`: sensor-validation's on
`dev`, ghg-bsfl's on a stray commit.

All nine v0.2.0 release notes contain a section titled "Declaration of AI
use". Seven of them are long, between 6,000 and 11,000 characters, with a
per-commit table of instruction, model and files touched, and a list of
what no agent touched. Two are five bullet points of about 360
characters (myco-sanitation, urine-durban). Both forms are honest; they
are not comparable.

## 7. Where the records are thin

- **The partner review.** Nothing in GitHub. If the review happened on
  paper or over a shoulder, the deck's "review comments" step needs a
  place where it lands, or the TODO pass should be named as the review.
- **The prompt archive.** Coverage is uneven: urine-durban archived 5
  prompts for 13 assisted commits, and 13 assisted commits across the
  cohort cite no prompt. Several prompt timestamps are `00:00:00`. The
  skill's archive is only as complete as the moments the learner
  accepted it.
- **The phone.** No commit, prompt or issue says it came from the phone.
  Milestone M12 is unobservable for all nine.
- **Reading time.** A three-minute median from opening a pull request to
  merging it leaves little room for "read everything the agent does" on
  diffs that run from hundreds to thousands of lines.
- **The question the data cannot answer.** Question 3 stayed open in
  eight repositories, by design. sensor-validation answered all three.

## 8. Outcomes per repository

- **caves-currents.** Two manuscripts: the Glas age range, and the
  meltwater-source analysis with age uncertainty, kernel correlation and
  surrogate tests. Plus the discharge explorer. Open: question 3 has no
  data in the repository.
- **ghg-bsfl.** Questions 1 and 2 answered with a literature comparison;
  the repository is now an R data package with CI. Open: E. coli data do
  not exist; two documentation issues; the tag points at an unmerged
  commit; a Word lock file is tracked.
- **implementation-mzuzu.** City and formalisation indicators answered;
  question 2 re-scored by twenty raters and adjudicated by the author.
  Open: question 3 cannot be answered from interviews; CLAUDE.md and a
  plan are on `dev`.
- **myco-sanitation.** Raw vs sterile degradation answered twice (once
  per model) and improved with literature; F40 vs AmBm answered with
  mixed models, a dry-mass balance and a plateau outlook. Open: faecal
  indicator bacteria.
- **sensor-validation.** All three questions answered in one manuscript,
  then independently in a second report; a generated codebook for the
  whole data folder. Open: the v0.2.0 tag is on `dev`; two TODO comments
  remain.
- **tdabc-mzuzu.** Total job time and travel time answered on cleaned
  data, with the review and cleaning documented, and a combined final
  manuscript. Open: worker-experience question; field verification of
  flagged rows; CLAUDE.md on `dev`.
- **urine-durban.** Areas and urine production answered, then the
  dataset was reconciled with the published papers and the residual
  differences diagnosed. Open: groundwater question; two discrepancies
  need the original Stata files.
- **washschools-nigeria.** Country and toilet access answered; annex
  tables tidied into a data package; question 3 started with exposure
  counts and literature parameters. Open: the scenario model and
  manuscript; no release assets.
- **water-quality-col.** Observational unit and completeness answered,
  with a municipal map and an HTML version with sortable table and
  interactive map. Open: coverage question; CLAUDE.md and codebook on
  `dev`.

## 9. What this suggests for the next iteration

1. **Move CLAUDE.md before the sprint 2 pull request**, or add an explicit
   "merge main into dev, open the last PR, merge, then tag" line. Five of
   nine releases miss the file on `main`, and two tags point off `main`.
2. **Decide what the review is.** Either give the GitHub review a literal
   click path and five minutes of its own, or teach the TODO pass as the
   review and drop the GitHub review from the deck. The TODO pass worked
   in eight of nine rooms.
3. **Give the declaration a shape.** A target length and the three
   headings (tools and models, what the agent touched per instruction,
   what no agent touched) would make the nine declarations comparable.
   Seven learners produced that shape on their own; two did not.
4. **Make the prompt archive the default, not a question.** Thirteen
   assisted commits have no prompt, and one repository stopped archiving
   after the first sprint.
5. **Expect scope to grow after lunch.** Several learners ran the
   plan-issues-implement loop more than once and built features (CI, a
   rater workflow, an interactive map). The run sheet can name this as the
   intended outcome of a good plan rather than as drift.
6. **Catch data hygiene at the pre-work check**: a 254 MB data folder with
   logs and PNGs, a committed Word lock file, and interview transcripts in
   a private repository are all things a one-line check on the setup page
   would catch.
7. **Four of thirteen repositories never started.** Whether those people
   were absent or stuck is not in the records; the chat log or the sign-in
   sheet would say.

## 10. Caveats

Git and GitHub record what was committed, not what was said or read. The
stage of each prompt is assigned by its wording and will be wrong at the
margins. The reading of what each manuscript answers is the collector's,
not the learner's. Local times are the committers' clocks. Timestamps in
prompt files are estimates; commit times are not.
