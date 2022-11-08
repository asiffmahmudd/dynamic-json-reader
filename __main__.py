
import PySimpleGUI as sg
from layout.dynamicJsonLayout import dynamicJsonLayout

#function: main function. the app starts here
if __name__ == "__main__":    
    layout = [
        [sg.Text('JSON to open')],
        [sg.Input(disabled=True), sg.FileBrowse()],
        [sg.Open(), sg.Cancel()]
    ]
    window = sg.Window('Dynamic JSON Reader', layout)
    while True:
        event, values = window.read()
        if values:
            fname = values[0]
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break

        if not fname:
            sg.popup("Cancel", "No filename supplied")
        else:
            dynamicJsonLayout(fname)
    
    window.close()