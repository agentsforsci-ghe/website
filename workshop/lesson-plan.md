# agentsforsci-ghe lesson plan (run of show), combined layout

Tuesday 29 September 2026, 08:30-17:00, Villa Hatt, ETH Zurich. Built from the
deck (`workshop/slides.qmd`), the studio cards (`workshop/studio-cards.qmd`)
and the schedule CSV. Per-block times get updated after the rehearsal (same
file, new commit, no amend). How this layout was chosen from the three before
it is in `workshop/layout-review.md`.

The shape of this layout: **the whole path twice, with a studio inside the
first run.** Sprint 1, before lunch, is fast and wide: three questions, one
framed run everyone does the same way, then studio cards on your own
repository with a commit after each, a pull request you merge yourself, and
release v0.1.0, rough on purpose. Sprint 2, after lunch, runs the path
properly on one question: an editable plan, issues a colleague reviews before
any code exists, a run that continues from the phone, a pull request your
partner reviews, a CLAUDE.md, release v0.2.0, and one declaration over both
records. The day closes with a zine.

The focus of this plan is the **My turn** blocks: exactly what I do at the
keyboard while the room watches. My-turn slides say only "sit back and watch";
the steps below are the demo script, not shown on screen. Every demo runs on
`agentsforsci-ghe/fstp-eval-india`, the repository of the rainbow-train demo
account. Expect to adapt to what the agent shows live.

## Operating rules

- My turn = instructor drives, room watches and notes questions. Your turn =
  participants drive, sticky note when done. Our turn = whole room does the same
  small step together.
- The sticky note means one thing all day: done. Stuck means a raised hand.
- Location icons on every Your-turn slide: terminal = Claude Code; laptop-code =
  RStudio; GitHub mark = github.com in the browser; comments = the Claude chat in
  the browser; pen = paper; mobile-screen = the Claude app on the phone.
- Two room rules, said in minute three and repeated at every "would I merge
  this?": never make another human read AI slop, read everything it does; and
  **commit often**, a pull request only at the end of a larger chunk of work.
  The commit skill is installed before the first agent run. Every Your turn
  with the agent that changes a file ends with `/ghe-skills:commit`. Two pull
  requests in the day, one at the end of each sprint.
- Three questions per person: one you know the answer to (question 1,
  sharpened by a neighbour), one you do not (question 2), one the data cannot
  answer (question 3). The framed run at 10:47 uses question 1 for everyone.
  The cards use 2 and 3. Sprint 2 is a choice: question 1 done properly, or
  question 2.
- Every round ends with the same self-check: would I merge this?
- Reflect right after the activity; the block after a break opens with the
  question that went into the break.
- Bounded regroup after each Your turn: 3 min, then park-and-pair, 1:1 fix at the
  next break. Never let one stuck participant stop the room.
- Conservative timing: 2 min per content slide, 1 min per section or transition
  slide, 3 min of questions in any block with five or more slides, a buffer line
  in every block. Countdowns on the slides equal the minutes in this plan.
