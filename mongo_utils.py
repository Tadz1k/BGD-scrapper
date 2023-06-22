from mongo_connection import MongoConnection
import json

connection = MongoConnection(host='localhost', port=27017).connect()
collection_otomoto = connection['carsAds']['otomoto']
collection_olx = connection['carsAds']['olx']

def insert(database, car):
    json_data = json.dumps(car)
    car_id = car['id']
    print(car_id)
    car_exists = f'{database}'.find_one({'id': car_id})
    print(f'car_exists: {car_exists}')

    if not car_exists:
        print('Inserting...')
        f'{database}'.insert_one(car)
        return 1
    else:
        return 0
