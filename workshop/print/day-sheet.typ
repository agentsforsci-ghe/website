// The day sheet: one per person, handed out at 10:37, before the first
// run. Landscape, so the six columns have room to write in.
#import "style.typ": *
#show: handout.with(title: "The day sheet", flipped: true, name-field: true)

#set text(10.5pt)
#grid(
  columns: (1fr, 1fr),
  column-gutter: 10mm,
  [
    - One row for every run, all day.
    - Fill it right after the run, while you still remember.
  ],
  [
    - "Minutes it ran" is the clock time from your prompt until the agent
      stops. A first run on a PDF took 12 minutes in the dry run, most
      cards under 2.
    - You need it after lunch, when we look back at v0.1.0, and for page 2
      of your zine.
  ],
)
#v(1mm)

#let head(body) = text(10pt, weight: "bold", fill: blue, body)
#let run(body) = text(10pt, weight: "bold", body)

#block(height: 1fr, table(
  columns: (16fr, 30fr, 18fr, 10fr, 14fr, 12fr),
  rows: (auto,) + (1fr,) * 11,
  stroke: 0.6pt + line-grey,
  inset: (x: 6pt, y: 5pt),
  align: (x, y) => if y == 0 { left + bottom } else { left + horizon },
  fill: (x, y) => if y == 0 { paper },
  table.header(
    head[Run],
    head[What happened (one line)],
    head[What it assumed],
    head[Minutes it ran],
    head[Would I merge this?],
    head[Committed?],
  ),
  run[First run], [], [], [], [], [],
  run[Card], [], [], [], [], [],
  run[Card], [], [], [], [], [],
  run[Card], [], [], [], [], [],
  run[Plan], [], [], [], [], [],
  run[Issues], [], [], [], [], [],
  run[Issues 1 and 2 (from the phone)], [], [], [], [], [],
  run[TODOs], [], [], [], [], [],
  run[CLAUDE.md], [], [], [], [], [],
  run[Review comments], [], [], [], [], [],
  run[Declaration], [], [], [], [], [],
))
