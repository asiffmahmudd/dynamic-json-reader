from operations.getStructFromMongo import getStructFromMongo
from operations.getDropDownValues import getDropDownValues
import PySimpleGUI as sg
from styles.defaultStyles import default_text_style
import globalStore.globals as globals

def createStructLayout(record, actionOn):
    
    text_style = default_text_style()
    record.pop('_id')
    inputFields = []
    col1 = []
    col2 = []

    if actionOn != "base":
        for inputKey, value in record.items():
            text = inputKey.replace("_", " ").title()
        
            col1.append(
                [sg.Push(),sg.Text(
                    text,
                    font=text_style["font"],
                )]
            )
            if (value["control"] == 'dropdown'):
                dropDownValues = getDropDownValues(inputKey)
                try:
                    col2.append(
                        [sg.Combo(
                            dropDownValues,
                            key = inputKey,
                            font=text_style["font"], 
                            default_value=dropDownValues[0],
                            enable_events=True
                        )]
                    )
                except:
                    col2.append(
                        [sg.Combo(
                            dropDownValues,
                            key = inputKey,
                            font=text_style["font"], 
                            enable_events=True
                        )]
                    )
            elif (value["control"] == 'textfield'):
                col2.append(
                    [sg.InputText(
                        key = inputKey,
                        font=text_style["font"], 
                    )]
                )
            elif (value["control"] == "date"):
                col2.append(
                    [sg.InputText(
                        key=inputKey, 
                        disabled=True, 
                        font=text_style["font"], 
                    ),
                    sg.CalendarButton(
                        "Date", 
                        close_when_date_chosen="True",  
                        target=inputKey, 
                        no_titlebar=False, 
                        font=("Arial", 12),
                        size=(10,1)
                    )]
                )
    else:
        for inputKey, value in record.items():
            text = inputKey.replace("_", " ").title()
        
            col1.append(
                [sg.Push(),sg.Text(
                    text,
                    font=text_style["font"],
                )]
            )
            if (value["control"] == 'dropdown'):
                dropDownValues = getDropDownValues(inputKey)
                try:
                    col2.append(
                        [sg.Combo(
                            dropDownValues,
                            key = inputKey,
                            font=text_style["font"], 
                            default_value=dropDownValues[0],
                            enable_events=True
                        )]
                    )
                except:
                    col2.append(
                        [sg.Combo(
                            dropDownValues,
                            key = inputKey,
                            font=text_style["font"], 
                            enable_events=True
                        )]
                    )
            elif (value["control"] == 'textfield'):
                try:
                    col2.append(
                        [sg.InputText(
                            key = inputKey,
                            font=text_style["font"],
                            default_text=globals.baseRecord[0][inputKey], 
                            disabled=True 
                        )]
                    )
                except:
                    col2.append(
                        [sg.InputText(
                            key = inputKey,
                            font=text_style["font"], 
                            disabled=True 
                        )]
                    )
            elif (value["control"] == "date"):
                try:
                    col2.append(
                        [sg.InputText(
                            key=inputKey, 
                            disabled=True, 
                            font=text_style["font"],
                            default_text=globals.baseRecord[0][inputKey] 
                        )]
                    )
                except:
                    col2.append(
                        [sg.InputText(
                            key=inputKey, 
                            disabled=True, 
                            font=text_style["font"],
                        )]
                    )

    inputFields.append([sg.Column(col1), sg.Column(col2)])
    return inputFields