# agentsforsci-ghe lesson plan (run of show)

Tuesday 29 September 2026, 08:30-17:00, Villa Hatt, ETH Zurich. Built from the
deck (`workshop/slides.qmd`) and the schedule CSV. Per-block times get updated
after the rehearsal (same file, new commit, no amend).

The focus of this plan is the **My turn** blocks: exactly what I do at the
keyboard while the room watches. My-turn slides say only "sit back and watch";
the steps below are the demo script, not shown on screen. Every demo runs on
`agentsforsci-ghe/fstp-eval-india`, the repository of the rainbow-train demo
account. Expect to adapt to what the agent shows live.

## Operating rules

- My turn = instructor drives, room watches and notes questions. Your turn =
  participants drive, sticky note when done. Our turn = whole room does the same
  small step together.
- Location icons on every Your-turn slide: terminal = Claude Code; laptop-code =
  RStudio; GitHub mark = github.com in the browser; comments = the Claude chat in
  the browser; pen = paper; mobile-screen = the Claude app on the phone.
- One question, your own, runs through the day. Each round changes one variable:
  who reads the files, who decides the steps, who reviews, where the instructions
  live. The variable is named on the section slide of every round.
- Every round ends with the same self-check: would I merge this?
- Reflect right after the activity; the block after a break opens with the
  question that went into the break.
- Bounded regroup after each Your turn: 2 min, then park-and-pair, 1:1 fix at the
  next break. Never let one stuck participant stop the room.
- Protected blocks: the partner review of issues (13:00), the walk with the agent
  (14:00), the first release (15:10), the taxonomy checklist (16:10). If behind,
  cut in this order: the buffers, be the agent (15 to 8), the round 5 pair
  comparison (7 to 4), the data package demo (8 to 4).
- Every example path follows the folder convention from July:
  `~/Documents/gitrepos/gh-org-agentsforsci-ghe/<repo>` for repositories in this
  organisation, `~/Documents/gitrepos/gh-rainbow-train/<repo>` for a personal
  account. `gh-org-*` and `gh-*` sit next to each other inside `gitrepos`.
- The day runs in auto mode. Shift+Tab switches to manual mode at any time; say
  so once in the safety rails block and leave it at that.

## Materials

- Yellow sticky notes on every seat (done-signal), a second colour for the
  evidence wall.
- Dot stickers and the poster for the arrival line ("never used AI for research"
  to "use an agent every week").
- Masking tape for the spectrum line and the stakes ladder on the floor.
- Three flipcharts and markers for the 16:10 block, plus one for the evidence
  wall.
- Printed bingo cards (one per person) and printed 18-task taxonomy checklists
  (one per person).
- Power strips for the laptops that stay inside at 14:00.

## Breaks and the questions that go into them

| Break | Time | Question on the slide | Opens the next block as |
|---|---|---|---|
| 1 | 10:00-10:10 | What in your data folder would you not want a model to read? | Safety rails: look through `data/` once more |
| 2 | 11:00-11:10 | Would you merge what the agent just did? What would it take? Leave your screen on | Gallery walk |
| Lunch | 12:00-13:00 | Of the 18 tasks in writing a paper, which would you hand to an agent, and which never? | Stakes ladder on the floor |
| 3 | 14:00-14:20 | Walk with your agent: what does it ask you, and what does it decide alone? | Evidence wall notes |
| 4 | 15:00-15:10 | Could you recreate what the agent built today if the AI were gone? | CLAUDE.md slides |
| 5 | 16:00-16:10 | Disclose whenever AI was used, or does a yes-or-no flag lose the intent? Pick a side | Two sides of the room |

Breaks outdoors where weather allows. The helper takes the list of parked
participants into every break.

---

## Arrival (08:30-09:00, 30 min)

- Room: projector, wall space for the evidence wall and the anchor questions,
  three flipcharts, sticky notes on every seat, tape lines laid before people
  arrive.
- Setup clinic as people arrive: `claude --version`, `/status`, `claude mcp list`.
  Anyone without a working install moves to claude.ai/code. The helper does this,
  not me.
