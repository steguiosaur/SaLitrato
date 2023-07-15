from tkinter import filedialog
import csv
import os

from pytesseract import image_to_string
from PIL import Image

from .assets import Assets
from .boyer import get_matched_positions

DATA_FOLDER = "data"
FOLDER_PATH = os.path.join(os.getcwd(), DATA_FOLDER)
SUPPORTED_FORMATS = {'.png', '.jpg', '.jpeg', '.jiff', '.pjpeg', '.pjp', '.jp2', '.tiff', '.gif', '.webp', '.bmp', '.pnm'}
filetypes = (
    ("Image files", "*.png;*.jpeg,;*.jpg"),
    ("Other Image Files", "*.jiff;*.pjpeg;*.pjp;*.jp2;*.tiff;*.webp;*.bmp;*.pnm"),
    ("All Files", "*.*")
)

def convert_to_text(current_dir, image_file, image_file_path):
    output_path = os.path.join(FOLDER_PATH, current_dir, image_file)
    with open(output_path + ".txt", "w") as f:
        f.write(image_to_string(Image.open(image_file_path)))

def read_csv(csv_path):
    return list(csv.DictReader(open(csv_path, "r"))) if os.path.exists(csv_path) else []

def write_csv(csv_path, data):
    with open(csv_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["file_key", "file_path", "file_name"], quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(data)

def get_path_image(current_folder):
    if current_folder is None:
        return

    file_path = filedialog.askopenfilename(filetypes=filetypes)
    if not file_path:
        return

    subfolder_path = os.path.join(FOLDER_PATH, current_folder)
    csv_path = os.path.join(subfolder_path, current_folder + ".csv")

    selected_file_path = file_path
    selected_file_name = os.path.basename(file_path)
    file_extension = os.path.splitext(selected_file_name)[1]

    if file_extension.lower() not in SUPPORTED_FORMATS:
        print("Unsupported file format.")
        return

    data = read_csv(csv_path)
    existing_file_names = [item['file_name'] for item in data]
    if selected_file_name in existing_file_names:
        print("Filename already exists in the CSV file.")
        return

    file_key = str(len(data) + 1)

    file_data = {
        "file_key": file_key,
        "file_path": selected_file_path,
        "file_name": selected_file_name
    }

    data.append(file_data)
    write_csv(csv_path, data)

    convert_to_text(subfolder_path, selected_file_name, selected_file_path)

def get_all_imgfiles(current_folder):
    if current_folder is None:
        return []

    subfolder_path = os.path.join(FOLDER_PATH, current_folder)
    csv_path = os.path.join(subfolder_path, current_folder + ".csv")

    data = read_csv(csv_path)
    return [(item['file_key'], item['file_name']) for item in data]

def delete_row_by_key(current_dir, img_name):
    if current_dir is None or img_name is None:
        return

    output_path = os.path.join(FOLDER_PATH, current_dir, img_name + ".txt")
    if os.path.exists(output_path):
        os.remove(output_path)

    subfolder_path = os.path.join(FOLDER_PATH, current_dir)
    csv_path = os.path.join(subfolder_path, current_dir + ".csv")

    data = read_csv(csv_path)
    data = [row for row in data if row['file_name'] != img_name]

    write_csv(csv_path, data)

def get_file_path_from_csv(current_dir, file_name):
    if current_dir is None and file_name is None:
        return Assets.asset_path("./salitrato_icon.png")

    output_path = os.path.join(FOLDER_PATH, current_dir, file_name)
    if os.path.exists(output_path):
        os.remove(output_path)

    subfolder_path = os.path.join(FOLDER_PATH, current_dir)
    csv_path = os.path.join(subfolder_path, current_dir + ".csv")
    if subfolder_path is not None:
        with open(csv_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['file_name'] == file_name:
                    return row['file_path']
    return Assets.asset_path("./salitrato_icon.png")

def get_all_text_files(current_dir):
    subfolder_path = os.path.join(FOLDER_PATH, current_dir)
    text_dict = {}
    if os.path.exists(subfolder_path):
        for file in os.listdir(subfolder_path):
            file_path = os.path.join(subfolder_path, file)
            if os.path.isfile(file_path) and file.endswith('.txt'):
                with open(file_path, 'r') as fileprocess:
                    lines = fileprocess.readlines()
                    text_dict[file] = lines
    return text_dict


# requires relocation
def access_text_infile(array, pattern):
    for file_name, lines in array.items():
        # Process the lines of text in the file
        for line in lines:
            print(file_name + ": " + str(get_matched_positions(line, pattern)) + " " + line)
