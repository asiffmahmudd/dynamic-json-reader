import PySimpleGUI as sg
from styles.defaultStyles import default_text_style
from datetime import datetime
import globalStore.globals as globals

# [am-38] statusbar layout
def createStatusBarLayout(actionOn):
    text_style = default_text_style()

    return [
        [
            sg.Text(
                "CRUD on "+ actionOn,
                font=text_style["font"]
            ),

            sg.Push(),

            sg.Text(
                "Version: " + globals.config['file-reader']['version'],
                font=text_style["font"]
            ),

            sg.Push(),

            sg.Text(
                datetime.today().strftime('%Y-%m-%d'),
                font=text_style["font"]
            )
        ]
    ]