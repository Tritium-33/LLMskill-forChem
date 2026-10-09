@echo off
setlocal
cd /d "%~dp0"
py -3 -c "import sys; sys.exit(sys.version_info < (3, 10))" >nul 2>&1
if not errorlevel 1 goto use_launcher
python -c "import sys; sys.exit(sys.version_info < (3, 10))" >nul 2>&1
if not errorlevel 1 goto use_python
echo Python 3.10 or newer is required. See README.md.
pause
exit /b 1
:use_launcher
py -3 install.py
goto finish
:use_python
python install.py
:finish
if errorlevel 1 (
  echo Installation stopped. Read the message above and README.md.
) else (
  echo Open the Codex Plugins screen, install the personal plugin, then start a new chat.
)
pause
