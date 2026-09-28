# Agents for Scientists: curriculum notes from the design session

Date: 2026-09-21
Author: Lars Schöbitz, with Claude Code
Status: working notes, to be worked into the teaching repository

## What went in

### The workshop

A one-day Agents for Scientists workshop for the Global Health Engineering group at ETH Zurich, second in a series after the git workshop. Participants and the instructor each bring their own data in a GitHub repository. The instructor demo account is rainbow-train.

The question asked at the start: how to take participants through five stages.

1. Chat
2. Agent with a basic prompt
3. Agent in plan mode
4. Plan mode with GitHub issues and issue review
5. Skills

The constraint for the session was to leave no traces. No branches or commits were created in any repository.

### Six data repositories in the session

All are data-only with no code, no CLAUDE.md, no skills, and no issues.

| Repository | Contents | Fit |
|---|---|---|
| tdabc-mzuzu | One clean task-timing CSV, richest README | Instructor running example |
| beaver-ss | 89,000-row arthropod dataset, Quarto notebook stating the research question, body mass not yet computed | Chat-stage hallucination moment, skill for the ISD pipeline |
| myco-sanitation | Six relational CSVs joined on cup, barrel, and inoculum ids | Plan mode, since the joins need decisions |
| implementation-mzuzu | Five interview transcripts and a draft constitution as Word files | Qualitative coding skill, consent check needed |
| biogas-malawi | One Excel file, not opened | Chat or basic-prompt stage only |
| teufeng-website | README only | Not used |

### The workshop website

Repository agentsforsci-ghe/website, read-only clone.

- Published: an overview with schedule and learning objectives, and two pre-work steps (create your repository with your data, join the chat room).
- Held back as under review: four background pages on security, literacy, transparency, and disclosure, plus glossary, platform guide, and references.
- A prompts folder logs every agent prompt used to edit the site, with model and files touched. This is already a working example of the disclosure record the workshop is about.
- The schedule frames the day as three conditions: work as you do it now, agent with minimal input, agent with a reviewed plan and issues. Then a CSV versus data package block and a disclosure consultation response.

### Two external workshops, read in full

Both are CC BY 4.0.

**Posit, Introduction to AI** (posit-dev/ai-intro). Five sessions of one hour, one per weekday, for an organisational cohort. Every session is slides, a prose page, and one hosted Shiny app as the activity. Attendees install nothing and need no API key. The agents session on day five has no hands-on exercise, only a placeholder slide.

**Hadley Wickham and Jenny Bryan, Modern R Workflow** (posit-conf-2026/modern-r-workflow). One day at posit::conf, 14 September 2026, for R package developers using Posit Assistant in Positron. Morning: helping yourself, Positron tour as bingo, Posit Assistant basics. Midday: how agents work, safety and cost, AGENTS.md and skills. Afternoon: workflow ladder and best-practices feedback loop. A "Your turn" slide every four or five slides.

## Conclusions

### Run one question through every stage

Same task, several rounds, one variable changed per round, with a self-check question at the end of each round. This is the design both external workshops share. Name the variable explicitly at each stage: who reads the files, who decides the steps, who reviews, where the instructions live. The self-check is "would I merge this?"

For the instructor demo on tdabc-mzuzu the anchor question is: how much of each job's time goes to extraction versus rest and communication, per gulper, and what does a job cost?

### Reconcile the five stages with the three conditions

The website does not yet mention chat, plan mode, or skills. Chat fits inside condition one. Plan mode and issues are condition three. Skills close condition three. The learning objectives and schedule need to say so if participants should see the five stages.

### Stage-specific takeaways

**Stage 1, chat.**
- Ask the same question you will later ask the agent.
- Build a hallucination moment from the participant's own data, such as asking about a column that does not exist. On beaver-ss, ask about body mass, which the notebook says is not computed yet.
- Framing from Hadley: being 20 percent more specific improves results by 80 percent. Ask for receipts.
- Terence Tao quotes on terse, precise questions transfer well to scientists.

**Stage 2, agent with a basic prompt.**
- Everyone uses the same deliberately underspecified prompt, then compares with a neighbour. Variation is the point.
- Show the tool calls in the transcript and run the context command so participants see what is loaded.
- Reflect questions: what did it assume without asking, what did it cost and was it worth it, did it use git.
- Add a "be the agent" bridge from chat: participants paste files the model asks for by hand, so the loop is felt before Claude Code automates it. This is Posit's "be the tool" trick.
- Hadley's exercise: try to make the agent use every tool by name.

