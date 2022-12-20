import configparser
from pymongo import MongoClient
import globalStore.globals as globals

# [am-02] connecting to database
def connectToDatabase():
    # storing parsed config file in the global variable for later use
    globals.config = configparser.ConfigParser()   
    # reading the config file from the root directory of the project
    globals.config.read("config.ini")
    #Creating a pymongo client using the variables from the config file
    client = MongoClient(globals.config['Mongo']['ParentConnStr'] + "/" + globals.config['Mongo']['SourceDatabase'])

    #Getting the database instance
    globals.database = client["PERIPHERALS"]