import PySimpleGUI as sg
from styles.defaultStyles import default_text_style
from datetime import datetime

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
                datetime.today().strftime('%Y-%m-%d'),
                font=text_style["font"]
            )
        ]
    ]