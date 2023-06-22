from mongo_connection import MongoConnection
import json

connection = MongoConnection(host='localhost', port=27017).connect()
collection_otomoto = connection['carsAds']['otomoto']
collection_olx = connection['carsAds']['olx']

def insert(database, car):
    car_exists = None
    json_data = None
    car_id = None
    if database == 'collection_otomoto':
        collection = collection_otomoto
    elif database == 'collection_olx':
        collection = collection_olx
    try:
        json_data = json.dumps(car)
        car_id = car['id']
        car_exists = collection.find_one({'id': car_id})

    except:
        return 0

    if not car_exists:
        collection.insert_one(car)
        return 1
    else:
        return 0
