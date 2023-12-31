import os
import shutil
import time
import psutil
import pathlib
import logging
from configparser import ConfigParser

USER_HOME = pathlib.Path.home()
APP_HOME = pathlib.Path(USER_HOME, "flashbackup")

if not os.path.exists(APP_HOME):
    os.makedirs(APP_HOME)

CONFIG_FILE = os.path.join(APP_HOME, "pfb_config.ini")

if not os.path.exists(CONFIG_FILE):
    config = ConfigParser()
    config.optionxform = str
    config["BackupConfig"] = {
        "source_path": "",
        "destination_path": str(APP_HOME),
        "exclude_files": "*.tmp, *.bak",
        "exclude_directories": "temp, cache, System Volume Information"
    }

    with open(CONFIG_FILE, "w") as config_file:
        config.write(config_file)

# Загружаем конфигурацию
config = ConfigParser()
config.optionxform = str
config.read(CONFIG_FILE)

# Получаем значения из конфигурации
source_path = config.get("BackupConfig", "source_path")
destination_path = config.get("BackupConfig", "destination_path")
exclude_files = [pattern.strip() for pattern in config.get("BackupConfig", "exclude_files").split(",")]
exclude_directories = [directory.strip() for directory in config.get("BackupConfig", "exclude_directories").split(",")]

# Настройка логирования
logging.basicConfig(filename=os.path.join(APP_HOME, "backup_log.txt"), level=logging.INFO)

# Строка формата времени для создания уникальных имен папок
backup_format = "Backup_%Y%m%d%H%M%S"


def backup_flash_drive(source_path, destination_path):
    try:
        timestamp = time.strftime(backup_format)
        backup_path = os.path.join(destination_path, timestamp)

        # Добавим игнорирование файлов и директорий
        ignore = shutil.ignore_patterns(*exclude_files, *exclude_directories)

        shutil.copytree(source_path, backup_path, ignore=ignore)
        logging.info(f"Backup successfully created! Source: {source_path}, Dest: {backup_path}")
    except shutil.Error as e:
        logging.error(f"Backup failed: {e}")
    except Exception as e:
        logging.exception(f"An unexpected error occurred: {e}")


def detect_flash_drive():
    drives = psutil.disk_partitions()

    for drive in drives:
        if 'removable' in drive.opts:
            return drive.device
    return None


def main():
    backup_folder = str(APP_HOME)

    while True:
        flash_drive = detect_flash_drive()

        if flash_drive:
            backup_flash_drive(flash_drive, destination_path)

            while detect_flash_drive() == flash_drive:
                time.sleep(1)
                logging.info("Waiting for USB device...")


if __name__ == "__main__":
    main()