- Protected blocks: sprint 1 ship (11:40, may spill into lunch), the partner
  review of issues (13:58), the walk with the agent (14:20), round 5 (15:06,
  twenty minutes, not less), sprint 2 ship (15:30), disclosure (16:00), the
  zine (16:30). If behind, cut in this order: the buffers; be the agent (6 to
  4); the studio (35 to 25, never less, "at least two cards" becomes "at least
  one"); two sides of the room (6 to 5); the 18-task checklist (8 to 5); the
  declaration demo (5 to 0, two volunteers read theirs instead).
- Git facts that bite: the pre-work never creates a `dev` branch, so the rails
  say `git switch -c dev` (and `git switch dev` for anyone who has one). The
  open-pr skill never pushes, so every step that opens a pull request is
  preceded by a push, and the hand-over prompt ends with "then push".
- A rough v0.1.0 is the point. If the manuscript does not render before lunch,
  the release goes out without the DOCX and the release note says so. Lunch is
  the repair window; sprint 2 tries again. Do not let anyone polish v0.1.0.
- The sticky note for a release fires when the release page is up, with or
  without the DOCX.
- Every example path follows the folder convention from July:
  `~/Documents/gitrepos/gh-org-agentsforsci-ghe/<repo>` for repositories in this
  organisation, `~/Documents/gitrepos/gh-rainbow-train/<repo>` for a personal
  account. `gh-org-*` and `gh-*` sit next to each other inside `gitrepos`.
- The day runs in auto mode. Shift+Tab switches to manual mode at any time; say
  so once in the safety rails block and leave it at that.

## How the recall slide works

The recall slide is one sentence with six blanks. It describes the whole
workflow: *You write a question. The agent reads your repository. The agent
proposes a plan. You reject it with one sentence. A colleague reviews the
issues and the pull request. The instructions live in the repository.* It
appears five times, spaced through the day: at the sprint 1 ship (blanks one
and two, 11:56), after the pair talk on plan mode (blanks three and four,
13:46), after the partner review (blank five, 14:59), after the declaration
(blank six, 15:55), and at the close, read aloud together.

The routine, every time, 90 seconds:

1. The slide appears with the newest blanks still empty. Say nothing.
2. Countdown 20 seconds: tell your neighbour what goes into them.
3. Reveal (next slide, the blanks filled). Two voices from the room if the
   guesses differed.
4. Everyone writes the full sentence so far on the back of the day sheet.

Why: retrieval practice. Filling the blank from memory, before seeing it, is
what makes the sentence stick; reading it would not. By 17:00 everyone can say
the workflow without the slide, and the final version goes on the last page of
the zine in their own words. If a version gets skipped for time, skip the
guessing, not the writing.

## Contact time with Claude

Minutes a participant spends at the keyboard or on the phone with the agent.
Free means the participant chooses what to ask.

| Block | Activity | Where | Min | Free |
|---|---|---|---|---|
| 10:37 | Be the agent, on the setup repository | Claude chat | 6 | |
| 10:47 | The framed run, then commit | Claude Code | 12 | |
| 11:02 | Studio cards, a commit after each that changed a file | Claude Code | 35 | 35 |
| 11:40 | Ship v0.1.0 | Claude Code | 18 | |
| 13:28 | Plan mode on one question, then issues | Claude Code | 25 | question is theirs |
| 14:10 | Hand-over to the phone | Claude Code, phone | 8 | |
| 14:20 | Walk with your agent | Phone | 20 | |
| 14:43 | Finish, push, open the pull request | Claude Code | 8 | |
| 15:06 | Round 5: CLAUDE.md, new session, rerun, pairs | Claude Code | 20 | |
| 15:30 | Ship v0.2.0 | Claude Code | 10 | |
| 15:45 | Your declaration over both releases | Claude Code | 10 | |
| | **Total** | | **172** | **35** |

For comparison: the first layout had 118 minutes (none free), the studio
layout 155 (45 free), the sprints layout 148 (25 free). Agent runs take 3 to
10 minutes each. The studio, the plan-mode block and round 5 are sized so a
slow run does not eat the block; the sprint 1 ship may spill into lunch.

## Materials

- Yellow sticky notes on every seat (done-signal), a second colour for the
  evidence wall.
- Dot stickers and the poster for the arrival line ("never used AI for research"
  to "use an agent every week").
- Masking tape for the spectrum line and the stakes ladder on the floor.
- Printed studio cards, one set per table, and one day sheet per person, ten
  rows (both on `workshop/studio-cards.qmd`; print the page). Paper and pens
  for the question sheets.
- Printed bingo cards (one per person) and printed 18-task taxonomy checklists
  (one per person), plus two pen colours per person for the 16:00 block.
- For the zine: A3 paper, one sheet per person plus spares; scissors, one pair
  per two people; coloured pens; stickers; a speaker for music; three flipcharts
  and markers (also used for the 16:00 block); tape.
- Snacks for 10:15 and 14:20. The helper lays them out during the chat demo
  (09:48) and during the partner review of issues (14:00), never during an Our
  turn script. Coffee and water all day.
- Power strips for the laptops that stay inside at 14:20.

## Breaks and the questions that go into them

| Break | Time | Question on the slide | Opens the next block as |
|---|---|---|---|
| Snack 1 | 10:15-10:35 | What in your data folder would you not want a model to read? | One last look at `data/` before the first run |
| Lunch | 12:00-13:00 | Of the 18 tasks in writing a paper, which did the agent touch in sprint 1, and which would you never hand over? | Reflect with the release page open |
| Snack 2 | 14:20-14:40 | Walk with your agent: what does it ask you, and what does it decide alone? | Evidence wall notes |

Breaks outdoors where weather allows. The helper takes the list of parked
participants into every break: failed installs and pairings at 10:15, failed
renders and releases at 12:00.

---

## Arrival (08:30-09:00, 30 min)

- Room: projector, wall space for the evidence wall and the question sheets,
  three flipcharts, sticky notes on every seat, tape lines laid before people
  arrive, cards and day sheets on the tables face down.
- Setup clinic as people arrive: `claude --version`, `/status`, `claude mcp list`.
  Anyone without a working install moves to claude.ai/code. The helper does this,
  not me.
- Phone check at the door: Claude app installed, signed in with the workshop
  account, same organisation as the laptop. The pairing itself is tested at
  10:08.
- Dot sticker on the arrival poster on the way in. First entry on the evidence
  wall.

---

## Opening: security, literacy, transparency, disclosure (09:00-09:40, 40 min)

Slides: Welcome -> Two room rules -> Spectrum line -> Four questions -> How
the day works -> The variable -> How the recall works -> Learning objectives ->
Schedule -> Your turn (question bank) -> The instructor's questions.

| Min | What |
|---|---|
| 3 | Welcome and the two room rules |
| 8 | Spectrum line |
| 6 | Four questions, two neighbour minutes |
| 4 | How the day works, the variable table |
| 2 | How the recall works |
| 3 | Objectives |
| 2 | Schedule |
| 10 | Your turn: question bank |
| 2 | Buffer |

### Welcome and the two rules (3 min)

- Link back to July: same workflow, one new participant in it.
- Opening claim, said once: subject matter expertise now matters more than
  programming skill.
- Rule one: never make another human read AI slop. Read everything it does.
- Rule two: commit often. A commit is a checkpoint you can return to and a line
  in the record. A pull request is for the end of a larger chunk of work. Today:
  a commit after every run that changed a file, one pull request per sprint.

### Spectrum line (8 min)

- Tape line along the room. Stand by agent experience (never, to weekly). Two
  voices from each end.
- Re-sort by "how much do I trust the output". Two voices again. Sit down.

### Four questions (6 min)

- One slide, four questions: what must never go in; how do I know this is
  right; could I recreate it if the AI were gone; what do I say, and to whom.
- Two neighbour minutes (countdown 2): pick the question that worries you most
  and say why. The background pages carry the arguments; the slide carries the
  questions.

### How the day works, the variable, the recall (6 min)

- The same path twice, a studio inside the first run. The variable table with
  its six rows: who reads the files, who decides the steps, who reviews, where
  the instructions live. Sprint 1 is rows 2 and 1, sprint 2 is rows 3 to 5.
- The recall routine, shown once on its own slide (see above). Run it for real
  at 11:56.

### Objectives and schedule (5 min)

- Objectives (four, keyword-led). Schedule: point at the two ships, the two
  snack breaks, the walk, the zine.

### Your turn: question bank (10 min, countdown 8)

- On paper, three questions your data can answer: (1) one you already know the
  answer to, (2) one you do not, (3) one the data cannot answer. One sentence
  each.
- Swap with a neighbour, who makes question 1 20 percent more specific: which
  column, which unit, which comparison.
- Pin the sheet on the wall.
- Then the instructor's questions on the slide: which of the 47 FSTPs meet the
  CPCB discharge standard of 30 mg/L BOD, and how does BOD removal compare across
  treatment technologies (question 1); helminth egg counts in the treated
  effluent (question 3, the one the report cannot answer).

---

## Current state, safety rails, the commit rule (09:40-10:15, 35 min)

Slides labelled "current state" for rounds 0 and 1, then the rails.

Slides: Round 0 (variable) -> The steps of a paper -> Round 1 (variable) -> My
turn (chat) -> A good question -> Our turn (safety rails) -> Who commits? ->
Our turn (two skills) -> Our turn (pair your phone once) -> Snack break.

| Min | What |
|---|---|
| 3 | Rounds 0 and 1 slides, neighbour minute |
| 6 | My turn: chat |
| 2 | A good question |
| 8 | Our turn: safety rails |
| 4 | Who commits, and how often |
| 5 | Our turn: install the two skills |
| 3 | Our turn: pair your phone once |
| 4 | Buffer, break slide |

The helper lays out the snacks during the chat demo.

### Rounds 0 and 1 (3 min)

- The steps of a paper as you do them now and where the hours go, one slide.
- Neighbour minute (countdown 1): where does AI sit in your workflow today, if
  anywhere?

### My turn: round 1, chat (6 min) [DEMO SCRIPT]

Browser, claude.ai chat, the report PDF from
`~/Documents/gitrepos/gh-org-agentsforsci-ghe/fstp-eval-india/data/`.

1. Upload the report, ask question 1. Show the answer and ask for receipts:
   which page, which table. (3)
2. Question 3: "What are the helminth egg counts in the treated effluent per
   plant?" The report's tables carry pH, TS, TDS, TSS, COD, BOD, TKN, ammoniacal
   nitrogen, total phosphate and faecal coliform, not helminth eggs. Confirmed
   in rehearsal: [note what the model did]. (2)
3. Name it: the answer sounds the same whether it is right or not. That is why
   question 3 is on your sheet, and why card 2 exists. (1)

### A good question (2 min)

- One slide, one sourced line: being 20 percent more specific improves the
  result by 80 percent (Wickham and Bryan, Modern R Workflow, posit::conf 2026).
  Point back at the neighbour edit of question 1.
- The first layout had a placeholder here for a Terence Tao quote on terse,
  precise questions. No sourced line was found, so it is gone; the Wickham line
  makes the same point with a source.

### Our turn: safety rails (8 min)

- Together, step by step: open `data/` in your own repository and look once
  more against the group rule; terminal at
  `~/Documents/gitrepos/gh-org-agentsforsci-ghe/<your repo>`, not one level up
  (the agent reads the folder it starts in); `git switch -c dev` (anyone who
  already has a `dev` branch: `git switch dev`); `claude`; `/status`; find the
  mode line (auto mode, Shift+Tab for manual); `/context`.
- Hand out the bingo cards. They run until 16:00.

### Who commits, and how often (4 min)

- The ladder with the issue step: do all commits yourself; tell the agent when
  to commit; let the agent commit, you write the issues and open the PR; let the
  agent make the whole PR. Sprint 1 climbs to rung 2, sprint 2 to rung 3.
- Commit often: after every run that changed a file. Small commits are cheap to
  read and cheap to undo. One pull request per sprint, when the chunk is done.
  Pushing is a separate step and the pull request skill will not do it for you.

### Our turn: two skills (5 min)

- In Claude Code: `/plugin marketplace add Global-Health-Engineering/skills`,
  then `/plugin install ghe-skills@ghe-skills`, then `/exit` and `claude` again.
  Sticky note when `/ghe-skills:commit` shows in the command list. A failed
  install goes to the helper in the break.

### Our turn: pair your phone once (3 min)

- `/remote-control`. Scan the QR code with the Claude app. Send "Status?" from
  the phone, read the answer on the laptop. Close the session on the phone.
  Sticky note when the answer arrived. Anyone whose pairing fails goes to the
  helper in the break; the fallback for 14:10 is set now, not then. Remote
  Control has to be enabled in the Team admin settings before the day; it is
  off by default.
- Break slide with question 1, restart 10:35.

---

## Snack break 1 (10:15-10:35, 20 min)

Question 1 on the screen. Helper fixes failed installs and pairings from a
known list.

---

## Sprint 1: the loop by hand, first run, studio, ship v0.1.0 (10:35-12:00, 85 min)

Slides: Question 1 opener -> Your turn (be the agent) -> Model -> Harness ->
Tool call -> Round 2 (variable) -> Your turn (the framed run, then commit) ->
The studio (the cards) -> The day sheet -> Your turn (explore) -> Stand up ->
The release path -> Our turn (ship v0.1.0) -> Recall v1 (guess, reveal) ->
Lunch.

| Min | What |
|---|---|
| 2 | Opens with question 1, one last look at `data/` |
| 6 | Your turn: be the agent, on the setup repository |
| 4 | Model, harness, tool call |
| 15 | Your turn: the framed run, then commit |
| 35 | Your turn: the studio, stand-up at minute 15 |
| 20 | Our turn: ship v0.1.0 (protected, may spill into lunch) |
| 2 | Recall v1 |
| 1 | Buffer, lunch slide |

### Your turn: be the agent (6 min, countdown 5)

- In the chat, not in Claude Code, and on the public data of the setup
  repository from the pre-work, not your own: "I have a repository with data.
  Ask me for the files you need to answer this question, one at a time, and I
  will paste what you ask for: what is in this data?" Paste by hand. Feel the
  loop.

### Model, harness, tool call (4 min)

- Three slides: model (stateless, on the provider's servers), harness (the loop,
  the tools, the permission layer, on your laptop), tool call (what will scroll
  past in a minute). Point at what they just did by hand.

### Your turn: the framed run, then commit (15 min, countdown 12)

- Everyone types the same frame with question 1 in it, nothing else: "Answer the
  following question using the data in this repository and write up the result
  as a Quarto manuscript: <your question 1>."
- Watch the tool calls. Do not intervene. When it stops: `/ghe-skills:commit`.
  Read the message it proposes. Log the run on the day sheet. Sticky note when
  the commit is in.

### Your turn: the studio (35 min, countdown 35) [PROTECTED, FLOOR 25]

- Ten cards on the table. Each card: a prompt frame, one line on what to watch
  for, and the same last line: if it changed a file, commit; either way, log
  it. Pick freely. At least two cards. Card 4 (one figure, rendered) is
  recommended for everyone: it is the render test for the ship at 11:40.
- The day sheet: ten rows, one per run, with what happened, what it assumed,
  cost line, would I merge this, committed. The sheet is the material for the
  13:00 reflect, the 16:00 checklist and page 2 of the zine.
- Rules inside the studio: if it asks, answer; stuck for two minutes, raise a
  hand and take another card. Cards 6 and 7 for the stuck (nothing can break),
  cards 8, 9 and 10 for the fast.
- At minute 15: everyone stands up, reads one other screen for one minute, sits
  down. There is no gallery walk; this is it.
- Instructor and helper circulate. Fix nothing longer than two minutes; park
  and move on. Anyone whose card 4 did not render is on the helper's lunch
  list.

### Our turn: ship v0.1.0 (20 min, countdown 18) [PROTECTED, SCRIPT]

Step by step, everyone at the same time. The release path slide first (1):
pull request merged into main, manuscript rendered, tag, release with the
artifact, dev synced. Sprint 1 does it rough.

1. "Push the dev branch." Then `/ghe-skills:open-pr`. The first pull request
   of the day: the chunk is done. (4)
2. On GitHub: open it, one minute on Files changed, merge it yourself. No
   reviewer, on purpose; sprint 2 has one. (3)
3. "Switch to main and pull. Render the manuscript to DOCX." If it fails, say
   so in the next step and move on. (4)
4. "Tag v0.1.0 and create a GitHub release. Attach the DOCX if it rendered; if
   not, say in the release note that the manuscript does not render yet." (4)
5. "Switch to dev, merge main into it, and push." Never leave a release on main
   with dev behind it. (2)
6. Sticky note when the release page is up, with or without the DOCX. (1)

If the room is still shipping at 12:00, lunch starts when the release pages
are up. Whoever is not up by 12:05 goes on the helper's lunch list and eats
first.

### Recall v1 and lunch (2 min)

- Recall routine for real: blanks one and two empty, 20 seconds, reveal "a
  question" and "your repository". Write it on the back of the day sheet.
- Lunch slide with the lunch question, countdown 60.

---

## Lunch (12:00-13:00, 60 min)

Lunch question on the screen. Helper works the list: failed renders first,
then releases that did not happen.

---

## Between sprints: what v0.1.0 shows (13:00-13:20, 20 min)

Slides: Stakes ladder -> Reflect on v0.1.0 -> Where repositories live -> Inside
a repository -> Your sprint 2 question.

| Min | What |
|---|---|
| 5 | Stakes ladder on the floor (opens with the lunch question) |
| 5 | Reflect with the release page open |
| 8 | Folders and files, three levels |
| 2 | One minute on paper: files, and the sprint 2 question |

### Stakes ladder (5 min)

- Opens with the lunch question: two answers, then everybody up. Four rungs
  taped on the floor: implement it; plan, then implement; plan, review the
  plan, implement, review the implementation; design first, then repeat the
  cycles. Sprint 1 was rung 1. Stand on the rung for the question you will take
  through sprint 2, then for "a figure in your thesis", then for "a throwaway
  plot". Sit down.

### Reflect on v0.1.0 (5 min)

- Release page open on every screen, day sheet in hand. What did it assume
  without asking? Where did it put files and how did it name them? How many
  commits did sprint 1 produce (hands up: three or more)? Would I send v0.1.0
  to a co-author?

### Folder and file organisation, three levels (8 min)

- Level 1, where repositories live: `gitrepos/` with `gh-org-agentsforsci-ghe/`,
  `gh-org-gitforsci-ghe/` and `gh-rainbow-train/` side by side, never in a
  cloud-synced folder. The agent starts inside the repository, never one level
  up.
- Level 2, inside a repository: the template as a tree (`data/raw_data/`,
  `data/derived_data/`, `data/metadata/codebook.csv`, `analysis/`,
  `docs/reports/`, `src/`). [Confirm the template before the day.]
- Level 3, file names: lowercase, dash as separator, short, two-digit prefix for
  scripts (`01-read-data.R`).

### One minute on paper (2 min)

- Where would your v0.1.0 files belong? And: sprint 2 runs question 1 done
  properly, or question 2. Write it down now.

---

## Sprint 2: plan mode, issues, partner review (13:20-14:10, 50 min)

Slides: Round 3 (variable) -> My turn (plan mode) -> Your turn (plan mode) ->
Pair talk -> Recall v2 (guess, reveal) -> Round 4 (variable) -> Your turn (the
issues) -> Find your review partner.

| Min | What |
|---|---|
| 8 | My turn: plan mode |
| 15 | Your turn: plan mode, commit the plan |
| 3 | Pair talk |
| 2 | Recall v2 |
| 10 | Your turn: the issues |
| 10 | Partner review of issues (protected) |
| 2 | Buffer |

The helper lays out the afternoon snacks during the partner review.

### My turn: round 3, plan mode (8 min) [DEMO SCRIPT]

Terminal at `~/Documents/gitrepos/gh-org-agentsforsci-ghe/fstp-eval-india`,
branch `dev`, after its own rough v0.1.0.

1. Shift+Tab until the status line says plan mode. The sprint 1 frame with
   question 1. (1)
2. The first plan proposes extracting Table 9 (pages 34 to 35) to a CSV somewhere.
   Read it out. (2)
3. Reject with one sentence: "Not like this: the PDF stays in `data/raw_data/`,
   the extracted table goes to `data/derived_data/`, a codebook to
   `data/metadata/`, and files are named by our rules." (1)
4. Ask for a markdown plan I can edit: "Write the plan as a markdown file I can
   edit before you do anything." Open it, change one line, show that this is the
   editable plan. Do not implement. (3)
5. Commit the plan file: `/ghe-skills:commit`. A plan is worth a commit. (1)

### Your turn: plan mode (15 min, countdown 15)

- Plan mode. The sprint 1 frame with your sprint 2 question. Reject the first
  plan on purpose, with one sentence that points at the template and the naming
  conventions. Ask for a markdown plan you can edit. Edit one line. Do not
  implement. Commit the plan. Log it.

### Pair talk and recall v2 (5 min, countdown 3)

- What did one sentence change? Would I merge this plan?
- Recall routine, blanks three and four: the agent proposes a plan, you reject
  it with one sentence.

### Your turn: the issues (10 min, countdown 10)

- Ask the agent to turn the approved plan into three or four issues on your
  repository: (1) organise the repository following the template; (2) the
  analysis inside the Quarto manuscript with `format: docx` and one figure
  produced by a code chunk; (3) five references from your Zotero library; (4) a
  methods paragraph. Each issue: a title, what done looks like, the files it
  touches. Sticky note when the issues are on GitHub.

### Find your review partner, review the issues (10 min, countdown 10) [PROTECTED]

- Move to sit with your partner (neighbour pairs, triple if odd). Review each
  other's issues on GitHub before any code exists. Comment where a step is
  unclear or done is not defined.

---

## Hand-over to the phone (14:10-14:20, 10 min)

Slides: Our turn (hand-over) -> Snack break 2 (walk with your agent).

### Our turn: hand-over to the phone (8 min) [SCRIPT]

Step by step, everyone at the same time. The pairing was tested at 10:08.

1. In the session: "Implement issues 1 and 2 on the dev branch. Run
   /ghe-skills:commit after each issue, then push. Ask me when you are unsure."
   (2)
2. Type `/remote-control`. A link and a QR code appear. (1)
3. Scan the QR code with the Claude app, or open Code in the app: the session
   shows a computer icon with a green dot. (2)
4. Send one message from the phone: "Status?" The answer appears on both
   screens. (1)
5. Laptop plugged in, lid open, terminal open. (1)
6. Break slide with question 3. Snack in hand, go outside. (1)

Fallback for a failed pairing: leave the laptop running, go outside anyway, read
the transcript on return. Same-account check: `/status` on the laptop, the
account and organisation in the app.

---

## Snack break 2: walk with your agent (14:20-14:40, 20 min) [PROTECTED]

Question 3 on the screen. Check progress from the phone every few minutes,
answer what it asks, do not start new tasks. The helper stays inside with the
laptops.

---

## Sprint 2: review, CLAUDE.md, rerun, merge (14:40-15:30, 50 min)

Slides: Question 3 opener -> Your turn (finish, push, open the pull request)
-> Partner review (approve, do not merge yet) -> Recall v3 (guess, reveal) ->
CLAUDE.md -> CLAUDE.md against a skill -> CSV against data package (one slide)
-> Round 5 (variable) -> Your turn (round 5) -> Partner merges -> Clarify.

| Min | What |
|---|---|
| 3 | Opens with question 3, evidence wall |
| 8 | Your turn: finish, push, open the pull request |
| 8 | Partner review: approve, do not merge yet |
| 2 | Recall v3 |
| 5 | CLAUDE.md, CLAUDE.md against a skill, CSV against data package |
| 20 | Your turn: round 5 (protected) |
| 2 | Partner merges |
| 2 | Buffer, clarify |

### What did it ask you? (3 min)

- Opens with question 3: what did it ask you, what did it decide alone. Notes on
  the evidence wall.

### Your turn: finish, push, open the pull request (8 min, countdown 8)

- Back at the laptop: read the diff. If the agent is not done, it finishes now.
  Commits are in (the skill ran after each issue). "Push the dev branch." Then
  `/ghe-skills:open-pr`. The second and last pull request of the day.

### Partner review: approve, do not merge yet (8 min, countdown 8)

- Partner reviews the pull request on GitHub, every line: would I merge this?
  Approve, or say what would have to change. Do not merge yet: round 5 adds the
  CLAUDE.md to the same pull request, so the tag carries it. Compare with the
  sprint 1 pull request nobody reviewed.

### Recall v3 (2 min)

- Routine, blank five: a colleague reviews the issues and the pull request.

### CLAUDE.md, a skill, and the data package slide (5 min)

- CLAUDE.md in the project folder: versioned, shared with collaborators, in the
  record. It holds what is true for this project: the template, the naming
  rules, where the codebook is, how to render. One line: a user level file
  exists on your machine, applies to every project, and never appears in the
  repository.
- CLAUDE.md against a skill: the "when" is always sent, the "what" loads on
  demand. Told it three times, put it in CLAUDE.md. Lots of text for one
  purpose, make it a skill. Never write skills prospectively.
- CSV against data package, one slide from the rehearsal: the same short
  prompt on a plain CSV and on the installed openwashdata package, two
  screenshots, one line. Documentation you wrote for a colleague is
  documentation the agent needs too. No live demo: it was the first cut in
  every layout, so it never happened. [Take the two screenshots in rehearsal.]

### Your turn: round 5 (20 min, countdown 20) [PROTECTED]

- "Write a CLAUDE.md for this repository from what we did today: the folder
  template, the naming rules, where the codebook is, how to render the
  manuscript. Then fill data/metadata/codebook.csv for the derived table."
  Commit. (8)
- New session (`/exit`, `claude`). Rerun the sprint 1 frame with question 1,
  word for word. Commit. "Push the dev branch." (8)
- Pairs: the sprint 1 output next to this one. Did it follow the template
  without being told? Would I merge this? Bingo closes. (4)

### Partner merges (2 min)

- The pull request now carries the issues, the CLAUDE.md and the rerun. The
  partner merges it. Sticky note when it is merged.

---

## Sprint 2: ship v0.2.0, declare both (15:30-16:00, 30 min) [PROTECTED]

Slides: Our turn (ship v0.2.0) -> My turn (declaration) -> Your turn (your
declaration) -> Recall v4 (guess, reveal).

| Min | What |
|---|---|
| 10 | Our turn: ship v0.2.0 |
| 5 | My turn: the declaration |
| 10 | Your turn: your declaration over both releases |
| 2 | Recall v4 |
| 3 | Buffer |

### Our turn: ship v0.2.0 (10 min, countdown 10) [SCRIPT]

1. "Switch to main and pull. Render the manuscript to DOCX." If it failed at
   lunch and again now, the release note says so, as in the morning. (4)
2. "Tag v0.2.0 and create a GitHub release with the DOCX attached." (3)
3. "Switch to dev, merge main into it, and push." (2)
4. Open the two release pages side by side. Sticky note when both are up. (1)

### My turn: the declaration (5 min) [DEMO SCRIPT]

1. "Write a declaration of AI use for this repository from the first commit to
   tag v0.2.0. Read the commit history and its trailers, the prompts folder, the
   issues, the pull requests and CLAUDE.md. Say which files an agent touched, in
   response to which instruction, who reviewed what, and what changed between
   v0.1.0 and v0.2.0. Put it in the release notes of v0.2.0." (4)
2. Open the release notes. Count the commits it found: that is the commit rule
   paying off. (1)
3. If behind: skip the demo, two volunteers read a line of theirs at the end of
   the next step.

### Your turn: your declaration (10 min, countdown 8)

- Same prompt on your repository. Put the declaration into the notes of v0.2.0.
  Log it. Two volunteers read one line aloud.
- Recall v4: routine, blank six, "the repository".

---

## Disclosure rules in the making: two records (16:00-16:30, 30 min) [PROTECTED]

No response is written in the room. The block turns the day's two records into
material for the GFRN AI working group.

Slides: Two sides of the room -> The 18 tasks, two colours -> Three flipcharts
-> What happens next.

| Min | What |
|---|---|
| 6 | Two sides of the room |
| 8 | Your turn: the 18 tasks, two colours |
| 8 | Three flipcharts |
| 2 | What happens next |
| 6 | Buffer, absorbs a late ship |

### Two sides of the room (6 min, countdown 5)

- "Disclose if used at all" on one side, "a yes-or-no flag loses the intent" on
  the other. Argue, cross over if persuaded. Use v0.1.0 and v0.2.0 as evidence:
  the same person, the same data, two records.

### Your turn: the 18 tasks, two colours (8 min, countdown 7)

- Printed checklist of the proposed taxonomy. In one colour, tick the tasks the
  agent touched in sprint 1; in the other, sprint 2. Your declaration and your
  day sheet are the source. Circle the ones a peer would need to know about (the
  "substantive" test). Compare with your lunch answer.

### Three flipcharts (8 min, countdown 7)

- The consultation's open questions: placement (spread through the sections or
  one statement), a mandatory null statement, describing oversight. One sticky
  note per person per chart, one line each, from what the two records showed.

