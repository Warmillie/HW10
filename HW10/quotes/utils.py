from pymongo import MongoClient
from pymongo.server_api import ServerApi


def get_mongodb():
    client = MongoClient(
    "mongodb+srv://warmillie1:%23EDCxsw2!QAZ@cluster0.ezi9yvk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    server_api=ServerApi('1'))
    db = client.HW
    return db


