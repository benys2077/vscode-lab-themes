# Installs both extensions into the current user's VS Code profile. No admin rights needed:
# VS Code extensions always live under %USERPROFILE%\.vscode\extensions.
# Usage: powershell -ExecutionPolicy Bypass -File .\install.ps1
$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$code = Get-Command code -ErrorAction SilentlyContinue
if (-not $code) {
  $candidates = @("$env:LOCALAPPDATA\Programs\Microsoft VS Code\bin\code.cmd", "$env:ProgramFiles\Microsoft VS Code\bin\code.cmd")
  $found = $candidates | Where-Object { Test-Path $_ } | Select-Object -First 1
  if (-not $found) { throw "VS Code 'code' command not found. Open VS Code, run 'Shell Command: Install code command', or install from the VSIX via Extensions > ... > Install from VSIX." }
  $code = $found
} else { $code = $code.Source }
Get-ChildItem (Join-Path $here 'dist') -Filter *.vsix | ForEach-Object {
  Write-Host "installing $($_.Name)"
  & $code --install-extension $_.FullName --force | Out-Null
}
Write-Host "done. Reload VS Code, then pick 'Quiet Light (local)' or a variant, and set folderTheme.map in your .code-workspace."
