// Shared look for the printed handouts of 29 September 2026. Each handout
// is one A4 page. Compile one with the Typst that ships with Quarto:
//   quarto typst compile workshop/print/question-sheet.typ
// The text follows workshop/studio-cards.qmd, the online print page.

#let blue = rgb("#0F4C81")
#let ink = rgb("#1e1e1e")
#let muted = rgb("#5c5751")
#let paper = rgb("#F2F2F2")
#let line-grey = rgb("#9a948d")

#let handout(title: "", flipped: false, name-field: false, body) = {
  set document(title: title, author: "Lars Schöbitz")
  set page(
    paper: "a4",
    flipped: flipped,
    margin: (x: 14mm, top: 12mm, bottom: 13mm),
    footer: align(center, text(8pt, fill: muted)[
      Agents for Scientists #sym.dot.c Global Health Engineering, ETH Zurich
      #sym.dot.c agentsforsci-ghe.github.io/website
    ]),
  )
  set text(font: "Atkinson Hyperlegible", size: 11pt, fill: ink, lang: "en")
  set par(leading: 0.55em, spacing: 0.8em)
  set list(indent: 0.4em, body-indent: 0.5em, spacing: 0.5em)
  show raw: set text(size: 1.05em)

  grid(
    columns: (1fr, auto),
    align: (left + bottom, right + bottom),
    text(20pt, weight: "bold", fill: blue, title),
    if name-field {
      text(11pt)[Name #box(width: 60mm, stroke: (bottom: 0.6pt + ink))]
    } else {
      text(10pt, fill: muted)[Tuesday, 29 September 2026]
    },
  )
  v(-1mm)
  line(length: 100%, stroke: 0.8pt + blue)
  v(1mm)
  body
}
