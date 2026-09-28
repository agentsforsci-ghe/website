// The question sheet: one per person, on the table at arrival, pinned on
// the wall at 09:41, where it becomes the question wall at 11:17.
#import "style.typ": *
#show: handout.with(title: "Your question bank", name-field: true)

Three questions your own data can answer, one sentence each. Then swap
with a neighbour, who writes box 4. Pin the sheet on the wall.

#let answer-box(label, hint) = block(
  width: 100%,
  height: 100%,
  stroke: 0.8pt + line-grey,
  radius: 3pt,
  inset: 9pt,
)[
  #text(weight: "bold", fill: blue, label) #h(3pt) #text(fill: muted, hint)
]

// The block takes the height left under the header; the grid's 1fr rows
// share it.
#block(height: 1fr, grid(
  columns: 1fr,
  rows: (1fr, 1fr, 1fr, 1fr, auto),
  row-gutter: 5mm,
  answer-box("1. To check it.", "A question you already know the answer to."),
  answer-box("2. To explore.", "A question you do not know the answer to."),
  answer-box("3. To catch it.", "A question your data cannot answer."),
  answer-box(
    "4. Question 1, 20 percent more specific.",
    "Written by your neighbour: which column, which unit, which comparison.",
  ),
  text(10pt, fill: muted)[
    At 10:06 you type the three questions into `questions.md` in your
    repository and commit them by hand. Question 1 runs the framed run at
    10:39. Question 2 is card 1, question 3 is card 2. Sprint 2 is a
    choice: question 1 done properly, or question 2.
  ],
))
