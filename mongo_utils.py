from mongo_connection import MongoConnection
import json

connection = MongoConnection(host='localhost', port=27017).connect()
collection_otomoto = connection['otomoto']['cars']
collection_olx = connection['olx']['cars']



def insert(database, car):
    json_data = json.dumps(car)
    if database == 'otomoto':
        collection_otomoot.insert_one(car)
    elif database == 'olx':
        collection_olx.insert_one(car)
        

car_dict = {'id': '123', 'title': 'test', 'description': 'test', 'manufacturer': 'test', 'model': 'test', 'fuel': 'test', 'engine': 'test', 'mileage': 'test',}
insert(car_dict)