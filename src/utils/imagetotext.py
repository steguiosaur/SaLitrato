from PIL import Image
from pytesseract import *

img_path = "insert path file"
img_name = "insert image name"
img_text = image_to_string(Image.open(img_path))
print(img_text)

with open(img_name+".txt", mode="w") as f:
    f.write(img_text)