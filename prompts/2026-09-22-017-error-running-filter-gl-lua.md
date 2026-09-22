---
id: 2026-09-22-017-error-running-filter-gl-lua
timestamp: 2026-09-22T08:58:42+0200
model: claude-fable-5-1
files_touched:
  - _brand.yml
  - _extensions/ghe/gl/_extension.yml
  - _extensions/ghe/gl/gl.css
  - _extensions/ghe/gl/gl.js
  - _extensions/ghe/gl/gl.lua
  - _quarto.yml
  - background/disclosure.qmd
  - background/literacy.qmd
  - background/security.qmd
  - background/transparency.qmd
  - docs/background/disclosure.html
  - docs/background/index.html
  - docs/background/literacy.html
  - docs/background/security.html
  - docs/background/transparency.html
  - docs/glossary.html
  - docs/index.html
  - docs/platform-guide.html
  - docs/pre-work/01-create-repository.html
  - docs/pre-work/02-join-element.html
  - docs/pre-work/03-survey.html
  - docs/pre-work/04-install-claude-code.html
  - docs/pre-work/05-github-cli.html
  - docs/pre-work/06-connect-r.html
  - docs/pre-work/07-zotero.html
  - docs/pre-work/08-zotero-mcp.html
  - docs/pre-work/09-setup-check.html
  - docs/pre-work/index.html
  - docs/references.html
  - docs/search.json
  - docs/site_libs/bootstrap/bootstrap-944cc49a1fd5d2d7222c95398737996b.min.css
  - docs/site_libs/bootstrap/bootstrap-ad4e323ce240e5abdcb06c1e9cf2b809.min.css
  - docs/site_libs/bootstrap/bootstrap-dark-944cc49a1fd5d2d7222c95398737996b.min.css
  - docs/site_libs/bootstrap/bootstrap-dark-ad4e323ce240e5abdcb06c1e9cf2b809.min.css
  - docs/site_libs/quarto-contrib/gl-1.0.0/gl.css
  - docs/site_libs/quarto-contrib/gl-1.0.0/gl.js
  - docs/sitemap.xml
  - glossary.qmd
  - glossary.yml
  - index.qmd
  - platform-guide.qmd
  - pre-work/01-create-repository.qmd
  - pre-work/02-join-element.qmd
  - pre-work/03-survey.qmd
  - pre-work/04-install-claude-code.qmd
  - pre-work/05-github-cli.qmd
  - pre-work/06-connect-r.qmd
  - pre-work/07-zotero.qmd
  - pre-work/08-zotero-mcp.qmd
  - pre-work/09-setup-check.qmd
  - pre-work/index.qmd
  - theme.scss
  - tools/build_glossary.py
  - tools/mark_glossary_terms.py
---

Error running filter '/Applications/Positron.app/Contents/Resources/app/quarto/share/filters/main.lua':
string expected, got nil
        while retrieving index 1
        while retrieving list
        while retrieving function argument filepaths
        while retrieving arguments for function join
stack traceback:
        ...h-org-agentsforsci-ghe/website/_extensions/ghe/gl/gl.lua:16: in upvalue 'load_glossary'
        ...h-org-agentsforsci-ghe/website/_extensions/ghe/gl/gl.lua:67: in function <...h-org-agentsforsci-ghe/website/_extensions/ghe/gl/gl.lua:56>
        (...tail calls...)
        [string "if pandoc.system.os == "mingw32" then..."]:778: in function <[string "if pandoc.system.os == "mingw32" then..."]:776>
        (...tail calls...)
        ...app/Contents/Resources/app/quarto/share/filters/main.lua:21758: in upvalue 'handle_shortcode'
        ...app/Contents/Resources/app/quarto/share/filters/main.lua:21828: in local 'filter_fn'
        ...app/Contents/Resources/app/quarto/share/filters/main.lua:656: in function <...app/Contents/Resources/app/quarto/share/filters/main.lua:646>
        (...tail calls...)
        [C]: in ?
        [C]: in method 'walk'
        ...nts/Resources/app/quarto/share/pandoc/datadir/_utils.lua:607: in function '_utils.walk'
        ...app/Contents/Resources/app/quarto/share/filters/main.lua:575: in function <...app/Contents/Resources/app/quarto/share/filters/main.lua:553>
        (...tail calls...)
        ...app/Contents/Resources/app/quarto/share/filters/main.lua:21883: in field 'Pandoc'
        ...app/Contents/Resources/app/quarto/share/filters/main.lua:589: in function 'run_emulated_filter'
        ...app/Contents/Resources/app/quarto/share/filters/main.lua:1318: in local 'callback'
        ...app/Contents/Resources/app/quarto/share/filters/main.lua:1336: in upvalue 'run_emulated_filter_chain'
        ...app/Contents/Resources/app/quarto/share/filters/main.lua:1372: in function <...app/Contents/Resources/app/quarto/share/filters/main.lua:1369>
stack traceback:
        ...nts/Resources/app/quarto/share/pandoc/datadir/_utils.lua:607: in function '_utils.walk'
        ...app/Contents/Resources/app/quarto/share/filters/main.lua:575: in function <...app/Contents/Resources/app/quarto/share/filters/main.lua:553>
        (...tail calls...)
        ...app/Contents/Resources/app/quarto/share/filters/main.lua:21883: in field 'Pandoc'
        ...app/Contents/Resources/app/quarto/share/filters/main.lua:589: in function 'run_emulated_filter'
        ...app/Contents/Resources/app/quarto/share/filters/main.lua:1318: in local 'callback'
        ...app/Contents/Resources/app/quarto/share/filters/main.lua:1336: in upvalue 'run_emulated_filter_chain'
        ...app/Contents/Resources/app/quarto/share/filters/main.lua:1372: in function <...app/Contents/Resources/app/quarto/share/filters/main.lua:1369>
WARN: Error encountered when rendering files
