import pymongo
# Creating connection to Mongo DB on Port 9999
client = pymongo.MongoClient("localhost", 9999)
try:
    client.list_database_names()
except:
    print("Host is down")
    # if the database is not working
    client=None

class DAO():
    # Object initializer to set attributes (fields)
    def __init__(self):
        pass

    # Returning connection of database
    @staticmethod
    def databaseconnection():
        if(client!=None):
            return client["local"]
        else:
            return None
