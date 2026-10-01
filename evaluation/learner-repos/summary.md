# Learner repositories after the workshop day: one page

Agents for Scientists, 29 September 2026. Records read on 1 October 2026
from thirteen learner repositories; data and method in this folder.

**Nine of thirteen repositories ran the day.** The other four
(bcmeter-example, beaver-ss, biogas-malawi, cybersecurity-ownership) stayed
at their pre-work state and show no commit on the day.

**The choreography held.** All nine active repositories merged a sprint 1
pull request and tagged v0.1.0 between 11:56 and 12:02 local time, and
tagged v0.2.0 between 15:45 and 15:49. In between they wrote 37 issues
from their plans (13:43 to 14:18), implemented and closed 31 of them, and
in eight rooms wrote TODO lines into the manuscript for the agent to work
through (14:41 to 14:49). The timestamps match the run sheet block by
block.

**The agent wrote, the humans asked and reviewed.** Of the 114 non-merge
commits on the day, 86 carry the commit skill's `Assisted-by` trailer, 6
the older co-author line, and 22 are human-only. The human-only commits
are the three-questions file, the "added todos" commits and file moves.
Eight learners work in R and Quarto, one in Python and Quarto; all render
to DOCX. The first run was on Opus 5.5 in eight rooms; six then
switched to Fable 5.1 for the rest of the day.

**The records cover the day well, with three gaps.**

- No pull request carries a GitHub review or comment (23 pull requests,
  0 reviews). The partner review left no trace; the TODO pass did.
- CLAUDE.md was written in all nine repositories but reached `main` in
  only four. Four sit on `dev`, one only behind the v0.2.0 tag. Two v0.2.0
  tags point at commits that are not on `main`.
- The prompt archive is uneven: 111 prompts across nine repositories,
  from 5 to 19 each, and 13 assisted commits cite no prompt.

**Every v0.2.0 release has a "Declaration of AI use".** Seven are long
(6,000 to 11,000 characters) with a per-commit table of instruction,
model and files touched. Two are five bullet points. A target shape would
make them comparable.

**Outcomes.** Eight repositories answered two of their three questions,
sensor-validation all three; question 3 was by design the one the data
cannot answer. Several afternoons went past one question: an R package
with CI (ghg-bsfl), twenty rater agents with author adjudication
(implementation-mzuzu), an age-uncertainty ensemble and an interactive
explorer (caves-currents), a tidy data package and 20 figures
(washschools-nigeria), a leaflet map (water-quality-col), a data review
and cleaning pipeline (tdabc-mzuzu), a generated codebook
(sensor-validation).

**For the next iteration.** Put CLAUDE.md before the last pull request and
spell out "merge, then tag". Decide whether the review is a GitHub review
or the TODO pass, and teach one. Give the declaration a target length and
three headings. Make the prompt archive the default. Add a data-hygiene
line to the pre-work check (one repository committed 254 MB of logs and
images, one a Word lock file).
