import PySimpleGUI as sg
import datetime
from styles.defaultStyles import default_input_style
import globalStore.globals as globals

def getField(value, index):
    input_style = default_input_style()
    inputKey = "-input"+str(index)+"-"
    try:
        format = '%Y-%m-%d'
        datetime.datetime.strptime(value, format)
        globals.dataTypes.update({inputKey: "date"})
        return [
            sg.InputText(
                key=inputKey, 
                disabled=True, 
                font=input_style["font"], 
                pad=input_style["pad"]
            ),
            sg.CalendarButton(
                "Date", 
                close_when_date_chosen="True",  
                target=inputKey, 
                no_titlebar=False, 
                format=format,
                font=("Arial", 15)
            )
        ]
    except Exception as e:
        globals.dataTypes.update({inputKey: type(value)})
        if type(value) == str or type(value) == int:
            return [
                sg.InputText(
                    key=inputKey, 
                    font=input_style["font"], 
                    pad=input_style["pad"])
                ]
        elif type(value) == list:
            return [
                sg.Combo(
                    value, 
                    key=inputKey, 
                    font=input_style["font"], 
                    pad=input_style["pad"])
                ]
        elif type(value) == type(True):
            return [
                sg.Radio(
                    'True', 
                    inputKey, 
                    default=True, 
                    font=input_style["font"], 
                    pad=input_style["pad"],
                    key=inputKey
                ),
                sg.Radio(
                    'False',
                    inputKey,
                    font=input_style["font"], 
                    pad=input_style["pad"]
                )
            ]