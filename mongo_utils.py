from mongo_connection import MongoConnection

# Path: mongo_utils.py
connection = MongoConnection(host='localhost', port=27017).connect()
collection_name = connection['otomoto']['cars']




def insert(car):
    car = {
    'id': 1,
    'name': 'Audi',
    'price': 52642
    }
    collection_name.insert_one(car)

insert('x')