**Stage 3, plan mode.**
- Introduce Hadley's stakes ladder as the reason plan mode exists:
  - Very low stakes: implement it.
  - Low stakes: plan, then implement.
  - Medium stakes: plan, review the plan, implement, review the implementation.
  - High stakes: design first, then repeat the cycles.
- Have participants reject the first plan on purpose. Correcting a plan costs one sentence; correcting code costs a re-run.
- Alternative variant: always ask for a markdown plan you can read and edit.

**Stage 4, issues and review.**
- Use Hadley's git-trust ladder with the issue step inserted before the PR:
  1. Do all commits yourself.
  2. Tell the agent when to commit.
  3. Let the agent commit; you write the issues and open the PR.
  4. Let the agent make the whole PR.
- Pair participants so the partner reviews issues before any code exists. A colleague without agent access can still shape the work.
- Rule for the room: never make another human read AI slop. Pay attention, try to read everything it does.

**Stage 5, skills.**
- Rerun the stage 2 prompt after adding CLAUDE.md, so the difference is the lesson. Hadley reruns the compliment package with AGENTS.md the same way.
- Teach the two parts of a skill: the "when" is always sent to the model, the "what" is loaded on demand.
- Told the agent something three times, put it in CLAUDE.md. Lots of text for one purpose, make it a skill.
- Do not write skills prospectively. Ask the agent to create the file, but extract the content from a conversation that just happened.
- Examples to point at: the Posit course repo has a real non-code skill (summarise slides into a blog post). Hadley's repo contrasts a 17-line AGENTS.md with a large router-style skill of forty reference files.
- Claude needs a CLAUDE.md that includes AGENTS.md if one file should serve several harnesses.

### Operational patterns to copy

- A recurring fill-in-the-blank recall slide that evolves per stage: you write some words, the agent reads your repo, the agent proposes a plan, you approve, a colleague reviews the issue.
- Reflect questions after every activity, debriefed at the start of the next block. Posit's set: what worked, what surprised you, did you trust it and why. Add: what did the agent assume without asking?
- A pre-course survey with one "curiosity about LLMs" question seeding an FAQ page. The survey instrument itself is not published anywhere; only the mechanism is documented.
- One mentor per eight participants. A chat channel. A recap after every session.
- Bingo cards as a tool tour, adaptable to Claude Code: find the context command, the plan mode toggle, the permission prompt, the transcript view.
- Short outside-quote interludes when energy dips.
- A per-stage rehearsed prompt file with expected turns and known failure points, following Posit's demo README with "expect to adapt to what the assistant shows live".
- Opening claim from Hadley's welcome: subject matter expertise now matters more than programming skill.

### Cautions

- Model and pricing content ages within weeks. Posit's model tables from one run are already stale. Keep materials about workflow.
- Claude Code has no persistent R session. Decide beforehand whether rendering Quarto instead of interactive exploration is acceptable, or pair with an MCP REPL server as Hadley suggests.
- Confirm consent for LLM processing before the Mzuzu interview transcripts are used. Both external workshops warn about sending confidential material to a provider.
- Branch protection on main before stage 2, since every participant will push.
- Claude Code on the web is the fallback for failed laptop setups.
- Stage 4 needs GitHub access from the agent, via an authenticated gh CLI or the GitHub MCP server. Test before the day.

### Timing estimate

| Stage | Minutes |
|---|---|
| 1 Chat | 20 |
| 2 Basic prompt | 20 |
| 3 Plan mode | 30 |
| 4 Issues and review | 60 |
| 5 Skills | 45 |

## Open items

- The message about rainbow-train was cut off after "instructor account t".
- No agentsforsci-ghe repository exists yet for rainbow-train. Earlier courses had one per assignment, such as setup-rainbow-train in gitforsci-ghe.
- The whereabouts of the session branch named in the instructions is unverified. The check was interrupted. No branches or commits were created in any repository.
- The biogas-malawi Excel file was not inspected.

## Sources

- posit-dev/ai-intro, https://github.com/posit-dev/ai-intro
- posit-conf-2026/modern-r-workflow, https://github.com/posit-conf-2026/modern-r-workflow
- agentsforsci-ghe/website, https://github.com/agentsforsci-ghe/website
