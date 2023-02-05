# ADD MORE EDITS FROM DOCUMENTATION https://pillow.readthedocs.io/en/stable/
#https://pillow.readthedocs.io/en/stable/reference/JpegPresets.html
from PIL import Image, ImageEnhance, ImageFilter
import os

#path = "./imgs" # folder for unedited images
#pathOut = "./editedImgs" # folder for edited images

path = input("Enter the address of the image to be edited.")
pathOut = input("Enter the address to store the edited image.")

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    # sharpening, BW
    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)
    edit = img.filter()
    # contrast
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')