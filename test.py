import os
import cv2

path = os.path.join("dataset", "3_retina_disease")
dic={}
dic2 ={}
for obj in os.listdir(path):
    img = cv2.imread(os.path.join(path, obj))
    x = img.shape[0:2]
    print(obj , ".",x)
    if x in dic2:
        dic2[x] +=1 
    else:
        dic2[x] =1

print(dic2)

            
