# PyFlashBackup

PyFlashBackup is a user-friendly cross-platform application designed to automate USB Flash drive backups whenever a drive is connected to your computer.

![GitHub release (latest by date)](https://img.shields.io/github/v/release/schubarkrsk/PyFlashBackup)
![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)

## Where Backups Are Stored
- **Windows:** `C:\Users\Your_username\flashbackup\`
- **UNIX:** `~/flashbackup/`

## Building Variants
You can build two variants of the application:
- **Normal:** `pyinstaller -F pyflashbackup.py`
- **Silent:** `pyinstaller -F --noconsole pyflashbackup.py`

Additionally, project tools are available for easy building:
- **For Windows:** `build.bat`
- **For UNIX:** `build.sh`

## Requirements
- Python 3.9 or higher
- psutil 5.9.7 or higher

## Getting Started
1. Download the latest release [here](https://github.com/schubarkrsk/PyFlashBackup/releases).
2. Choose the appropriate build variant based on your preferences.
3. Run the installer for the silent client (`pyflashbackup_install.exe`) for an effortless setup.

## Community and Support
Join the conversation on [GitHub Discussions](https://github.com/schubarkrsk/PyFlashBackup/discussions) to connect with other users, ask questions, and share your PyFlashBackup experiences.

## Feedback and Contributions
We welcome your feedback and contributions. If you encounter any issues or have suggestions for improvement, please open an [issue](https://github.com/schubarkrsk/PyFlashBackup/issues) on GitHub.

Thank you for choosing PyFlashBackup! We are committed to making data backups easy and efficient for you.