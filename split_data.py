import os
import splitfolders  # or import split_folders

# input_folder = 'dataset - Copy/'
# output_folder = 'ila/'
# # Split with a ratio.
# # To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
# splitfolders.ratio(input_folder, output=output_folder, seed=42, ratio=(.40, .30,.30), group_prefix=None) # default values
counter=0
for obj, label  in zip(os.listdir("ila/val/0_cataract"),(os.listdir("ila/val/cataract labels"))):
    obje = obj.replace(".png", ".txt")
    if obje !=label:
        counter +=1
        for i , j in zip(obje, label):
            if i != j :
                print(i, j )
        print(obj,".",label)
print(counter)
    