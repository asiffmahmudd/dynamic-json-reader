import PySimpleGUI as sg
from styles.defaultStyles import default_btn_style
from operations.resizeImage import resize_image
from styles.defaultStyles import default_text_style

def buttonM(actionOn):
    
    btn_style = default_btn_style()
    text_style = default_text_style()
    toggle_btn_path = 'images/off-btn.png'
    if actionOn == 'base':
        toggle_btn_path = 'images/on-btn.png'
    return [
        [
            sg.Button(
                'Add', 
                size=(8,1),
                font=btn_style["font"],
                key='-ADD_BTN-'+actionOn,
                enable_events=True
            ), 
            sg.Button(
                'Update', 
                size=(8,1),
                font=btn_style["font"],
                key='-UPDATE_BTN-'+actionOn,
                enable_events=True
            ), 
            sg.Button(
                'Delete', 
                size=(8,1),
                font=btn_style["font"],
                key='-DELETE_BTN-'+actionOn,
                enable_events=True
            ), 
            sg.Button(
                'Cancel', 
                pad=(10,5), 
                size=(8,1),
                font=btn_style["font"],
                visible=True
            ),
            sg.Push(),
            sg.Text(
                'CRUD on Base:',
                font=text_style["font"]
            ),
            sg.Image(
                resize_image(toggle_btn_path, resize = (60,50)),
                key="-TOGGLE_CRUD-",
                enable_events=True
            )
        ]
    ]