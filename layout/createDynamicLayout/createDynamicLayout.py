from layout.createDynamicLayout.createInputFields import createInputFields
from layout.createDynamicLayout.createTableLayout import createTableLayout
from layout.buttonMenu.buttonMenu import buttonM

def createDynamicLayout():
    button_menu = buttonM()
    inputLayout = createInputFields()
    tableLayout = createTableLayout()

    layout = button_menu + inputLayout + tableLayout
    return layout

