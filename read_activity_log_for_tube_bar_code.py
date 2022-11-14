#! c:\LocalData\Tools\Vision\_python.bat
# first line is a so called 'shebang' and can be used to execute the python script direct from explorer (doubleclick)
# refer to _python.bat for more details.

from email import message_from_binary_file
from operator import delitem
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

def main():
    filename = 'P:/0740/009/Product/Test/ATD3_TestResults/Temporary Integration Results/ContainerCamera/Data/20221014 Data Matrix/ATD_ActivityLog.stripped.txt'
    print('start reading activity log')
#    df = pd.read_csv(filename, sep='\t:')
#    print(df)
#    df.to_excel('  try.xlsx')
    my_file = open(filename, 'r')
    lines = my_file.readlines()

    my_file.close()

    dates = []
    times = []
    counter = []
    types = []
    modules = []
    commands = []

    tube_ID = []
    DM_ID = []

    remarks = []

    for k in range(len(lines)):
    #for k in range(100):
        #print(str(k) + '    ' + lines[k])
        split_line = lines[k].replace('\n','').split('\t')
        if (split_line[0].find('2022') == []):
            # skip, the line doesn't contain data
            print('line doesn\'t start with date')
        elif len(split_line) > 5:
            # we assume the file is well formed
            datetime = split_line[0].split(' ')
            dates.append(datetime[0])
            times.append(datetime[1])
            deconstructed_time = datetime[1].split(':')
            # print(datetime[1])
            if len(deconstructed_time) < 3:
                print(str(k) + ' ' + datetime[1])
                for m in range(len(deconstructed_time)):
                    print(deconstructed_time[m])
            else:
                counter.append(float(deconstructed_time[0])*3600 + float(deconstructed_time[1])*60 + float(deconstructed_time[2]))
                types.append(split_line[1])
                modules.append(split_line[2])
                commands.append(split_line[3])
                if split_line[3] == 'DetermineContainerBarcodes':
                    print('line ' + str(k) + ': barcode detected!')
                    # Found container at position : 231 with ID : 0388454257
                    raw_number = split_line[4].split(':')[1].replace(' with ID','')
                    tube_ID.append((int(raw_number)-1)/10+1)
                    #print(str(tube_ID))
                    DM_ID.append(split_line[4].split(':')[2])
                else:
                    tube_ID.append('')
                    DM_ID.append('')
                # reconstruct
                remark = ''
                for m in range(4,len(split_line)):
                    remark = remark + ' ' + split_line[m]
                # print(remark)
                
                remarks.append(remark)
        else:
            print('warning: could not find other fields')


    title = ['Date', 'Time', 'Counter', 'Type', 'Module', 'Command', 'Remark', 'Tube ID', 'DM ID']
    df = pd.DataFrame() 
    df['Date'] = dates
    df['Time'] = times
    df['Counter'] = counter
    df['Type'] =  types
    df['Module'] = modules
    df['Command'] = commands
    df['Remark'] = remarks
    df['Tube ID'] = tube_ID
    df['DM_ID'] = DM_ID
    df.to_excel('20221014_DM.xlsx')

    input()

if __name__ == "__main__":
    main()
