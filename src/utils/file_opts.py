from tkinter import filedialog
import csv
import os

from pytesseract import image_to_string
from PIL import Image

DATA_FOLDER = "data"
FOLDER_PATH = os.path.join(os.getcwd(), DATA_FOLDER)
SUPPORTED_FORMATS = {'.png', '.jpg', '.jpeg', '.jiff', '.pjpeg', '.pjp', '.jp2', '.tiff', '.gif', '.webp', '.bmp', '.pnm'}
filetypes = (
    ("Image files", "*.png"),
    ("Other Image Files", "*.jiff;*.pjpeg;*.pjp;*.jp2;*.tiff;*.webp;*.bmp;*.pnm"),
    ("All Files", "*.*")
)

def convert_to_text(current_dir, image_file, image_file_path):
    output_path = os.path.join(FOLDER_PATH, current_dir, image_file)
    with open(output_path + ".txt", mode="w") as f:
        f.write(image_to_string(Image.open(image_file_path)))

def get_path_image(current_folder):
    if current_folder is None:
        return
    file_path = filedialog.askopenfilename(filetypes=filetypes)
    if not file_path:
        return
    subfolder_path = os.path.join(FOLDER_PATH, current_folder)
    csv_path = os.path.join(subfolder_path, current_folder + ".csv")

    # Extract the file path and name
    selected_file_path = file_path
    selected_file_name = os.path.basename(file_path)
    file_extension = os.path.splitext(selected_file_name)[1]

    # Check if the selected file has a supported format
    if file_extension.lower() not in SUPPORTED_FORMATS:
        print("Unsupported file format.")
        return

    # Check if the CSV file already exists
    if os.path.exists(csv_path):
        # Load existing data from the CSV file
        with open(csv_path, 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)
    else:
        # Start with an empty data list
        data = []

    # Check if the file path already exists in the data
    existing_file_paths = [item['file_path'] for item in data]
    if selected_file_path in existing_file_paths:
        print("File path already exists in the CSV file.")
        return

    # Generate a unique key for the new file
    file_key = str(len(data) + 1)

    # Create a dictionary with the file path and name
    file_data = {
        "file_key": file_key,
        "file_path": selected_file_path,
        "file_name": selected_file_name
    }

    # Add the file data to the list
    data.append(file_data)

    # Save the list to the CSV file with quoting option
    with open(csv_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["file_key", "file_path", "file_name"], quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(data)

    convert_to_text(subfolder_path, selected_file_name, selected_file_path)


def get_all_imgfiles(current_folder):
    if current_folder is None:
        return []
    subfolder_path = os.path.join(FOLDER_PATH, current_folder)
    csv_path = os.path.join(subfolder_path, current_folder + ".csv")

    if os.path.exists(csv_path):
        # Load existing data from the CSV file
        with open(csv_path, 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)
    else:
        data = []

    # Create an array to store the file data
    file_data_array = []

    # Extract the file key and file name from each file data
    for file_data in data:
        file_key = file_data['file_key']
        file_name = file_data['file_name']
        file_data_array.append((file_key, file_name))

    return file_data_array
