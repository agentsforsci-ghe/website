---
id: 2026-09-21-001-feedback-step-3-leave-out-need-to-design
timestamp: 2026-09-21T16:26:28+0200
model: claude-fable-5-1
files_touched:
  - theme.scss
---

Feedback: 


- Step 3: leave out, need to design.
- Step 4: the font colour for "curl" is not well chosen, improve
- Step 4.2: iTerm is a great alternative to Terminal on Mac. If you are interested in using it, get in touch.
- 4.3: that needs a manual workflow. For mac: open finder, navigate to folder, (e.g. /Documents/gitrepos/agentsforsci-ghe/rainbow). right-click folder, select "New Terminal at Folder". Terminal opens at folder. Is there an equivalent for Windows?
- Step 5.1: do not send people to the CLI releease oage. homebrew needs to be installed from: https://brew.sh/ using that line on the page
- 5.2: remove the terminal way. Add a note, that people not using RStudio should use their preferred method. 
- 6: Generally, somewhere here in setup instructions, it needs to tell people that use of RStudio, R and Quarto are that I can expect, as it was taught, however people are welcome to use other IDEs (e.g. Positron, VS Code) and languages (Python, JavaScript, STATA do files), I only cannot ensure that the setup works the same way (see setup of mcptools for R)
- 6.1 Needs a bit more instruction. Open RStudio IDE, locate Console (bottom left window), type install.packages()...
- 6.2 More detail, open the Terminal App, copy and run 
- 6.3 More detail: back to RStudio, ...
- 6.4: Needs much more detail,open Restuodio. find Console, run x <- head(mtcars), check in your Environment pane (top-right window) that x shows up. In a new window open terminal at your repository (see steps in X), start Claude, then ask:  ...
- 7. Why not Zotero 10? What's different? On what to have in library: tell people to use https://www.semanticscholar.org/ and or https://www.connectedpapers.com/ to quickly get 5 to 10 references related to their data. It's good experimentation on it's own and it doesn't matter if it's the best referecnes for what we work with. Remember, everything can be reverted or started from scratch after what you leaerned. 
- 8.2: this doesn0t work yet
- 8.3: needs more detail, but 8.2 fix first.
- Step 9. Needs more rework from me. I don't want people to interact with their data yet. Maybe I need to prepare a setup repo for them first where they can test their setup after cloning it.


