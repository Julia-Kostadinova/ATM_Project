from pymongo import MongoClient

def connect_to_local_cluster():
    connection_string = 'mongodb://localhost:27017/python_course'
    return MongoClient(connection_string)

local_client = connect_to_local_cluster()

python_course_db = local_client['python_course']

clients_info_collection = python_course_db['clients_info']

for client_info in clients_info_collection.find():
    print(client_info)

