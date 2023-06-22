from pymongo import MongoClient

class MongoConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = None

    def connect(self):
        connection_string = f'mongodb://{self.host}:{self.port}/carAds'
        self.client = MongoClient(connection_string)
        return client

    def close(self):
        self.client.close()