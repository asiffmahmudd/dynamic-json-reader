
from styles.defaultStyles import default_text_style
import PySimpleGUI as sg
import globalStore.globals as globals
from layout.createDynamicLayout.getField import getField

def createInputFields():
    layout = []
    index = 0
    text_style = default_text_style()
    singleRow = globals.data['info'][0]
    for field in singleRow:
        inputField = getField(singleRow[field], index)
        layout.append([sg.Text(field, font=text_style["font"], size=text_style["size"])] + inputField)
        index += 1
    return layout