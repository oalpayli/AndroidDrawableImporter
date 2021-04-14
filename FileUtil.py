import os
import shutil


def move_all_files_to_dest(entry_path, dest_path):
    for sub_entry in os.listdir(entry_path):
        try:
            shutil.move(entry_path + "/" + sub_entry, dest_path)
        except FileNotFoundError as ex:
            print(ex)
        finally:
            continue
