#! c:\LocalData\Tools\Vision\_python.bat
# first line is a so called 'shebang' and can be used to execute the python script direct from explorer (doubleclick)
# refer to _python.bat for more details.

import numpy as np
from matplotlib import pyplot as plt
import cv2
from pylibdmtx.pylibdmtx import decode
import ctypes

def main():
    print('load container image')
    img = cv2.imread('220906-152725_0_1.png', cv2.IMREAD_COLOR)
    
    print(decode(img))

    DMlib = ctypes.cdll.LoadLibrary("./icDMDecNetPro.dll")
    DMlib = ctypes.cdll.LoadLibrary("./IP2Lib64.dll")
    DMlib = ctypes.WinDLL("./DM_EP_64.dll")

    DMApiProto = ctypes.WINFUNCTYPE (
        ctypes.c_int,   # Return ...
        ctypes.c_int,   # Parameters 1 ...
        ctypes.c_int)   # Parameters 1 ...
    DMApiParams = (1, "i1", 5000), (1, "i2", 8191),

    DMApi = DMApiProto(("Connect_DM_Decoder", DMlib), DMApiParams)

    DMApi(5000,8191)

if __name__ == "__main__":
    main()
