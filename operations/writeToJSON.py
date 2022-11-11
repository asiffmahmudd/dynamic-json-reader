import json
import os
import PySimpleGUI as sg
import globalStore.globals as globals

# from macpath import dirname
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))

def writeToJSON(data):
    # open the file in the write mode
    filePath = ROOT_DIR + '\data\\' + "userdata.json"
    mode = ''

    if os.path.exists(filePath):
        mode = 'r+'
    else:
        mode = 'w'

    with open(filePath, mode) as json_file:
        listObject = list(globals.data.keys())[0]
        if mode == 'w':
            data = {
                listObject : [
                    data
                ]
            }
            json.dump(data, json_file)
        else:
             # First we load existing data into a dict.
            file_data = json.load(json_file)
            # Join new_data with file_data inside emp_details
            file_data[listObject].append(data) # Sets file's current position at offset.
            json_file.seek(0)  # convert back to json.
            json.dump(file_data, json_file, indent = 4)
        sg.popup("User added!")
        # Close the file object