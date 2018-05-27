import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb://rafa:daipass123@cluster0-shard-00-00-1ivyw.mongodb.net:27017,cluster0-shard-00-01-1ivyw.mongodb.net:27017,cluster0-shard-00-02-1ivyw.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin")

db = client.test.restaurants

def find_restaurant(key, value):
    return db.find( {key: value})
