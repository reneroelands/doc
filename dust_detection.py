#! c:\LocalData\Tools\Vision\_python.bat
# first line is a so called 'shebang' and can be used to execute the python script direct from explorer (doubleclick)
# refer to _python.bat for more details.

from threading import local
from tkinter import image_names
import cv2
import os
import matplotlib.pyplot as plt

def main():
    img_dir = 'P:/0740/009/Product/Test/ATD3_TestResults/Temporary Integration Results/ContainerCamera/Data/background/ADM1/220930-115728'

    os.chdir(img_dir)
    all_files = os.listdir()
    
    roi_min_row = -420
    roi_max_row = 420
    roi_min_col = -916
    roi_max_col = 897

    for image in all_files:
        if image.find('.png') > -1:
            print(image + ' --> ' + image.replace('.png', '.jpg'))
            img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
            # cv2.imshow(image, img)
            row, column = img.shape
            center_row = int(row/2)
            center_col = int(column/2)
            #print(center_row)
            #print(center_col)
            #print(center_row - roi_min_row)
            cropped_img = img[center_row+roi_min_row:center_row+roi_max_row, center_col+roi_min_col:center_col+roi_max_col]
            # cv2.imshow('', cropped_img)
            # cv2.imwrite(image.replace('.png', '_cropped.png'), cropped_img)
            brightspots = cropped_img[cropped_img > 50]
            print(len(brightspots))

if __name__ == "__main__":
    main()
