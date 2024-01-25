# DB.py
from pymongo import MongoClient


class DB:
    def __init__(self):
        self.client = None

    def connect_to_local_cluster(self):
        connection_string = 'mongodb://localhost:27017/python_course'
        self.client = MongoClient(connection_string)

    def get_clients_info_collection(self):
        if self.client:
            return self.client['python_course']['clients_info']
        else:
            raise Exception("Not connected to the database.")

    def identify_client_by_id(self, client_id):
        clients_info_collection = self.get_clients_info_collection()
        client = clients_info_collection.find_one({'client_id': client_id})
        return client['name'] if client else None

    def insert_db_record(self, new_client_name):
        self.clients_info.insert_one({
            "name": new_client_name
        })
    