
import globalStore.globals as globals

#clears the inputs of the given keys
def clearInputs():#keysToClear):
    inputFieldsLength = len(globals.inputKeys)

    for i in range(inputFieldsLength):
        globals.modalwindow["-input"+str(i)+"-"].update('')
    # for key in keysToClear:
    #     globals.window[key].update('')