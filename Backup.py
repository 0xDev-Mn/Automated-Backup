import os
import shutil
import datetime
import time
import schedule

source_dir = "/home/bat-man/Pictures/profile-images"
destination_dir = "/home/bat-man/backup"

def backup(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try: 
        shutil.copytree(source, dest_dir)
        print(f"Folder backed up to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already backed up in: {dest}")

# schedule.every().day.at("12:05").do(lambda: backup(source_dir, destination_dir))

# while True:
#     schedule.run_pending()
#     time.sleep(60)

backup(source_dir, destination_dir)