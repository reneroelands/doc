#! c:\LocalData\Tools\Vision\_python.bat
# first line is a so called 'shebang' and can be used to execute the python script direct from explorer (doubleclick)
# refer to _python.bat for more details.

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.collections import PolyCollection
import numpy as np
# import pytesseract
# import cv2

def activity_log_to_dataframe(filename):
    print('start reading activity log')
    my_file = open(filename, 'r')
    lines = my_file.readlines()

    my_file.close()

    dates = []
    times = []
    counter = []
    types = []
    modules = []
    commands = []

    remarks = []

    for k in range(len(lines)):
        # print(lines[k])
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
                # reconstruct
                remark = ''
                for m in range(4,len(split_line)):
                    remark = remark + ' ' + split_line[m]
                # print(remark)
                remarks.append(remark)
                
        else:
            print('warning: could not find other fields')


   # title = ['Date', 'Time', 'Counter', 'Type', 'Module', 'Command', 'Remark']
    df = pd.DataFrame() 
    df['Date'] = dates
    df['Time'] = times
    df['Counter'] = counter
    df['Type'] =  types
    df['Module'] = modules
    df['Command'] = commands
    df['Remark'] = remarks
    #df.to_excel('DataMatrix.xlsx')
    return df

class duration:
    
    name = ''
    
    def __init__(self, module_id):
        self.name = module_id
        
    def set_data(self, df, type_id = 'TRACE', remove_list = []):

        self.type_id = type_id
        self.remove_list = remove_list
        if type_id in ['TRACE', 'INFO', 'DEBUG', 'ERROR']:
            temp = df[df['Type'] == type_id]
        else:
            print('unknown type id: ' + type_id)
            temp = df
        for item in remove_list:
            temp = temp[temp.Command != item]
        
        self.df = temp[temp['Module'] == self.name]
    
    def get_data(self):
        return self.df
    
    def crop(self, start_counter = 43825.587, end_counter = 46498.2274):

        self.df = self.df[(self.df.Counter >= start_counter)]
        self.df = self.df[(self.df.Counter <= end_counter)]
        self.df.Counter  = df.Counter - start_counter    

    def calculate(self, method = 'till next'):
        
        if method == 'till next':
            start = []
            duration = []
            for k in range(len(self.df)-1):
                start.append(df.Counter.values[k])
                duration.append(df.Counter.values[k+1] - df.Counter.values[k])
        
        else:
            print('Unknown method id: ' + method)
        
def get_adm_data(df, adm_id):
    
    remove_list = ['ImageCalculated', 'm_backgroundScanning_DoWork', 'm_backgroundDissecting_DoWork']
    temp = df[df['Type']=='TRACE']
    for item in remove_list:
        temp = temp[temp.Command != item]

    return temp[temp['Module']== adm_id]
   
def get_worfklow_data(df, adm_id):
    
    remove_list = []
    temp = df[df['Type']=='TRACE']
    for item in remove_list:
        temp = temp[temp.Command != item]

    return temp[temp['Module']== adm_id]
    
def crop_dataframe(df, start_counter = 43825.587, end_counter = 46498.2274):

    df1 = df[(df.Counter >= start_counter) & (df.Counter <= end_counter)]
    df1.Counter  = df1.Counter - start_counter
    
    return df1
    
def get_module_data(df, module_id):
    
    return df[df['Module']==module_id]

def get_duration(df, method_id = 'till next'):
    starts = []
    durations = []
    commands = [] 
    remarks = []
    module_id = df.Module.values[0]
    
    if method_id == 'till next':
        for k in range(len(df)-1):
            starts.append(df.Counter.values[k])
            durations.append(df.Counter.values[k+1] - df.Counter.values[k])
            commands.append(df.Command.values[k])
            remarks.append(df.Remark.values[k])
            
        nr_durations = len(durations)
        module_ids = nr_durations * [module_id]

        
    elif method_id == 'till finished':
        # change this for ATD_Handler
        finished = df[df.Remark.str.contains('Finished')]
        for k in range(len(finished)):
            command = finished.Command.values[k]
            command_counter = finished.Counter.values[k]
            # find the same command berfore 
            same_command_before_counter = max(df[(df.Counter < command_counter) & (df.Command == command)].Counter.values)
            print(str(command_counter) + ' ' + str(same_command_before_counter))
            starts.append(same_command_before_counter)
            durations.append(command_counter - same_command_before_counter)
            commands.append(command)
            remarks.append(finished.Remark.values[k])

        nr_durations = len(durations)
        module_ids = nr_durations * [module_id]
        
    else:
        print('Unknown method id: ' + method_id)
    
    duration_df = pd.DataFrame()
    duration_df['Module'] = module_ids
    duration_df['Command'] = commands
    duration_df['Remark'] = remarks
    duration_df['Start'] = starts
    duration_df['Duration'] = durations
    
    
    return duration_df

