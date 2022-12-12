import configparser
from pymongo import MongoClient
import globalStore.globals as globals

def connectToDatabase():
    globals.config = configparser.ConfigParser()   
    # configFilePath = r'config.ini'
    globals.config.read("config.ini")
    #Creating a pymongo client
    client = MongoClient(globals.config['Mongo']['ParentConnStr'] + "/" + globals.config['Mongo']['SourceDatabase'])

    #Getting the database instance
    globals.database = client["PERIPHERALS"]