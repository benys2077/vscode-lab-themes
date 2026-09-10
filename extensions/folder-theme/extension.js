// Folder Theme: when the active editor moves between workspace roots, apply that root's theme.
// The map lives in the workspace settings (folderTheme.map), keyed by the root's display name.
const vscode = require('vscode');

let last = null;

function apply(editor) {
  if (!editor) return;
  const folder = vscode.workspace.getWorkspaceFolder(editor.document.uri);
  if (!folder) return;
  const map = vscode.workspace.getConfiguration('folderTheme').get('map') || {};
  const theme = map[folder.name];
  if (!theme || theme === last) return;
  last = theme;
  // Workspace scope so the choice stays inside this .code-workspace and never touches user settings.
  vscode.workspace.getConfiguration('workbench').update('colorTheme', theme, vscode.ConfigurationTarget.Workspace);
}

function activate(context) {
  context.subscriptions.push(vscode.window.onDidChangeActiveTextEditor(apply));
  apply(vscode.window.activeTextEditor);
}

module.exports = { activate, deactivate() {} };
