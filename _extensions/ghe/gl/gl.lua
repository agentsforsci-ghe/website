-- gl: glossary term with a popover definition and a link to the full entry.
--
--   {{< gl agent >}}                      shows "agent"
--   {{< gl agent display="agents" >}}     shows "agents", defines "agent"
--
-- Definitions come from glossary.yml at the project root, generated from
-- glossary.qmd by tools/build_glossary.py before every render. Hover or
-- keyboard focus opens a Bootstrap popover with the plain definition; a
-- click follows the link to the entry on the glossary page.

local glossary = nil
local root = nil      -- directory that holds glossary.yml
local offset = nil    -- relative path from the document to that directory

-- Inside a project render Quarto tells us where the project is. A single
-- file render or preview from an editor does not, so walk up from the
-- document until glossary.yml is found.
local function find_root()
  if root ~= nil then return root, offset end
  if quarto.project ~= nil and quarto.project.directory ~= nil then
    root, offset = quarto.project.directory, quarto.project.offset or "."
    return root, offset
  end
  local dir = pandoc.path.directory(quarto.doc.input_file)
  local rel = "."
  for _ = 1, 8 do
    local f = io.open(pandoc.path.join({dir, "glossary.yml"}), "r")
    if f then
      f:close()
      root, offset = dir, rel
      return root, offset
    end
    local parent = pandoc.path.directory(dir)
    if parent == dir then break end
    dir = parent
    rel = (rel == ".") and ".." or (rel .. "/..")
  end
  return nil, nil
end

local function load_glossary()
  if glossary ~= nil then return glossary end
  glossary = {}
  local dir = find_root()
  if dir == nil then
    quarto.log.warning("gl: glossary.yml not found above " .. tostring(quarto.doc.input_file))
    return glossary
  end
  local path = pandoc.path.join({dir, "glossary.yml"})
  local f = io.open(path, "r")
  if not f then
    quarto.log.warning("gl: cannot open " .. path)
    return glossary
  end
  local content = "---\n" .. f:read("*a") .. "\n---\n"
  f:close()
  local meta = pandoc.read(content, "markdown").meta
  for key, value in pairs(meta) do
    glossary[string.lower(key)] = value
  end
  return glossary
end

local function to_html(value)
  local doc
  if value.t == "MetaBlocks" then
    doc = pandoc.Pandoc(value)
  elseif value.t == "MetaInlines" then
    doc = pandoc.Pandoc({pandoc.Para(value)})
  else
    doc = pandoc.Pandoc({pandoc.Para({pandoc.Str(pandoc.utils.stringify(value))})})
  end
  local html = pandoc.write(doc, "html")
  return (html:gsub("%s+$", ""))
end

local function slug(term)
  local s = string.lower(term)
  s = s:gsub("[^%w]+", "-"):gsub("^%-+", ""):gsub("%-+$", "")
  return s
end

return {
  ["gl"] = function(args, kwargs, meta)
    local shown = pandoc.utils.stringify(args[1])
    local term = string.lower(shown)
    -- Quarto passes an absent keyword as an empty Inlines list, not as nil.
    if kwargs.display ~= nil then
      local d = pandoc.utils.stringify(kwargs.display)
      if d ~= "" then shown = d end
    end

    if not quarto.doc.isFormat("html:js") then
      return pandoc.Str(shown)
    end

    local g = load_glossary()
    local entry = g[term]
    if entry == nil then
      quarto.log.warning("gl: no glossary entry for '" .. term .. "'")
      return pandoc.Str(shown)
    end

    quarto.doc.add_html_dependency({
      name = "gl",
      version = "1.0.0",
      stylesheets = {"gl.css"},
      scripts = {"gl.js"}
    })

    local key = term
    if entry.t == "MetaMap" then
      -- alias entry: {alias: true, of: "canonical term"}
      key = string.lower(pandoc.utils.stringify(entry.of))
      entry = g[key]
    end

    local _, rel = find_root()
    local href = pandoc.path.join({rel or ".", "glossary.html"}) .. "#gl-" .. slug(key)
    -- A native Link renders correctly in every block context (a raw HTML
    -- inline came out empty inside tight list items) and Pandoc escapes the
    -- attribute values itself.
    local attr = pandoc.Attr("", {"gl"}, {
      ["data-bs-toggle"] = "popover",
      ["data-bs-trigger"] = "hover focus",
      ["data-bs-html"] = "true",
      ["data-bs-placement"] = "top",
      ["data-bs-title"] = key,
      ["data-bs-content"] = to_html(entry)
    })
    return pandoc.Link({pandoc.Str(shown)}, href, "", attr)
  end
}
