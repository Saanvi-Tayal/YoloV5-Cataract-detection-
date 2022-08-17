# Imports
import os
import cv2
from PIL import Image


# Code

img_path = os.path.join("images", "train")
label_path = os.path.join("labels", "train")
categories = os.listdir(img_path) # ['0_cataract', '2_glaucoma', '3_retina_disease']
# print(categories)

for category in categories:
    folder_path = os.path.join(img_path, category)
    # print(folder_path)

    for img in os.listdir(folder_path):
        # print(img)

        img_name = img.split(".")[0]
        # print(img_name)

        curr_path = os.path.join(img_path, category, img_name + ".png")
        final_path = os.path.join(img_path, category, img_name + "_flipped.png")

        image = Image.open(curr_path)
        image_flipped = image.transpose(Image.FLIP_LEFT_RIGHT)
        image_flipped.save(final_path, "png")
        break
