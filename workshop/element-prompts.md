# Prompts for the chat room

Every prompt learners type on 29 September, in slide order, for pasting into the Element room when the step comes up. Each block is the exact text on the slide. Text in angle brackets is the part each learner replaces. Times follow `workshop/lesson-plan.qmd`.

## 09:57 Our turn: safety rails

```text
Create a branch called dev and switch to it. If dev already exists, switch to it.
```

## 10:14 Our turn: two skills

One command at a time:

```text
/plugin marketplace add Global-Health-Engineering/skills
```

```text
/plugin install ghe-skills@ghe-skills
```

## 10:39 Your turn: the framed run

```text
Answer the following question using the data in this repository and write up the result as a Quarto manuscript that renders to DOCX: <your question 1>
```

## 11:02 Your turn: the studio

The full prompts from the printed cards.

Card 1, the question you cannot answer yet:

```text
Answer the following question using the data in this repository and add the result to the manuscript: <your question 2>
```

Card 2, the question the data cannot answer:

```text
Answer the following question using the data in this repository: <your question 3>
```

Card 3, the codebook:

```text
Describe every file in data/. Then write a codebook for the main table as a CSV with one row per variable: name, type, unit, description.
```

Card 4, one figure, rendered (recommended):

```text
Add one figure that answers <your question 1> to the manuscript, with the plot code in a chunk, and render the manuscript to DOCX.
```

Card 5, five references:

```text
Find the five references in my Zotero library that are most relevant to this data, and say in one sentence each why.
```

Card 6, the README, read by a stranger:

```text
Read the README and tell me what a new collaborator would not understand about this repository. Do not change anything.
```

Card 7, what does it know right now (type `/context` first):

```text
What do you know about this repository right now, and what have you not read?
```

Card 8, name the tool:

```text
Use git log to tell me the history of this repository in five lines.
```

## 11:40 Our turn: ship v0.1.0

After `/ghe-skills:open-pr` and the merge on GitHub:

```text
Switch to main and pull.
```

After the render in RStudio:

```text
Tag v0.1.0 and create a GitHub release. Attach the DOCX if it rendered; if not, say in the release note that the manuscript does not render yet.
```

```text
Switch to dev, merge main into it, and push.
```

## 13:00 Our turn: start your plan

Type `/clear` first, then Shift+Tab until plan mode is on.

```text
Answer the following question using the data in this repository and write up the result as a Quarto manuscript that renders to DOCX: <your sprint 2 question>. Plan only. Do not run any analysis or write any file yet.
```

## 13:28 Your turn: plan mode

After leaving plan mode:

```text
Write the plan as a markdown file in this repository that I can edit.
```

## 13:44 Your turn: the issues

```text
Turn the plan into four issues on this repository. Each issue gets a title, what done looks like in at most five checkboxes, and the files it touches:

1. Organise the repository following the template.
2. The analysis inside the Quarto manuscript with format: docx, one figure from a code chunk.
3. Five references from my Zotero library.
4. A methods paragraph.
```

## 14:10 Our turn: hand over to your phone

```text
Implement issues 1 and 2 on the dev branch. Run /ghe-skills:commit after each issue, then push. Ask me when you are unsure.
```

## 14:46 Your turn: TODOs, then the pull request

```text
Work through the TODOs in the manuscript. Remove each one when it is done. When all are done, run /ghe-skills:commit.
```

## 15:11 Your turn: round 5

```text
Write a CLAUDE.md for this repository from what we did today: the folder template, the naming rules, where the codebook is, how to render the manuscript. Then fill data/metadata/codebook.csv for the derived table.
```

Then `/ghe-skills:commit`, `/exit` and `claude` for a new session:

```text
Read the review comments on my open pull request and work on each one. Reply to each comment with what you changed. Then run /ghe-skills:commit and push the dev branch.
```

## 15:36 Our turn: ship v0.2.0

```text
Switch to main and pull.
```

After the render in RStudio:

```text
Tag v0.2.0 and create a GitHub release with the DOCX attached.
```

```text
Switch to dev, merge main into it, and push.
```

## 15:51 Your turn: your declaration

```text
Write a declaration of AI use for this repository from the first commit to tag v0.2.0. Read the commit history and its trailers, the prompts folder, the issues, the pull requests and CLAUDE.md. Say which files an agent touched, in response to which instruction, who reviewed what, and what changed between v0.1.0 and v0.2.0. Put it in the release notes of v0.2.0.
```

## 16:58 Thanks

To remove the skills:

```text
/plugin uninstall ghe-skills@ghe-skills
```
