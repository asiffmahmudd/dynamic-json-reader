import globalStore.globals as globals
from operations.resizeImage import resize_image

def toggleCrud():
    globals.cathod_history_active = not globals.cathod_history_active
    imagePath = ''
    if globals.cathod_history_active:
        globals.window['-HISTORY_LAYOUT-'].update(visible=True)
        globals.window['-BASE_LAYOUT-'].update(visible=False)
        imagePath = 'images/off-btn.png'
    else:
        globals.window['-HISTORY_LAYOUT-'].update(visible=False)
        globals.window['-BASE_LAYOUT-'].update(visible=True)
        imagePath = 'images/on-btn.png'
    globals.window['-TOGGLE_CRUD-'].update(resize_image(imagePath, resize = (60,50)))