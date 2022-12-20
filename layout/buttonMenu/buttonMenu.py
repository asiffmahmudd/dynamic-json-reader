import PySimpleGUI as sg
from styles.defaultStyles import default_btn_style
from operations.resizeImage import resize_image
from styles.defaultStyles import default_text_style
import globalStore.globals as globals

# [am-34] button menu layout main function
def buttonM(actionOn):
    #getting default style 
    btn_style = default_btn_style()
    text_style = default_text_style()
    # path to toggle button off image
    toggle_btn_path = 'images/off-btn.png'
    if actionOn == 'base':
        # path to toggle button on image
        toggle_btn_path = 'images/on-btn.png'
    buttonLayout = [
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
    ]
    # checking if isParentChild active. if it's active then show the toggle button
    if globals.config["app-params"]["isParentChild"] == "1":
        buttonLayout.append(sg.Push())
        buttonLayout.append(
            sg.Text(
                'CRUD on Parent:',
                font=text_style["font"]
            )
        )
        buttonLayout.append(
            sg.Image(
                resize_image(toggle_btn_path, resize = (60,50)),
                key="-TOGGLE_CRUD-",
                enable_events=True
            )
        )
    return [buttonLayout]