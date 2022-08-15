import os
import splitfolders  # or import split_folders

input_folder = 'dataset - Copy/'
output_folder = 'ila/'
# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
splitfolders.ratio(input_folder, output=output_folder, seed=42, ratio=(.40, .30,.30), group_prefix=None) # default values

counter=0
dic  = {
    "ila/test/0_cataract/":"ila/test/cataract labels/", "ila/train/0_cataract/":"ila/train/cataract labels/","ila/val/0_cataract/":"ila/val/cataract labels/",
    "ila/test/1_normal/":"ila/test/normal labels/","ila/train/1_normal/":"ila/train/normal labels/","ila/val/1_normal/":"ila/val/normal labels/",
    "ila/test/2_glaucoma/":"ila/test/glaucoma labels/","ila/train/2_glaucoma/":"ila/train/glaucoma labels/","ila/val/2_glaucoma/":"ila/val/glaucoma labels/",
    "ila/test/3_retina_disease/":"ila/test/retina labels/","ila/train/3_retina_disease/":"ila/train/retina labels/","ila/val/3_retina_disease/":"ila/val/retina labels/",
    }
for i  in dic.keys():
    for obj, label  in zip(os.listdir(i),(os.listdir(dic[i]))):
        obje = obj.replace(".png", ".txt")
        if obje !=label:
            counter +=1
            for i , j in zip(obje, label):
                if i != j :
                    print(i, j )
            print(obj, ".", label )
    print(counter)
    