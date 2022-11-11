import json
import globalStore.globals as globals

def readJSONFile(filePath):
    try:
        # Opening JSON file
        f = open(filePath)
        
        # returns JSON object as 
        # a dictionary
        jsondata = json.load(f)
        # Closing file
        f.close()
        
        globals.data = jsondata
        listObject = list(jsondata.keys())[0]
        globals.inputKeys = list(globals.data[listObject][0].keys())
        return jsondata
    except:
        return []