import datetime

def isDate(value):
    try:
        format = '%Y-%m-%d'
        datetime.datetime.strptime(value, format)
        return True
    except:
        return False