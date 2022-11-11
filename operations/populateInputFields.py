import globalStore.globals as globals

def populateInputFields(data):
    for i in range(len(data)):
        globals.modalwindow["-input"+str(i)+"-"].update(list(data)[i])