- Phone check at the door: Claude app installed, signed in with the workshop
  account, same organisation as the laptop. Anyone without it gets the fallback
  for the 14:00 walk (leave the laptop running, go outside anyway).
- Dot sticker on the arrival poster on the way in. First entry on the evidence
  wall.

---

## Opening: security, literacy, transparency, disclosure (09:00-09:45, 45 min)

Slides: Welcome -> Spectrum line -> Four themes (four slides) -> How the day
works -> The variable -> Learning objectives -> Schedule -> Your turn (anchor
question) -> The instructor's question.

### Welcome (5 min)

- Link back to July: same workflow, one new participant in it.
- Opening claim, said once: subject matter expertise now matters more than
  programming skill.
- Room rule: never make another human read AI slop. Pay attention, read
  everything it does.

### Spectrum line (8 min)

- Tape line along the room. Stand by agent experience (never, to weekly). Two
  voices from each end.
- Re-sort by "how much do I trust the output". Two voices again. Sit down.

### Four themes (15 min)

- One slide and one question each, one neighbour minute per question (countdown
  1): what must never go in; how do I know this is right; could I recreate it if
  the AI were gone; what do I say, and to whom.
- The background pages carry the arguments; the slides carry only the question
  and one line.

### How the day works, objectives, schedule (5 min)

- One question, six rounds, one variable per round, the self-check, the evidence
  wall, a question into every break.
- Objectives (four, keyword-led). Schedule: point at the breaks on the hour.

### Your turn: your anchor question (12 min, countdown 10)

- On paper: one question your data can answer. Swap with a neighbour, who makes
  it 20 percent more specific. Pin it on the wall.
- Then the instructor's question on the slide: which of the 47 FSTPs meet the
  CPCB discharge standard of 30 mg/L BOD, and how does BOD removal compare across
  treatment technologies?

---

## Condition one: the work as you do it now, current state (09:45-10:00, 15 min)

Slides only, labelled "current state". No exercise.

Slides: Round 0 (variable) -> The steps of a paper -> Round 1 (variable) -> My
turn (chat) -> Quote (Tao) -> Recall v1 -> Would I merge this? -> Break 1.

### Round 0 (5 min)

- The steps of a paper as you do them now and where the hours go, one slide.
- Neighbour minute (countdown 1): where does AI sit in your workflow today, if
  anywhere?

### My turn: round 1, chat (7 min) [DEMO SCRIPT]

Browser, claude.ai chat, the report PDF from
`~/Documents/gitrepos/gh-org-agentsforsci-ghe/fstp-eval-india/data/`.

1. Upload the report, ask the anchor question. Show the answer and ask for
   receipts: which page, which table. (3)
2. The parameter that does not exist: "What are the helminth egg counts in the
   treated effluent per plant?" The report's tables carry pH, TS, TDS, TSS, COD,
   BOD, TKN, ammoniacal nitrogen, total phosphate and faecal coliform, not
   helminth eggs. Confirmed in rehearsal: [note what the model did]. (2)
3. Name it: the answer sounds the same whether it is right or not. Tao quote as
   the transfer: terse, precise questions. (2)

### Recall v1 and break (3 min)

- Recall slide v1, first blank filled: you write a question.
- Would I merge what chat gave me? Asked, not answered.
- Break slide with question 1, restart 10:10.

---

## Break 1 (10:00-10:10, 10 min)

Question 1 on the screen. Helper takes the parked list.

---

## Condition two, part one: the first run (10:10-11:00, 50 min)

Slides: Question 1 opener -> Our turn (safety rails) -> Your turn (be the agent)
-> Model -> Harness -> Tool call -> Round 2 (variable) -> Your turn (round 2) ->
Clarify -> Break 2.

### Our turn: safety rails (10 min)

- Opens with question 1: two answers from the room.
- Together, step by step: open `data/` in your own repository and look once
  more against the group rule; terminal at
  `~/Documents/gitrepos/gh-org-agentsforsci-ghe/<your repo>`, not one level up
  (the agent reads the folder it starts in); `git switch dev`; `claude`;
  `/status`; find the mode line (auto mode, Shift+Tab for manual); `/context`.
