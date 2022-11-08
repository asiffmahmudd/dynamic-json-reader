import PySimpleGUI as sg
from styles.defaultStyles import default_input_style

def getField(value, index):
    input_style = default_input_style()
    if type(value) == str or type(value) == int:
        return [sg.InputText(key="-input"+str(index)+"-", font=input_style["font"], pad=input_style["pad"])]
    elif type(value) == list:
        return [sg.Combo(value, key="-input"+str(index)+"-", font=input_style["font"], pad=input_style["pad"])]
    elif type(value) == type(True):
        return [
            sg.Radio('True', "input"+str(index), default=True, font=input_style["font"], pad=input_style["pad"]),
            sg.Radio('False', "input"+str(index), font=input_style["font"], pad=input_style["pad"])
        ]