from mongo_connection import MongoConnection

# Path: mongo_utils.py
connection = MongoConnection(host='localhost', port=27017).connect()
collection_name = connection['otomoto']['cars']




def insert(car):
    car = {
    'id': 2,
    'name': 'BMW',
    'price': 12412
    }
    collection_name.insert_one(car)

insert('x')