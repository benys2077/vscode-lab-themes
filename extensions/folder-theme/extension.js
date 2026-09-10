// Folder Theme: apply the theme mapped to the workspace root of the active editor,
// with a light/dark mode toggle. Map values are either a theme name or {light, dark}.
const vscode = require('vscode');

let status;

function cfg() { return vscode.workspace.getConfiguration('folderTheme'); }
function mode() { return cfg().get('mode') || 'light'; }

function themeFor(folderName) {
  const entry = (cfg().get('map') || {})[folderName];
  if (!entry) return null;
  if (typeof entry === 'string') return entry;
  return entry[mode()] || entry.light || entry.dark || null;
}

function currentFolder() {
  const editor = vscode.window.activeTextEditor;
  const folders = vscode.workspace.workspaceFolders || [];
  if (editor) {
    const f = vscode.workspace.getWorkspaceFolder(editor.document.uri);
    if (f) return f.name;
  }
  return folders.length ? folders[0].name : null;
}

async function apply() {
  const name = currentFolder();
  const theme = name ? themeFor(name) : null;
  if (theme && vscode.workspace.getConfiguration('workbench').get('colorTheme') !== theme) {
    // Workspace scope only: user settings are never touched.
    await vscode.workspace.getConfiguration('workbench').update('colorTheme', theme, vscode.ConfigurationTarget.Workspace);
  }
  if (status) {
    status.text = mode() === 'dark' ? '$(color-mode) Dark' : '$(color-mode) Light';
    status.tooltip = 'Folder Theme: click to flip light/dark for this workspace';
    status.show();
  }
}

async function toggle() {
  const next = mode() === 'dark' ? 'light' : 'dark';
  await cfg().update('mode', next, vscode.ConfigurationTarget.Workspace);
  await apply();
}

function activate(context) {
  status = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Right, 200);
  status.command = 'folderTheme.toggle';
  context.subscriptions.push(
    status,
    vscode.commands.registerCommand('folderTheme.toggle', toggle),
    vscode.window.onDidChangeActiveTextEditor(apply),
    vscode.workspace.onDidChangeConfiguration((e) => { if (e.affectsConfiguration('folderTheme')) apply(); }),
  );
  apply();
}

module.exports = { activate, deactivate() {} };