def create_bars(duration, colormapping, bar_row =1, bar_width=0.8):
    verts = []
    colors = []
    for k in range(len(duration)):
        start = duration.Start.values[k]
        end = start + duration.Duration.values[k]
        v = [(start, bar_row - bar_width/2),
             (start, bar_row + bar_width/2),
             (end, bar_row + bar_width/2),
             (end, bar_row - bar_width/2),
             (start, bar_row - bar_width/2)]
        verts.append(v)
        colors.append(colormapping[duration.Command.values[k]])
    
    return PolyCollection(verts, facecolors=colors)

    
def create_diamonds(command, color_id, row = 1, diamond_size = 0.8):

    verts = []
    colors = []
    for k in range(0, len(command)-1, 1):
        v = [(command.Counter.values[k], row - diamond_size/2),
             (command.Counter.values[k] + diamond_size/2, row),
             (command.Counter.values[k], row + diamond_size/2),
             (command.Counter.values[k] - diamond_size/2, row),
             (command.Counter.values[k], row - diamond_size/2)]
        verts.append(v)
        colors.append(color_id)
    
    return PolyCollection(verts, facecolors=colors)

def decode_scrape_move_remark(remark):
    
    ref = []
    x = []
    y = []
    Rz = []
    cmd = []
    
    # check for motion command
    if remark.find(' MotionCommand : ') > -1:
        motion_command = remark.replace(' MotionCommand : ', '')
        if motion_command.find('Start Reference ') > -1:
            #
            cmd = 'Start Reference'
            arg = motion_command.replace(',', '').split(' ')
            ref = float(arg[2])
            x = float(arg[4])
            y = float(arg[5])
            Rz = float(arg[7])
        elif motion_command.find('MoveTo ') > -1:
            cmd = 'MoveTo'
            arg = motion_command.replace(',', '').split(' ')
            ref = []
            x = float(arg[2])
            y = float(arg[3])
            Rz = []
        elif motion_command.find('Start Rotation ') > -1:
            cmd = 'Start Rotation'
            arg = motion_command.replace(',', '').split(' ')
            ref = []
            x = []
            y = []
            Rz = float(arg[2])
        elif motion_command.find('Stop ') > -1:
           cmd = 'Stop'
           #print(motion_command.split(','))
        else:
            print('Motion Command ' + motion_command + ' not recognized')
    
    return cmd, ref, x, y, Rz

def get_scrape_move_coordinates(adm_stage_duration):
    
    scrape_moves = adm_stage_duration[adm_stage_duration.Command == 'PerformScrapeMove']
    
    nr_scrape_moves = len(scrape_moves)
    
    REF = np.zeros(nr_scrape_moves)
    X  = np.zeros(nr_scrape_moves)
    Y = np.zeros(nr_scrape_moves)
    RZ = np.zeros(nr_scrape_moves)
    CMD = []
    # first decode the first line. It should contain all coordinates
    [cmd, ref, x, y, Rz] = decode_scrape_move_remark(scrape_moves.Remark.values[0])
    if not cmd or not ref or not x or not y or not Rz:
        print(' The first line should contain all coordinates!')
    else:
        REF[0] = ref
        X[0] = x
        Y[0] = y
        RZ[0] = Rz
        CMD.append(cmd)
        for k in range(1, len(scrape_moves)):
            [cmd, ref, x, y, Rz] = decode_scrape_move_remark(scrape_moves.Remark.values[k])
            CMD.append(cmd)
            if not ref:
                REF[k] = REF[k-1]
            else:
                REF[k] = ref
            if not x:
                X[k] = X[k-1]
            else:
                X[k] = x
            if not y:
                Y[k] = Y[k-1]
            else:
                Y[k] = y
            if not Rz:
                RZ[k] = RZ[k-1]
            else:
                RZ[k] = Rz
    
    df = pd.DataFrame()
    df['Module'] = scrape_moves.Module.values
    df['Command'] = CMD
    df['Ref'] = REF
    df['x'] = X
    df['y'] = Y
    df['Rz'] = RZ
    df['Start'] = scrape_moves.Start.values
    df['Duration'] = scrape_moves.Duration.values
    
    return df