- Hand out the bingo cards. They run until 16:00.

### Your turn: be the agent (15 min, countdown 8, then three slides)

- In the chat, not in Claude Code: "I have a repository with data. Ask me for the
  files you need to answer this question, one at a time, and I will paste what you
  ask for: <your anchor question>." Paste by hand. Feel the loop.
- Then three slides: model (stateless, on the provider's servers), harness (the
  loop, the tools, the permission layer, on your laptop), tool call (what scrolls
  past). Point at what they just did by hand.

### Your turn: round 2 (20 min, countdown 20)

- Everyone types the same frame with their own question in it, nothing else:
  "Answer the following question using the data in this repository and write up
  the result: <your anchor question>."
- Watch the tool calls. Do not intervene. Do not commit.

### Clarify and break (5 min)

- Regroup 2 min. Clarify slide. Break slide with question 2: leave your screen
  on.

---

## Break 2 (11:00-11:10, 10 min)

Question 2 on the screen. Screens stay on for the gallery walk.

---

## Condition two, part two: what it did with one line (11:10-12:00, 50 min)

Slides: Gallery walk -> Reflect -> Where repositories live -> Inside a
repository -> Git-trust ladder -> Our turn (install the skills) -> Recall v2 ->
Quote (Boykis) -> Lunch.

### Gallery walk (10 min, countdown 10)

- Result, transcript and file pane on every screen. Read three other screens.
  Look at where files landed and what they are called. Variation is the point.

### Reflect (10 min, countdown 2 for the note)

- What did it assume without asking? Where did it put files and how did it name
  them? What did it cost and was it worth it? Did it use git? Would I merge this
  (hands up)?
- One note each for the evidence wall.

### Folder and file organisation, three levels (12 min)

- Level 1, where repositories live: `gitrepos/` with `gh-org-agentsforsci-ghe/`,
  `gh-org-gitforsci-ghe/` and `gh-rainbow-train/` side by side, never in a
  cloud-synced folder. The agent starts inside the repository, never one level
  up.
- Level 2, inside a repository: the template as a tree (`data/raw_data/`,
  `data/derived_data/`, `data/metadata/codebook.csv`, `analysis/`,
  `docs/reports/`, `src/`). [Confirm the template before the day.]
- Level 3, file names: lowercase, dash as separator, short, two-digit prefix for
  scripts (`01-read-data.R`).
- One minute on paper: where would your round 2 files belong?

### Git-trust ladder and the skills (8 min)

- Picks up "did it use git". The ladder with the issue step: do all commits
  yourself; tell the agent when to commit; let the agent commit, you write the
  issues and open the PR; let the agent make the whole PR.
- Our turn, install the two GHE skills in Claude Code:
  `/plugin marketplace add Global-Health-Engineering/skills`, then
  `/plugin install ghe-skills@ghe-skills`, then start a new session. A failed
  install goes to the helper over lunch.

### Recall v2, quote, lunch (5 min, buffer 5)

- Recall slide v2, second blank filled: the agent reads your repository.
- Boykis: we should be more tired than the model.
- Lunch slide with the lunch question, countdown 60. If the buffer is unused,
  lunch starts early.

---

## Lunch (12:00-13:00, 60 min)

Lunch question on the screen. Helper fixes failed skill installs.

---

## Condition three, part one: the planned run (13:00-14:00, 60 min)

Slides: Stakes ladder -> Round 3 (variable) -> My turn (plan mode) -> Your turn
(round 3) -> Pair talk -> Round 4 (variable) -> Your turn (round 4a, issues) ->
Find your review partner -> Your turn (review the issues) -> Our turn (hand-over)
-> Break 3 (walk with your agent).

### Stakes ladder (5 min)

- Opens with the lunch question: two answers.
- Four rungs taped on the floor: implement it; plan, then implement; plan,
  review the plan, implement, review the implementation; design first, then
  repeat the cycles. Stand on the rung for your anchor question, then for "a
  figure in your thesis", then for "a throwaway plot". Sit down.

### My turn: round 3, plan mode (7 min) [DEMO SCRIPT]

