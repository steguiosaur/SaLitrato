import os

from pytesseract import image_to_string
from PIL import Image

DATA_FOLDER = "data"
FOLDER_PATH = os.path.join(os.getcwd(), DATA_FOLDER)

def convert_to_text(current_dir, image_file):
    image_path = os.path.join(FOLDER_PATH, current_dir, image_file)
    with open(image_file + ".txt", mode="w") as f:
        f.write(image_to_string(Image.open(image_path)))
