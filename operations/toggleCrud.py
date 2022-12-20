import globalStore.globals as globals
from operations.resizeImage import resize_image
# [am-20] function for changing the layout when the user clicks the toggle button
def toggleCrud():
    # changing the global variable for default view
    globals.cathod_history_active = not globals.cathod_history_active
    # variable for changing image for the toggle button
    imagePath = ''
    # if the variable is true it means the view is for the child records
    if globals.cathod_history_active:
        # updating the layout to the child window
        globals.window['-HISTORY_LAYOUT-'].update(visible=True)
        # hiding the parent window
        globals.window['-BASE_LAYOUT-'].update(visible=False)
        # changing the image path for the toggle button
        imagePath = 'images/off-btn.png'
    else:
        # hiding the child window
        globals.window['-HISTORY_LAYOUT-'].update(visible=False)
        # updating the layout to the parent window
        globals.window['-BASE_LAYOUT-'].update(visible=True)
        imagePath = 'images/on-btn.png'
    # updating the toggle button image on the window
    globals.window['-TOGGLE_CRUD-'].update(resize_image(imagePath, resize = (60,50)))