Terminal at `~/Documents/gitrepos/gh-org-agentsforsci-ghe/fstp-eval-india`,
branch `dev`.

1. Shift+Tab until the status line says plan mode. Same frame as round 2 with the
   instructor's question. (1)
2. The first plan proposes extracting Table 9 (pages 34 to 35) to a CSV somewhere.
   Read it out. (2)
3. Reject with one sentence: "Not like this: the PDF stays in `data/raw_data/`,
   the extracted table goes to `data/derived_data/`, a codebook to
   `data/metadata/`, and files are named by our rules." (1)
4. Ask for a markdown plan I can edit: "Write the plan as a markdown file I can
   edit before you do anything." Open it, change one line, show that this is the
   editable plan. Do not implement. (3)

### Your turn: round 3 (15 min, countdown 15)

- Rerun the round 2 frame in plan mode. Reject the first plan on purpose, with
  one sentence that points at the template and the naming conventions. Ask for a
  markdown plan you can edit. Do not implement.

### Pair talk (3 min, countdown 3)

- What did one sentence change? Would I merge this plan?

### Your turn: round 4a, issues (10 min, countdown 10)

- Ask the agent to turn the approved plan into four issues on your repository:
  (1) organise the repository following the template; (2) the analysis inside a
  Quarto manuscript with `format: docx` and one figure produced by a code chunk;
  (3) five references from your Zotero library; (4) a methods paragraph. Each
  issue: a title, what done looks like, the files it touches.

### Find your review partner, review the issues (12 min, countdown 10)

- Move to sit with your partner (neighbour pairs, triple if odd). Review each
  other's issues on GitHub before any code exists. Comment where a step is
  unclear.

### Our turn: hand-over to the phone (8 min) [SCRIPT]

Step by step, everyone at the same time.

1. In the session: "Implement issues 1 and 2 on the dev branch. Run
   /ghe-skills:commit after each issue. Ask me when you are unsure." (2)
2. Type `/remote-control`. A link and a QR code appear. (1)
3. Scan the QR code with the Claude app, or open Code in the app: the session
   shows a computer icon with a green dot. (2)
4. Send one message from the phone: "Status?" The answer appears on both
   screens. (1)
5. Laptop plugged in, lid open, terminal open. (1)
6. Break slide with question 3. Go outside. (1)

Fallback for a failed pairing: leave the laptop running, go outside anyway, read
the transcript on return. Same-account check: `/status` on the laptop, the
account and organisation in the app.

---

## Break 3: walk with your agent (14:00-14:20, 20 min)

Question 3 on the screen. Check progress from the phone every few minutes,
answer what it asks, do not start new tasks. The helper stays inside with the
laptops.

---

## Condition three, part two: review and merge (14:20-15:00, 40 min)

Slides: Question 3 opener -> Your turn (finish round 4b) -> Partner review ->
Recall v3 -> My turn (CSV against data package) -> Clarify -> Break 4.

### What did it ask you? (5 min)

- Opens with question 3: what did it ask you, what did it decide alone. Notes on
  the evidence wall.

### Your turn: finish round 4b (10 min, countdown 10)

- Back at the laptop: read the diff. If the agent is not done, it finishes now.
  Then `/ghe-skills:open-pr`.

### Partner review (10 min, countdown 10)

- Partner reviews the pull request on GitHub: would I merge this? Merge.

### Recall v3 (3 min)

- Blanks three to five filled: the agent proposes a plan, you reject it with one
  sentence, a colleague reviews the issues and the pull request.

### My turn: CSV against data package (8 min) [DEMO SCRIPT]

Not the fstp data. An openwashdata package of your choice against its raw CSV.

1. Same short prompt on the plain CSV in a scratch repository: what is in this
   data, and what would you compute first? (3)
2. Same prompt on the installed data package: it reads the documentation, names
   the variables, and proposes something that fits. (3)
3. Name the difference: documentation you wrote for a colleague is documentation
   the agent needs too. Sets up 15:10. (2)

### Clarify and break (4 min)

- Clarify slide. Break slide with question 4, restart 15:10.

---

## Break 4 (15:00-15:10, 10 min)

Question 4 on the screen.

---

