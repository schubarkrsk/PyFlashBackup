# Copyright 2023 Stanislav Chubar (as known as schubar or schubarkrsk)
# This code licensed under Apache 2.0
# Code provide "AS IS" without any warranty


import os
import shutil
import time
import psutil
import pathlib

USER_HOME = pathlib.Path.home()
APP_HOME = pathlib.Path(USER_HOME, "flashbackup")

if not os.path.exists(APP_HOME):
    os.makedirs(APP_HOME)


def backup_flash_drive(source_path, destination_path):
    try:
        shutil.copytree(source_path, destination_path)
        print(f"Backup successfully created! Dest: {destination_path}")
    except Exception as e:
        print(f"ERROR | Oh no, we have a error...: {e}")


def detect_flash_drive():
    drives = psutil.disk_partitions()

    for drive in drives:
        if 'removable' in drive.opts:
            return drive.device
    return None


def main():
    backup_folder = APP_HOME

    while True:
        flash_drive = detect_flash_drive()

        if flash_drive:
            timestamp = time.strftime("%Y%m%d%H%M%S")
            backup_path = os.path.join(backup_folder, f"Backup_{timestamp}")

            backup_flash_drive(flash_drive, backup_path)

            while detect_flash_drive() == flash_drive:
                time.sleep(1)
                print("Waiting for USB device...")


if __name__ == "__main__":
    main()
