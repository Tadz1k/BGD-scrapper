from mongo_connection import MongoConnection
import json

connection = MongoConnection(host='localhost', port=27017).connect()
collection_otomoto = connection['carsAds']['otomoto']
collection_olx = connection['carsAds']['olx']



def insert(database, car):
    json_data = json.dumps(car)
    if database == 'otomoto':
        collection_otomoto.insert_one(car)
    elif database == 'olx':
        collection_olx.insert_one(car)