## Where the instructions live (15:10-16:00, 50 min)

Slides: Question 4 opener -> CLAUDE.md -> CLAUDE.md against a skill -> Round 5
(variable) -> Your turn (round 5) -> Pairs -> The release path -> Our turn
(first release) -> My turn (declaration) -> Your turn (your declaration) -> Break
5.

### CLAUDE.md (5 min, after a 3 min opener)

- Opens with question 4: two answers.
- CLAUDE.md in the project folder: versioned, shared with collaborators, in the
  record. It holds what is true for this project: the template, the naming rules,
  where the codebook is, how to render. One line: a user level file exists on your
  machine, applies to every project, and never appears in the repository.
- CLAUDE.md against a skill: the "when" is always sent, the "what" loads on
  demand. Told it three times, put it in CLAUDE.md. Lots of text for one purpose,
  make it a skill. Never write skills prospectively.

### Your turn: round 5 (12 min, countdown 12)

- "Write a CLAUDE.md for this repository from what we did today: the folder
  template, the naming rules, where the codebook is, how to render the
  manuscript. Then fill data/metadata/codebook.csv for the derived table."
- New session (`/exit`, `claude`). Rerun the round 2 frame.

### Pairs (7 min, countdown 7)

- Round 2 output next to round 5 output: did it follow the template without
  being told? Would I merge this? Bingo closes.

### Our turn: first release (10 min) [SCRIPT]

1. Merge the pull request on GitHub if not merged yet. (1)
2. "Switch to main and pull. Render the manuscript to DOCX." (3)
3. "Tag v0.1.0 and create a GitHub release with the DOCX attached." The agent
   runs `gh release create v0.1.0 <file>.docx`. The DOCX stays out of git. (3)
4. "Switch to dev, merge main into it, and push." Never leave a release on main
   with dev behind it. (2)
5. Open the release page on GitHub. (1)

### My turn: the declaration (8 min) [DEMO SCRIPT]

1. "Write a declaration of AI use for this repository up to tag v0.1.0. Read the
   commit history and its trailers, the prompts folder, and CLAUDE.md. Say which
   files an agent touched, in response to which instruction, and what I checked.
   Put it in the release notes of v0.1.0." (5)
2. Open the release notes. Read one line aloud. (3)

### Your turn: your declaration (5 min, countdown 5)

- Same on your repository. Put the declaration into the notes of your release.
- Break slide with question 5, restart 16:10.

---

## Break 5 (16:00-16:10, 10 min)

Question 5 on the screen. Pick a side before you come back.

---

## Disclosure rules in the making: what the record shows (16:10-16:45, 35 min)

No response is written in the room. The block turns the day's record into
material for the GFRN AI working group.

Slides: Two sides of the room -> The 18 tasks -> Three flipcharts -> What
happens next.

### Two sides of the room (12 min, countdown 10)

- Opens with question 5. "Disclose if used at all" on one side, "a yes-or-no
  flag loses the intent" on the other. Argue, cross over if persuaded.

### Your turn: the 18 tasks (8 min, countdown 8)

- Printed checklist of the proposed taxonomy. Tick the tasks the agent touched
  today, from your declaration. Circle the ones a peer would need to know about
  (the "substantive" test). Compare with your lunch answer.

### Three flipcharts (10 min, countdown 10)

- The consultation's open questions: placement (spread through the sections or
  one statement), a mandatory null statement, describing oversight. One sticky
  note per person per chart, one line each, from what the record showed today.

### What happens next (3 min, buffer 2)

- The wall goes to the GFRN AI working group. Round 2 of the consultation closes
  16 October. The chat room stays open.

---

## Close (16:45-17:00, 15 min)

Slides: Standing circle -> Recall (final) -> What you learned today -> Feedback,
and thanks -> Thanks.

- Standing circle. On paper, then aloud: one thing I will change about how I
  work, one thing I will not hand to an agent.
- Final recall slide with every blank filled.
- What you learned today, mirrored to the four objectives.
- Feedback survey link while the slide is up. How to remove the two skills
  (`/plugin uninstall ghe-skills@ghe-skills`) and the app. The chat room stays
  open.
