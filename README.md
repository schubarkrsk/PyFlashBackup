# PyFlashBackup

PyFlashBackup is a simple cross-platform application which can help to automatically create USB Flash drive backups on
it's connected to computer

### Where backups located?
* Windows - `C:\Users\Your_username\flashbackup\`
* UNIX - `~/flashbackup/`

### You can build two variants of application
* Normal - `pyinstaller -F pyflashbackup.py`
* Silent - `pyinstaller -F --noconsole pyflashbackup.py`

#### Also you can use project's tools to simply build application
* For Windows - `build.bat`
* For UNIX - `build.sh`

### Requirements
* Python 3.9 or higher
* psutil 5.9.7 or higher