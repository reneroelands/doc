#! c:\LocalData\Tools\Vision\_python.bat
# first line is a so called 'shebang' and can be used to execute the python script direct from explorer (doubleclick)
# refer to _python.bat for more details.

from threading import local
from tkinter import image_names
import cv2
import os

all_image = [['220906', '134123', '0_0'],
    ['220906',	'134511', '5_3'],
    ['220906',	'135041'],
    ['220906',	'135323', '1_1', '3_1', '4_0'],
    ['220906',	'135728', '0_0', '1_1', '1_4'],
    ['220906',	'140824', '5_0', '5_2'],
    ['220906',	'142305', '0_0'],
    ['220906',	'151405'],			
    ['220906',	'152033', '5_2'],
    ['220906',	'152725', '0_0', '0_1'],
    ['220906',	'154743', '0_1', '3_1', '3_2'],
    ['220906',	'154931', '3_0', '3_1', '3_2'],
    ['220906',	'161827', '3_0'],	
    ['220906',	'163624', '4_4'],
    ['220906',	'163830'],			
    ['220906',	'164402', '0_0', '5_1'],	
    ['220906',	'165537', '2_0'],
    ['220906',	'165826', '2_0', '5_0'],
    ['220906',	'170018', '2_0'],
    ['220906',	'170317', '2_0'],
    ['220906',	'170804', '0_0', '4_0'],
    ['220906',	'174040', '2_0'],
    ['220906',	'174255', '0_0', '1_0', '2_0'],
    ['220906',	'174554', '2_0', '2_1', '5_0'],
    ['220906',	'174752', '2_0', '5_0'],	
    ['220906',	'175018', '2_0', '5_0'],	
    ['220907',	'100445', '1_0', '5_0'],	
    ['220907',	'100739', '5_0'],
    ['220907',	'101306', '0_0', '1_4',	'5_0'],
    ['220907',	'101559', '0_0', '4_0', '5_0'],
    ['220907',	'105037'],
    # ['220907',	'105354', '0_2', '5_4'],
    # ['220907',	'105638'],
    # ['220907',	'105942', '0_2'],
    # ['220907',	'111727', '0_3'],
    # ['220907',	'112211'],
    # ['220907',	'112418', '0_0', '0_1'],
    # ['220907',	'112903'],
    # ['220907',	'113718'],
    # ['220907',	'114320'],
    # ['220907',	'114514', '5_2'],	
    # ['220907',	'115750'],
    # ['220907',	'115944'],
    # ['220907',	'120118']
]

more_image = []
def main():
    # img_dir = 'C:/LocalData/XALL HT/20220909 log/ADM2/ProcessImages/'
    # converted_dir = 'C:/LocalData/converted images/'

    # for k in range(len(all_image)):
    #     local_dir = all_image[k][0] + '-' + all_image[k][1]

        
    #     if len(all_image[k]) > 2:
    #         for m in range(2,len(all_image[k])):
    #             image_name = img_dir + local_dir + '/container_' + all_image[k][m] + '.png'
    #             converted_name  = converted_dir + 'container ' + local_dir + '_' + all_image[k][m] + '.jpg'
    #             print(image_name + ' --> ' + converted_name)
    #             img = cv2.imread(image_name, cv2.IMREAD_COLOR)
    #             cv2.imwrite(converted_name, img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

    img_dir = 'C:/LocalData/Projects/XYALL/XYALLTT-525/Data/20220921/ADM1/220921-153256/'
    img_dir = 'C:/LocalData/Projects/XYALL/XYALLTT-525/Data/20220921/ADM1/220921-161935/'
    img_dir = 'C:/LocalData/Projects/XYALL/XYALLTT-525/Data/20220921/ADM1/220921-162641/'
    img_dir = 'C:/LocalData/Projects/XYALL/XYALLTT-525/Data/20220921/ADM2/220921-161653/'
    img_dir = 'C:/LocalData/Projects/XYALL/XYALLTT-525/Data/20220921/ADM2/220921-162856'

    os.chdir(img_dir)
    png_files = os.listdir()
    
    for image in png_files:
        print(image + ' --> ' + image.replace('.png', '.jpg'))
        img = cv2.imread(image, cv2.IMREAD_COLOR)
        cv2.imwrite(image.replace('.png', '.jpg'), img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

if __name__ == "__main__":
    main()
