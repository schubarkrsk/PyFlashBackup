#!/bin/bash

echo "Wellcome to PyFlashBackup easy build tool!"
echo "Before using you need install pyinstaller"
echo "You can build two variants of PyFlashBackup"
echo "[1] - Normal - You can see console and app logs"
echo "[2] - Silent - App run in background"
read -p "Now please select which variant you need : " build_choise

if [ "$build_choise" = "1" ]; then
  pyinstaller -F pyflashbackup.py
elif [ "$build_choise" = "2" ]; then
  pyinstaller -F --noconsole pyflashbackup.py
else
  echo "Incorrect choise!"
  exit 1
fi

echo "Build finished! You can find it in dist folder"
read -p "Press Enter to exit"
