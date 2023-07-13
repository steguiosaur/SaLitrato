import os
import shutil

DATA_FOLDER = "data"
FOLDER_PATH = os.path.join(os.getcwd(), DATA_FOLDER)

def create_data_folder():
    if not os.path.exists(FOLDER_PATH):
        os.makedirs(FOLDER_PATH)
        return 0

def create_subfolder(subfolder_name):
    subfolder_path = os.path.join(FOLDER_PATH, subfolder_name)

    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
        return 0
    return 1

def delete_subfolder(subfolder_name):
    subfolder_path = os.path.join(FOLDER_PATH, subfolder_name)

    if os.path.exists(subfolder_path):
        shutil.rmtree(subfolder_path)
        return 0
    return 1

def get_folders():
    if os.path.exists(FOLDER_PATH):
        folders = [name for name in os.listdir(FOLDER_PATH) if os.path.isdir(os.path.join(FOLDER_PATH, name))]
        return folders
    return []
