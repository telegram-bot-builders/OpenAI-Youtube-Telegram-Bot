from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

class Database:
    def __init__(self, database, table):
        self.database = database
        self.table = table
        self.user_table = database
        self.client = self._connect_to_server()
        self.collection = self._connect_to_database()

    def _connect_to_server(self):
        MONGODB_PWD = os.getenv('MONGODB_PWD')
        MONGODB_USER = os.getenv('MONGODB_USR')
        MONGO_DB_CLUSTER_CODE = os.getenv('MONGO_DB_CLUSTER_CODE')
        uri = f"mongodb+srv://{MONGODB_USER}:{MONGODB_PWD}@cluster0.{MONGO_DB_CLUSTER_CODE}.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        return MongoClient(uri, server_api=ServerApi('1'))
    
    def _connect_to_database(self):
        db = self.client[self.database]
        return db[self.table]

if __name__ == '__main__':
    _db = Database("Communities", "Acct_Execs_Connected")

    try:
        _db.client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
        pass
