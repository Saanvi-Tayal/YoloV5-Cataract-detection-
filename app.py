import streamlit as st
import torch
from yolov5.detect import *
from PIL import Image
from io import *
import glob
#from IPython.display import Image, display
from datetime import datetime
import os
import wget
import time
import glob


## CFG
cfg_model_path = "yolov5/runs/train/exp14/weights/best.pt"

 

def imageInput(device, src):
    
    if src == 'Upload your own data.':
        global image_file
        global img
      
        image_file = st.file_uploader("Upload An Image", type=['png', 'jpeg', 'jpg']) #image as input
        col1, col2 = st.columns(2)
        if image_file is not None:
            img = Image.open(image_file)
            with col1:
                st.image(img, caption='Uploaded Image', use_column_width='always')#show image

            inp = img.save(f'yolov5/data/images/{image_file.name}')# save image

           
            run(weights= "yolov5/runs/train/exp14/weights/best.pt"  ,conf_thres= 0.1, source = "yolov5/data/images" ,iou_thres=0.65,max_det=0) #run model 
            #run fucntion hain in detect.py, which was in yolo already nd in shell we were running it only
            
     
        
            # #--Display predicton
            
            # img_ = Image.open(outputpath)
            # with col2:
            #     st.image(img_, caption='Model Prediction(s)', use_column_width='always')

def main():
    # -- Sidebar
    st.sidebar.title('⚙️Options')
    datasrc = st.sidebar.radio("Select input source.", ['From test set.', 'Upload your own data.'])
    
        
                
    option = st.sidebar.radio("Select input type.", ['Image', 'Video'])
    if torch.cuda.is_available():
        deviceoption = st.sidebar.radio("Select compute Device.", ['cpu', 'cuda'], disabled = False, index=1)
    else:
        deviceoption = st.sidebar.radio("Select compute Device.", ['cpu', 'cuda'], disabled = True, index=0)
    # -- End of Sidebar

    st.header('📦Obstacle Detection')
    st.subheader('👈🏽 Select options left-haned menu bar.')
    st.sidebar.markdown("https://github.com/thepbordin/Obstacle-Detection-for-Blind-people-Deployment")
    if option == "Image":    
        imageInput(deviceoption, datasrc)



if __name__ == '__main__':
  
    main()