### What happens next (2 min)

- The wall goes to the GFRN AI working group. Round 2 of the consultation closes
  16 October. The chat room stays open.

---

## Close: the zine (16:30-17:00, 30 min) [PROTECTED, HARD START]

Slides: What you learned today -> Fold a zine -> Eight pages (countdown 15)
-> The table (countdown 8, survey link on the screen) -> Recall (final) ->
Thanks.

| Min | What |
|---|---|
| 2 | What you learned today, the four objectives |
| 3 | Fold demo at the front, shown twice |
| 15 | Fill and decorate, music on |
| 8 | Zines on the table, feedback; survey link on the screen |
| 2 | Final recall aloud, thanks |

### Fold a zine (3 min)

- One A3 sheet per person. Fold in half the long way, open; fold in half the
  short way, then each half again, open: eight panels. One cut along the middle
  crease, two panels long. Push the ends together, fold into a booklet. Show it
  twice at the front, slowly; the slide has the steps as text.

### Eight pages (15 min, countdown 15)

- Music on. Coloured pens and stickers on the tables. The pages:
  1. Cover: a name for today's paper, or for your agent workflow.
  2. My two sprints: v0.1.0 against v0.2.0, what changed and why (from the day
     sheet).
  3. Who reviews: who I want reviewing the agent's issues and pull requests, and
     who has a say in what an agent may touch in my project.
  4. Where the instructions live: what goes into my CLAUDE.md, what stays in my
     head.
  5. What I will not hand to an agent, and what I hand over from tomorrow.
  6. and 7. Left free for feedback from others.
  8. Biggest take-away, my one-line rule for working with an agent, and the
     recall sentence in my own words.
- Work alone. Instructor and helper answer questions at the tables, do not
  comment on content.

### The table (8 min, countdown 8)

- Zines in the middle of the table. Read at least three. Write on pages 6 and
  7: positive things noticed, questions, encouragements. Sign or not.
- Three flipcharts around the table, one note each if you have one: open
  questions, learnings, what I still wanted to say.
- The post-course survey link is on the screen the whole time: five minutes,
  anonymous, on the phone at the table or tonight.

### Final recall, thanks (2 min)

- Final recall slide with every blank filled, read aloud together.
- How to remove the two skills (`/plugin uninstall ghe-skills@ghe-skills`) and
  the app. The chat room stays open. Take your zine home.

---

## After the room empties

- Photograph the evidence wall and the three flipcharts for the working group.
- Collect the parked-problem list from the helper; answer open questions the same
  week.
- Note actual per-block times on this plan for the retrospective.
