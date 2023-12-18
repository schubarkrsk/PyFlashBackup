@echo off

echo Welcome to PyFlashBackup easy build tool!
echo Before using, you need to install pyinstaller
echo You can build two variants of PyFlashBackup
echo [1] - Normal - You can see console and app logs
echo [2] - Silent - App runs in the background
set /p build_choice=Now please select which variant you need:

if "%build_choice%"=="1" (
  pyinstaller -F pyflashbackup.py
) elif "%build_choice%"=="2" (
  pyinstaller -F --noconsole pyflashbackup.py
) else (
  echo Incorrect choice!
  exit /b 1
)

echo Build finished! You can find it in the dist folder
pause
