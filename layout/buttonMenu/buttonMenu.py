import PySimpleGUI as sg
from styles.defaultStyles import default_btn_style

def buttonM():
    
    btn_style = default_btn_style()

    return [
        [
            sg.Button(
                'Add', 
                size=(8,1),
                font=btn_style["font"],
                key='-ADD_BTN-',
                enable_events=True
            ), 
            sg.Button(
                'Update', 
                size=(8,1),
                font=btn_style["font"],
                key='-UPDATE_BTN-',
                enable_events=True
            ), 
            sg.Button(
                'Delete', 
                size=(8,1),
                font=btn_style["font"],
                key='-DELETE_BTN-',
                enable_events=True
            ), 
            sg.Button(
                'Cancel', 
                pad=(10,5), 
                size=(8,1),
                font=btn_style["font"],
                visible=True
            )
        ]
    ]