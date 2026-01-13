-- Convert HTML <img> tags to Pandoc Markdown images

local function parse_style(style)
  if not style then return nil end
  local zoom = style:match("zoom:%s*([%d%.]+)%%")
  if zoom then
    return zoom .. "%"
  end
  return nil
end

local function parse_img(html)
  local src = html:match('src="([^"]+)"')
  local alt = html:match('alt="([^"]*)"') or ""
  local style = html:match('style="([^"]+)"')

  if not src then
    return nil
  end

  local width = parse_style(style)

  local attr = {}
  if width then
    attr = pandoc.Attr("", {}, { { "width", width } })
  else
    attr = pandoc.Attr()
  end

  return pandoc.Image({ pandoc.Str(alt) }, src, "", attr)
end

function RawInline(el)
  if el.format == "html" and el.text:match("^%s*<img") then
    return parse_img(el.text)
  end
end

function RawBlock(el)
  if el.format == "html" and el.text:match("^%s*<img") then
    return pandoc.Para({ parse_img(el.text) })
  end
end
