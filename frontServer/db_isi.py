import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb://isi-read-only-user:cIW25owBr5NPcEKG@cluster0-shard-00-00-fjo6d.mongodb.net:27017,cluster0-shard-00-01-fjo6d.mongodb.net:27017,cluster0-shard-00-02-fjo6d.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

collection = client.trabajos.isi

def find_by_key(key, value):
    return collection.find( {key: value})

def search(value):
    return collection.find({"$text": {"$search": value}})
