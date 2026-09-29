// The studio cards: one sheet per table, 35 minutes from 11:02. The dashed
// lines are cut lines, if the cards are to be handed round one by one.
#import "style.typ": *
#show: handout.with(title: "The studio: ten cards")

#set text(10pt)
#grid(
  columns: (1fr, 1fr),
  column-gutter: 8mm,
  [
    - Ten cards, 35 minutes, your own repository. Pick freely, in any
      order, *at least two*. *Card 4 for everyone*: it is the render test
      for the release before lunch.
    - Your questions from the morning: 1 is the one you know the answer
      to, 2 the one you do not, 3 the one your data cannot answer.
  ],
  [
    - Changed a file? Run `/ghe-skills:commit`. Either way, fill one row
      of your day sheet.
    - If it asks, answer. Stuck for two minutes: raise your hand, next card.
    - Curious? Go further. Ask it about what just happened: why did you
      do that? What does this line do?
  ],
)
#v(1mm)

#let prompt(body) = block(
  width: 100%,
  fill: paper,
  radius: 3pt,
  inset: (x: 6pt, y: 5pt),
  body,
)

#let card(n, title, oneliner, body, watch) = block(
  width: 100%,
  height: 100%,
  stroke: (thickness: 0.6pt, paint: line-grey, dash: "dashed"),
  inset: 7pt,
)[
  #set text(9pt)
  #set par(leading: 0.45em, spacing: 0.55em)
  #text(10.5pt, weight: "bold", fill: blue)[#n. #title] \
  #text(fill: muted, style: "italic", oneliner)

  #body

  *Watch for:* #watch
]

#block(height: 1fr, grid(
  columns: (1fr, 1fr),
  rows: (1fr,) * 5,
  gutter: 3mm,
  card(
    1, [The question you cannot answer yet],
    [Ask your question 2 and watch what it assumes without asking.],
    prompt[Answer the following question using the data in this repository
      and add the result to the manuscript: _your question 2_.],
    [what it assumes without asking. Does it name the assumption?],
  ),
  card(
    2, [The question the data cannot answer],
    [Ask your question 3. Does it say the data cannot answer it, or does it
      make something up?],
    prompt[Answer the following question using the data in this
      repository: _your question 3_.],
    [does it say the data cannot answer it, or does it produce an answer
      anyway? Ask for receipts: which file, which column.],
  ),
  card(
    3, [The codebook],
    [Ask it to describe every file in data/ and write a codebook, one row
      per variable.],
    prompt[Describe every file in data/. Then write a codebook for the main
      table as a CSV with one row per variable: name, type, unit,
      description.],
    [where it puts the codebook and what it calls it. Would a colleague
      find it?],
  ),
  card(
    4, [One figure, rendered (recommended)],
    [Ask for one figure for your question 1 in the manuscript, then render
      it to DOCX.],
    prompt[Add one figure that answers _your question 1_ to the manuscript,
      with the plot code in a chunk, and render the manuscript to DOCX.],
    [whether it renders. If it does not, this is the moment to find out,
      not at the release. Raise your hand.],
  ),
  card(
    5, [Five references],
    [Ask it for the five most relevant references in your Zotero library.],
    prompt[Find the five references in my Zotero library that are most
      relevant to this data, and say in one sentence each why.],
    [does it read the library through the Zotero tool, or does it guess
      titles? Check one. If the tool returned nothing: did it go around the
      tool, and did it ask you first?],
  ),
  card(
    6, [The README, read by a stranger],
    [Ask what a new colleague would not understand in your README.],
    prompt[Read the README and tell me what a new collaborator would not
      understand about this repository. Do not change anything.],
    [does it read, or does it flatter? Is anything it names actually
      missing? Nothing to commit.],
  ),
  card(
    7, [What does it know right now],
    [Type /context, then ask what it has read and what it has not.],
    [Type `/context`. Then:
      #prompt[What do you know about this repository right now, and what
        have you not read?]],
    [the size of the context and what is in it. The answer should match
      the list. Nothing to commit.],
  ),
  card(
    8, [Name the tool],
    [Ask it to use git log to tell the history of your repository in five
      lines.],
    [#prompt[Use git log to tell me the history of this repository in five
        lines.]
      Then try another tool by name: read a file, list a folder, run a
      command.],
    [the tool call line before each answer. Nothing to commit.],
  ),
  card(
    9, [The same task twice],
    [Start a new session and run card 1 again, word for word. What
      changed?],
    [Type `/exit`, then `claude`, then card 1 again, word for word.],
    [what differs between the two runs. Which one would you merge? Commit
      the one you would.],
  ),
  card(
    10, [Wild card],
    [Ask anything you are curious about.],
    [],
    [your own reaction. Write it on the day sheet.],
  ),
))
