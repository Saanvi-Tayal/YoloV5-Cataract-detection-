import os
import cv2
import shutil



path = os.path.join("dataset", "1_normal")
dic2 ={}
for obj in os.listdir(path):
    img = cv2.imread(os.path.join(path, obj))
    x = img.shape[0:2]
    ptf = ('dataset/normal labels/'+obj.replace(".png",".txt"))
    if x == (1728, 2592):
        with open(ptf, 'w') as f:
            f.write("1 0.497050 0.502212 0.648968 0.973451")

    elif x == (1632, 2464):
        with open(ptf, 'w') as f:
            f.write("1 0.503687 0.501113 0.662242 0.995402")
         
    
    elif x == (1224, 1848):
        with open(ptf, 'w') as f:
            f.write("1 0.500737 0.505047 0.659292 0.989906")
        

    #0 0.500737 0.505047 0.659292 0.989906
                        
