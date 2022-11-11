import globalStore.globals as globals

def populateInputFields(data):
    name, salary, birthday = data
    globals.window['-NAME-'].update(name)
    globals.window['-SALARY-'].update(salary)
    globals.window['-BIRTHDAY-'].update(birthday)