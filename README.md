# vscode-lab-themes

Two small VS Code extensions for a multi-root workspace that spans a local checkout and several lab hosts mounted as drives.

## folder-theme

Switches the colour theme to match the workspace root that the active editor belongs to. VS Code only supports one theme per window, so this is the missing piece for "different look per folder". Configure a map from root display name to theme name in the workspace file:

```json
"folderTheme.map": {
  "LOCAL  workstation": "Quiet Light (local)",
  "S:  svc-dev": "Quiet Light svc-dev",
  "P:  svc-prod": "Quiet Light svc-prod",
  "U:  dev-ubuntu": "Quiet Light dev-ubuntu"
}
```

The theme is written at workspace scope, so user settings are never touched. It fires on editor changes (VS Code does not expose folder selection to extensions).

## quiet-light-lab

Four colour themes built on the bundled Quiet Light: an unchanged `Quiet Light (local)` and three variants that recolour only the frame (title bar, activity bar, status bar, buttons, cursor, tab marker) with a blue, red or green accent, leaving the editor and syntax colours alone.

## Install

```bash
cd extensions/quiet-light-lab && npx @vscode/vsce package --allow-missing-repository --skip-license && code --install-extension *.vsix
cd ../folder-theme && npx @vscode/vsce package --allow-missing-repository --skip-license && code --install-extension *.vsix
```

`example.code-workspace` shows the settings that tie the two together, including Material Icon Theme root and folder icon associations and SSH terminal profiles per host.
