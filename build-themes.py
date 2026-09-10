"""Generate the Quiet Light accent variants. Edit PALETTES, run: py build-themes.py"""
import json, pathlib
ROOT = pathlib.Path(__file__).parent / "extensions" / "quiet-light-lab" / "themes"
# light = frame, mid = accent, deep = accent text, tint = panels, wash = selection, paper = editor background, line = current line
PALETTES = {
  "quiet-light-svc-dev.json":    ("Quiet Light svc-dev",    dict(light="#a8c8ec", mid="#5b8fd6", deep="#2f5fa8", tint="#e3edf9", wash="#c9dcf3", paper="#f3f7fc", line="#e1ecf9")),
  "quiet-light-svc-prod.json":   ("Quiet Light svc-prod",   dict(light="#f0b8b0", mid="#dc7a6c", deep="#b04638", tint="#fae7e3", wash="#f3cdc7", paper="#fcf5f3", line="#f9e3de")),
  "quiet-light-dev-ubuntu.json": ("Quiet Light dev-ubuntu", dict(light="#b7ddbd", mid="#6fb47f", deep="#3f7f4c", tint="#e6f3e8", wash="#cfe8d3", paper="#f3f9f4", line="#e1f1e4")),
}
def variant(label, p):
    light, mid, deep, tint, wash, paper, line = (p[k] for k in ("light", "mid", "deep", "tint", "wash", "paper", "line"))
    colors = {
      "focusBorder": mid,
      "titleBar.activeBackground": light, "titleBar.activeForeground": "#1f1f1f", "titleBar.inactiveBackground": tint, "titleBar.inactiveForeground": "#1f1f1f99",
      "activityBar.background": light, "activityBar.foreground": "#1f1f1f", "activityBar.inactiveForeground": "#1f1f1f88", "activityBar.activeBorder": deep,
      "activityBarBadge.background": deep, "activityBarBadge.foreground": "#ffffff",
      "sideBar.background": tint, "sideBar.foreground": "#2b2b2b", "sideBarTitle.foreground": deep, "sideBarSectionHeader.background": wash, "sideBarSectionHeader.foreground": deep,
      "statusBar.background": light, "statusBar.foreground": "#1f1f1f", "statusBarItem.hoverBackground": mid, "statusBarItem.remoteBackground": mid, "statusBarItem.remoteForeground": "#ffffff", "statusBar.debuggingBackground": deep,
      "editorGroupHeader.tabsBackground": tint, "editorGroup.border": light, "tab.activeBorderTop": deep, "tab.inactiveBackground": tint, "tab.activeBackground": paper, "tab.activeForeground": "#1f1f1f", "tab.border": light,
      "breadcrumb.background": paper, "breadcrumb.foreground": "#4a4a4a", "breadcrumb.focusForeground": deep, "breadcrumb.activeSelectionForeground": deep,
      "panel.background": tint, "panel.border": light, "panelTitle.activeBorder": deep, "panelTitle.activeForeground": deep,
      "list.activeSelectionBackground": wash, "list.activeSelectionForeground": "#1f1f1f", "list.inactiveSelectionBackground": tint, "list.hoverBackground": wash + "80", "list.highlightForeground": deep,
      "button.background": mid, "button.foreground": "#ffffff", "button.hoverBackground": deep, "badge.background": mid, "badge.foreground": "#ffffff",
      "progressBar.background": mid, "textLink.foreground": deep, "textLink.activeForeground": mid,
      # editor surface
      "editor.background": paper, "editorGutter.background": paper, "minimap.background": paper, "editorPane.background": paper,
      "editor.lineHighlightBackground": line, "editor.lineHighlightBorder": line,
      "editor.selectionBackground": wash, "editor.inactiveSelectionBackground": tint, "editor.selectionHighlightBackground": tint,
      "editor.wordHighlightBackground": tint, "editor.wordHighlightStrongBackground": wash,
      "editor.findMatchBackground": light, "editor.findMatchHighlightBackground": wash,
      "editorBracketMatch.background": wash, "editorBracketMatch.border": mid,
      "editorCursor.foreground": deep, "editorLineNumber.foreground": "#9a9a9a", "editorLineNumber.activeForeground": deep,
      "editorIndentGuide.background1": tint, "editorIndentGuide.activeBackground1": light, "editorWhitespace.foreground": tint,
      "editorRuler.foreground": tint, "editorCodeLens.foreground": mid, "editorLink.activeForeground": deep,
      "editorOverviewRuler.border": light, "editorHoverWidget.background": tint, "editorHoverWidget.border": light,
      "editorSuggestWidget.background": paper, "editorSuggestWidget.border": light, "editorSuggestWidget.selectedBackground": wash,
      "scrollbarSlider.background": tint, "scrollbarSlider.hoverBackground": wash, "scrollbarSlider.activeBackground": light,
      "minimap.selectionHighlight": wash, "minimapSlider.background": tint + "80",
      "editorWidget.background": tint, "editorWidget.border": light, "input.background": "#ffffff", "input.border": light, "inputOption.activeBorder": deep, "dropdown.border": light,
      "editorGutter.modifiedBackground": mid, "editorGutter.addedBackground": mid, "gitDecoration.modifiedResourceForeground": deep, "sash.hoverBorder": mid,
      "terminal.background": paper, "terminal.selectionBackground": wash, "terminalCursor.foreground": deep,
      "peekView.border": mid, "peekViewEditor.background": tint, "notificationCenterHeader.background": light, "notifications.background": tint,
      "pickerGroup.foreground": deep, "quickInput.background": paper, "quickInputList.focusBackground": wash,
      "menu.background": paper, "menu.selectionBackground": wash, "menu.selectionForeground": "#1f1f1f",
    }
    tokens = [
      {"scope": ["keyword", "storage", "storage.type", "keyword.control", "keyword.operator.new"], "settings": {"foreground": deep}},
      {"scope": ["entity.name.function", "support.function", "meta.function-call entity.name.function"], "settings": {"foreground": mid}},
      {"scope": ["entity.name.type", "entity.name.class", "support.type", "support.class"], "settings": {"foreground": deep, "fontStyle": "bold"}},
      {"scope": ["string", "string.quoted"], "settings": {"foreground": "#6b5a3a"}},
      {"scope": ["constant.numeric", "constant.language", "constant.character"], "settings": {"foreground": "#8a5a1e"}},
      {"scope": ["variable", "variable.other", "variable.parameter"], "settings": {"foreground": "#2b2b2b"}},
      {"scope": ["entity.name.tag", "punctuation.definition.tag"], "settings": {"foreground": deep}},
      {"scope": ["entity.other.attribute-name"], "settings": {"foreground": mid}},
      {"scope": ["comment", "punctuation.definition.comment"], "settings": {"foreground": "#8a8a82", "fontStyle": "italic"}},
      {"scope": ["markup.heading", "entity.name.section"], "settings": {"foreground": deep, "fontStyle": "bold"}},
      {"scope": ["markup.bold"], "settings": {"fontStyle": "bold"}},
    ]
    return {"name": label, "type": "light", "include": "./quiet-light-base.json", "colors": colors, "tokenColors": tokens}
for f, (label, pal) in PALETTES.items():
    (ROOT / f).write_text(json.dumps(variant(label, pal), indent=2) + "\n", encoding="utf-8")
print("wrote", len(PALETTES), "variants")
