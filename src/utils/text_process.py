import csv
import os

from .boyer import boyer_moore

DATA_FOLDER = "data"
FOLDER_PATH = os.path.join(os.getcwd(), DATA_FOLDER)

def get_rows_of_text(path, filenames):
    rows_of_text = {}
    for filename in filenames:
        text_file = os.path.join(path, filename + ".txt") 
        with open(text_file, 'r') as file:
            rows_of_text[filename] = [line.replace('\n', '') for line in file]
    return rows_of_text

def process_csv_and_text(current_folder):
    if current_folder is None: return
    subfolder_path = os.path.join(FOLDER_PATH, current_folder)
    csv_path = os.path.join(subfolder_path, current_folder + ".csv")

    filenames = []
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            filenames.append(row['file_name'])

    ordered_file_names = sorted(filenames)
    rows_of_text = get_rows_of_text(subfolder_path, ordered_file_names)

    data = {}
    for filename in ordered_file_names:
        data[filename] = rows_of_text[filename]

    return data

def find_pattern_in_data(data, pattern, bad_char):
    result = {}
    for filename, rows in data.items():
        matched_rows = {}
        for i, row in enumerate(rows):
            positions = boyer_moore(row, pattern, bad_char)
            if positions:
                matched_rows[i] = positions

        # Skip adding entries with no matched rows
        if matched_rows:
            result[filename] = matched_rows

    return result

def get_text_in_txt(current_folder, file):
    if current_folder is None: return
    subfolder_path = os.path.join(FOLDER_PATH, current_folder)
    filepath = os.path.join(subfolder_path, file + ".txt")
    with open(filepath, "r") as file:
        contents = file.read()
        return contents
