#! c:\LocalData\Vision\_python.bat
# first line is a so called 'shebang' and can be used to execute the python script direct from explorer (doubleclick)
# refer to _python.bat for more details.
import cv2
import numpy as np
from matplotlib import pyplot as plt
# this is just to unconfuse pycharm
try:
    from cv2 import cv2
except ImportError:
    pass


def main():
    print('Start of the code')
    img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)
    niew = img[1:100,200:250]
    cv2.imshow('original',img)
    cv2.waitKey(0)

    cv2.imshow('sub',niew)
    cv2.waitKey(0)



if __name__ == "__main__":
    main()
