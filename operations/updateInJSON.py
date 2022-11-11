import json
import os
import globalStore.globals as globals

# from macpath import dirname
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))

def updateInJSON():
    # open the file in the write mode
    filePath = ROOT_DIR + '\data\\' + "userdata.json"
    mode = 'w'

    with open(filePath, mode) as json_file:
        listKey = list(globals.data.keys())[0]
        json_data = {
            listKey : globals.data[listKey]
        }
        json_file.seek(0)  # convert back to json.
        json.dump(json_data, json_file, indent = 4)
        # Close the file object