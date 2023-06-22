from pymongo import MongoClient

class MongoConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self):
        connection_string = f'mongodb://{self.host}:{self.port}/carAds'
        client = MongoClient(connection_string)
        return client

    def close(self):
        self.client.close()