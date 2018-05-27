import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb://isi-user:0608neyumansa@cluster0-shard-00-00-fjo6d.mongodb.net:27017,cluster0-shard-00-01-fjo6d.mongodb.net:27017,cluster0-shard-00-02-fjo6d.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

db = client.trabajos.isi

def find_by_key(key, value):
    return db.find( {key: value})

def search(query):
    return db.find()
