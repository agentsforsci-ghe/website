# Layout review: three days compared, one combined

Date: 23 September 2026. Four local branches of this repository lay out the
29 September day. This file records how the fourth was built from the other
three: five reviewers, each with a different seat in the room, read all three
in full and wrote a report to the same brief. Their keep and drop lists, the
tally, and the decisions are below. The full reports are not in the
repository; the reviewers were agents run by the instructor's assistant, and
each spoke from a persona.

## The three layouts

| Branch | Shape | Contact time with Claude | Free |
|---|---|---|---|
| `feat/day-structure` (A) | six rounds, one anchor question, a 10-minute break every hour | 118 min | 0 |
| `feat/day-studio` (B) | explore wide in the morning with cards, go deep in the afternoon | 155 min | 45 |
| `feat/day-sprints` (C) | the whole path twice, a rough release before lunch, a planned one after | 148 min | 25 |
| `feat/day-combined` (D) | C's two sprints with B's studio inside sprint 1 | 172 min | 35 |

## The five seats

1. Arti, the fearful outsider from the July personas: will I keep up, is
   exploring safe, are the commit steps mine.
2. Bianca, the quick R user: where am I bored, do I get to try my own ideas,
   is the review real.
3. Cem, the controlled-AI researcher: commit discipline, the record, the
   declaration, the disclosure block.
4. An instructor trainer: timing realism block by block, cognitive load,
   retrieval practice, the close.
5. The helper who runs the room: what breaks operationally and when,
   materials, snacks, pairing, renders.

## Tally

Elements kept by three or more reviewers, and where they came from:

| Element | From | Votes |
|---|---|---|
| Two room rules on their own slide in minute three, commit often as rule two | B, C | 5 |
| Skills installed before the first agent run, sticky note when the command shows | B, C | 5 |
| The studio cards, with the sheet that logs "would I merge this?" and "committed?" | B | 5 |
| Zine pages 1 to 8, work alone, feedback in writing on pages 6 and 7 | B, C | 5 |
| Recall as guess, 20 seconds, reveal, write; the routine on its own slide | B, C | 5 |
| Two 20-minute snack breaks, the afternoon one as the walk with the agent | B, C | 5 |
| Question bank of three (known answer, unknown, unanswerable) | B | 3 |
| Rough v0.1.0 before lunch, self-merged, "do not polish", release without the DOCX and say so | C | 3 (Bianca, Cem, helper) |
| Rails, ladder and skills before snack 1, first run after it | C | 3 |
| Partner review of issues before any code exists, protected | A, B, C | 5 |
| "Be the agent" before the model, harness and tool call slides | A, B | 3 |
| The variable table on the opening slide | A | 3 |
| Pair talk after plan mode, and commit the plan | A, B | 3 |
| 18-task checklist in two colours, sprint 1 against sprint 2 | C | 4 |
| Round 5 given 20 minutes | all asked | 5 |
| Declaration over both releases, naming who reviewed what | C | 3 |
| Disclosure block protected at 30 minutes | A, C | 2, kept for the working group |

Dropped by three or more:

| Element | From | Reason |
|---|---|---|
| "Do not commit" in the first run, first commit at 14:00, skills after the first run | A | four hours of agent output uncommitted; the declaration reads two commits |
| A 10-minute break every hour | A | five breaks cost 15 minutes each in practice |
| Standing circle aloud | A | the zine table does it in writing |
| Tao placeholder | A | no sourced line exists; the Wickham line carries the point |
| The live CSV against data package demo | A, B, C | first cut in every plan, so it never happens; one slide from rehearsal keeps objective 3 |
| The harvest round-robin | B | 15 voices in 10 minutes; the sticky notes carry it |
| The gallery walk as its own block | A, C | the one-minute stand-up inside the studio gives the same exposure |
| Card 10, plan mode preview | B | repeats the 13:28 demo |
| "Commit after every card" without a rule for read-only cards | B | cards 6, 7 and 8 change no files |
| Ship v0.2.0 in 8 minutes | C | the same five steps got 15 in the morning |
| Sprint 2 merge before the CLAUDE.md commits are on the pull request | B, C | the tag would lack the file the declaration reads |

## Bugs the helper found in all three layouts

- `git switch dev` fails for anyone whose repository has no `dev` branch yet;
  the pre-work never creates one. The combined day uses `git switch -c dev`,
  with `git switch dev` as the line for anyone who already has it.
- `/ghe-skills:open-pr` never pushes. Every script step that opens a pull
  request is preceded by a push, and the hand-over prompt ends with "then
  push".
- Snacks laid out inside an Our turn script put the helper in two places.
  They go out during the chat demo (09:45) and the partner review (14:00).
- The release sticky note fired only when the DOCX showed, so a failed render
  never signalled. It now fires when the release page is up.

Addendum, 24 September 2026: the second bug was fixed in the skill rather
than on the slides. `/ghe-skills:open-pr` now pushes `dev` first, sets the
upstream if it is missing, and reports how many commits went up. The "Push
the dev branch" lines before both pull request steps are gone; the hand-over
prompt and the rerun keep a plain push, because no pull request is opened
there. The skill also ends by offering to run the test plan, which the learner
trace found hanging unanswered, so both pull request slides say "answer no".

## Where the reviewers split, and the decision

- **One release or two.** Arti and the trainer wanted one release, in the
  afternoon, with C's permission to fail. Bianca, Cem and the helper wanted the
  rough release before lunch: it is the render test with lunch as the repair
  window, it clears `dev` so the afternoon pull request is a clean chunk, and
  v0.1.0 against v0.2.0 is the one comparison made with two records. Decision:
  two releases. The ship before lunch may spill into lunch; the run sheet says
  so.
- **Studio length.** Three wanted 45 minutes, two wanted two cards inside a
  sprint. With the ship in the morning, 35 minutes fit, with a floor of 25 in
  the cut order and "at least two cards".
- **Where "be the agent" goes.** The trainer wanted it before the model,
  harness and tool call slides; Cem objected to pasting repository files into
  the chat before the safety rails. Decision: after snack 1, on the public data
  of the setup repository, right before the three slides and the first run.
- **Recall cadence.** The trainer asked for even spacing. Decision: blanks 1
  and 2 at the ship (11:56), 3 and 4 after the pair talk (13:46), 5 after the
  partner review (14:59), 6 after the declaration (15:55), the full sentence
  aloud at the close.

## What each layout contributed

- From A: the variable table, the break question table, the hand-over script
  with the pairing check, the demo scripts.
- From B: the room rules slide, the question bank, the cards and the sheet,
  the stand-up, the recall routine, the contact time table, the cut order with
  a floor for the studio, the zine close.
- From C: the two sprints, the rough release with the no-DOCX rule, the
  labelled self-merge, the declaration over both records, the lunch question
  that asks what the agent touched, the two pen colours, the protected
  disclosure block.
