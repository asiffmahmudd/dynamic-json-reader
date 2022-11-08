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
        return jsondata
    except:
        return []