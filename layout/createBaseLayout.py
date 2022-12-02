from operations.getStructFromMongo import getStructFromMongo
from operations.getDropDownValues import getDropDownValues
import PySimpleGUI as sg
from styles.defaultStyles import default_text_style
import globalStore.globals as globals

def createBaseLayout(record, actionOn):
    
    text_style = default_text_style()
    record.pop('_id')
    inputFields = []
    col1 = []
    col2 = []

    for inputKey, value in record.items():
        text = inputKey.replace("_", " ").title()
        col1.append(
            [sg.Push(),sg.Text(
                text,
                font=text_style["font"],
            )]
        )
        if (value["control"] == 'textfield') or (value["control"] == 'dropdown'):
            col2.append(
                [sg.InputText(
                    key = inputKey+actionOn,
                    font=text_style["font"], 
                )]
            )
        elif (value["control"] == "date"):
            col2.append(
                [sg.InputText(
                    key=inputKey+actionOn, 
                    disabled=True, 
                    font=text_style["font"], 
                ),
                sg.CalendarButton(
                    "Date", 
                    close_when_date_chosen="True",  
                    target=inputKey+actionOn, 
                    no_titlebar=False, 
                    font=("Arial", 12),
                    size=(10,1)
                )]
            )

    inputFields.append([sg.Column(col1), sg.Column(col2)])
    return inputFields