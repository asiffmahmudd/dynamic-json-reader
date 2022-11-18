from operations.getStructFromMongo import getStructFromMongo
from operations.getDropDownValues import getDropDownValues
import PySimpleGUI as sg
from styles.defaultStyles import default_text_style
import globalStore.globals as globals

def createStructLayout(record):
    
    text_style = default_text_style()
    record.pop('_id')
    inputFields = []
    temp = []
    for inputKey, value in record.items():
        temp.append(
            sg.Text(
                inputKey,
                font=text_style["font"],
                size =text_style["size"],
            )
        )
        if (value["type"] == 'dropdown'):
            dropDownValues = getDropDownValues(inputKey)
            temp.append(
                sg.Combo(
                    dropDownValues,
                    key = inputKey,
                    font=text_style["font"], 
                    default_value=dropDownValues[0],
                    enable_events=True
                )
            )
        elif (value["type"] == 'textfield'):
            temp.append(
                sg.InputText(
                    key = inputKey,
                    font=text_style["font"], 
                )
            )
        elif (value["type"] == "date"):
            temp.append(
                sg.InputText(
                    key=inputKey, 
                    disabled=True, 
                    font=text_style["font"], 
                )
            )
            temp.append(
                sg.CalendarButton(
                    "Date", 
                    close_when_date_chosen="True",  
                    target=inputKey, 
                    no_titlebar=False, 
                    font=("Arial", 15)
                )
            )
        inputFields.append(temp)
        temp = []
    return inputFields