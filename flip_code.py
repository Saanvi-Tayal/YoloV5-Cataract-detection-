# ----------------------- Imports ------------------------

import os
import cv2
from PIL import Image


# ------------------------- Code -------------------------

os.chdir("ila\\")
# print(os.getcwd())

img_path = os.path.join("images", "train")
label_path = os.path.join("labels", "train")
categories = os.listdir(img_path) # ['0_cataract', '1_normal', '2_glaucoma', '3_retina_disease']
# print(categories)

for category in categories:
    if category == "1_normal": # as we don't want to do augmentation on 1_normal
        continue

    folder_path = os.path.join(img_path, category)
    # print(folder_path)

    for img in os.listdir(folder_path):
        # print(img)

        img_name = img.split(".")[0]
        # print(img_name)

        # Initialization
        curr_path_img = os.path.join(img_path, category, img_name + ".png")
        final_path_img = os.path.join(img_path, category, img_name + "_flipped.png")

        # Image Manupulation
        image = Image.open(curr_path_img)
        image_flipped = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        image_flipped.save(final_path_img, "png")

        curr_path_label = os.path.join(label_path, category, img_name + ".txt")
        final_path_label = os.path.join(label_path, category, img_name + "_flipped.txt")


        # Label Manupulation
        with open(curr_path_label, "r") as fh:
            txt_data = fh.read()

        txt_data_lst = [float(x) for x in txt_data.split()]
        txt_data_lst[1] = 1 - txt_data_lst[1]
        txt_data_lst[2] = 1 - txt_data_lst[2]
        txt_data = " ".join(str(x) for x in txt_data_lst)

        with open(final_path_label, "w") as fh:
            fh.write(txt_data)
        
        # For the time being
        break
