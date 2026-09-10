# vscode-lab-themes

Two small VS Code extensions for a multi-root workspace where each root deserves its own look: a theme that follows the folder you are working in, and a Quiet Light theme family with one accent per root.

No admin rights are needed anywhere. VS Code installs extensions into your own profile (`%USERPROFILE%\.vscode\extensions`), and everything here is plain JSON and a 30-line script.

## Install (prebuilt, no admin)

Option A, PowerShell:

```powershell
git clone https://github.com/benys2077/vscode-lab-themes
cd vscode-lab-themes
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

Option B, inside VS Code: Extensions view, the `...` menu, "Install from VSIX", pick the two files in `dist/`.

Then reload the window.

## Configure for your own folder structure

Everything is set in your `.code-workspace` file (File, Save Workspace As if it is untitled). The keys are the root folder display names, exactly as they appear in the Explorer:

```json
{
  "folders": [
    { "path": "C:/work/my-app", "name": "LOCAL  my-app" },
    { "path": "\\fileserver\dev", "name": "DEV  fileserver" },
    { "path": "\\fileserver\prod", "name": "PROD  fileserver" }
  ],
  "settings": {
    "workbench.colorTheme": "Quiet Light (local)",
    "folderTheme.map": {
      "LOCAL  my-app": "Quiet Light (local)",
      "DEV  fileserver": "Quiet Light svc-dev",
      "PROD  fileserver": "Quiet Light svc-prod"
    }
  }
}
```

Any installed theme name works as a value, not only the ones shipped here. The switch happens when the active editor moves into a file under a different root (VS Code does not tell extensions about folder clicks). The theme is written at workspace scope, so your user settings are never modified.

`example.code-workspace` is a fuller sample: Material Icon Theme root and folder icon associations (so git checkouts and deploy folders get distinct icons) and per-host SSH terminal profiles.

## The themes

- `Quiet Light (local)`: the bundled Quiet Light, unchanged.
- `Quiet Light svc-dev` (blue), `Quiet Light svc-prod` (red), `Quiet Light dev-ubuntu` (green): light pastel frame (title bar, activity bar, status bar) with dark text, and the sidebar, tab strip, panel, selections, cursor, scrollbars and git decorations follow the accent. Syntax moves off Quiet Light's greens and purples: keywords, types and tags take the accent family, strings and numbers go warm neutral, comments stay grey italic.

Rename or recolour by editing `extensions/quiet-light-lab/themes/*.json` (the three variants are generated from five colours each: light, mid, deep, tint, wash).

## Build from source

```bash
cd extensions/quiet-light-lab && npx @vscode/vsce package --allow-missing-repository --skip-license -o ../../dist/quiet-light-lab-0.0.1.vsix
cd ../folder-theme && npx @vscode/vsce package --allow-missing-repository --skip-license -o ../../dist/folder-theme-0.0.1.vsix
```

`npx` fetches vsce on demand; nothing is installed globally.
