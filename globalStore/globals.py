# class for storing global variables for using them on different files accross the application
database = None
baseStruct = {}                 # variable for storing the parent structure of data
historyStruct = {}              # variable for storing the child structure of data
config = None                   # variable for storing the config file data
event = None                    # variable for storing events happening on UI
value = None                    # variable for storing values associated with those events
window = None                   # variable for changing UI changes on the window
data = []                       # variable for storing child data to show on the table
cathod_history_active = True    # variable for deciding the default view (child/parent)
baseRecord = []                 # variable for storing current parent data to show on the table