def add_remark_to_move_command(adm_stage):
    
    for k in range(len(adm_stage)):
        if adm_stage.Command.values[k] == 'Move':
            adm_stage.Command.values[k] = 'Move' + adm_stage.Remark.values[k]
    return adm_stage

if __name__ == "__main__":
    filename = './data/ArchiveActivityLog.20220118.txt'
    filename = './data/20221103_ApplicationSoftwareLog_Selection.txt'
    
    filename = './data/20221111_VerTR_UIF8/20221111_MSw_ActivityLog_Selection.txt'
    
    df = activity_log_to_dataframe(filename)
    
    #Crop and filter
    thruput = crop_dataframe(df)
    
#%%----------------------------------------------------------------------------    
    cats = {"ATD_Handler" : 1, "ADM1" : 2, "ADM2" : 3, "Workflow" : 4}

    handler_colormapping = {"MoveToInfeedUnit" : "C0", 
                    "MoveToADM" : "C1", 
                    "MoveToStoreSlot" : "C2", 
                    "MoveToOutfeedUnit" : "C3", 
                    "MoveToRejectUnit": "C4",
                    "PlaceCarrierInADM" : "C5", 
                    "PlaceCarrierInStoreSlot" : "C6", 
                    "PlaceCarrierInOutfeedUnit" : "C7", 
                    "PlaceCarrierInRejectUnit" : "C8",
                    "TakeOverCarrierAtInfeedUnit" : "C9", 
                    "TakeOverCarrierAtADM" : "C10", 
                    "TakeOverCarrierAtStoreSlot" : "C11"
                    }
    
    adm_colormapping = {"PrepareRetrieveCarrier": "C12",            
                    "StartScan" : "C13",
                    "PrepareHandoutCarrier": "C14",
                    "FinishHandoutCarrier" : "C15",
                    "StartDissecting": "C16",
                    "ImageCalculated": "C17",
                    "m_backgroundScanning_DoWork": "C17",
                    "m_backgroundDissecting_DoWork": "C17"
                    }

    #Get Handler data
    han_thruput = get_module_data(thruput, "ATD_Handler")
    han_duration = get_duration(han_thruput, 'till finished')
    han_bars = create_bars(han_duration, handler_colormapping, cats['ATD_Handler'])
    
    adm = get_adm_data(thruput, 'ADM1')
    nr_commands = len(adm)
    adm_duration = get_duration(adm, 'till next')
    adm_bars = create_bars(adm_duration, adm_colormapping, cats['ADM1'])

    adm_stage = get_adm_data(thruput, 'ADM2_Stage')
    adm_stage = add_remark_to_move_command(adm_stage)
    adm_stage_commands = adm_stage.Command.unique()
    adm_stage_colormap = dict.fromkeys(adm_stage_commands)
    for k in range(len(adm_stage_commands)):
        adm_stage_colormap[adm_stage_commands[k]] = 'C' +str(k)
        
    adm_stage_duration = get_duration(adm_stage, 'till next')
    adm_stage_bars = create_bars(adm_stage_duration, adm_stage_colormap, cats['ADM2'])
     
    workflow = get_module_data(thruput, 'Workflow')
    nr_commands = len(workflow)
    workflow_bars = create_diamonds(workflow[:nr_commands], 'black', cats['Workflow'])

    #Pictures
    fig, ax = plt.subplots()
    ax.add_collection(han_bars)
    ax.add_collection(adm_bars)
    ax.add_collection(adm_stage_bars)
    ax.add_collection(workflow_bars)
    
    ax.autoscale()
    
    ax.set_yticks([1,2,3,4])
    ax.set_yticklabels(["ATD Handler", "ADM1", "ADM2", "Workflow"])
    plt.show()    
