import pandas as pd
import sys
import os
from PIL import Image
import pandas as pd
dic = {"ila - Copy/images/train/0_cataract/":"ila - Copy/labels/train/0_cataract/"}
   # "ila - Copy/images/train/1_normal/":"ila - Copy/labels/train/1_normal/",
   # "ila - Copy/images/train/2_glaucoma/":"ila - Copy/labels/train/2_glaucoma/",
 #   "ila - Copy/images/train/3_retina_disease/":"ila - Copy/labels/train/3_retina_disease/"}
count = 101
for i  in dic.keys():
    for obj, label  in zip(os.listdir(i),(os.listdir(dic[i]))):

        image = Image.open(i+obj)
        FlipImage = image.transpose(Image.FLIP_LEFT_RIGHT)
        file_name = i+"cataract_"+str(count)+".png"
        label_name = i+"cataract_"+str(count)+".txt"
        FlipImage.save(file_name,'png')
        count+=1

        with open (i+obj,'r') as f:
          text = f.read()
        with open(label_name, 'w') as f:
            f.write(text)





