#!/usr/bin/env
'''
Instead of Redis, I use MongoDB instead -- since I am using it in 
a regular basis:)
Make sure that you have a live mongo connection running on port 27017,
which is the default port.
'''
import uuid
from pymongo import MongoClient
## start a client to connect python to mongo
c = MongoClient()
## to use a specific db
## > use mydb 
db = c['mydb']
## to create a collection instance to access collection mongoPyPipe
## I've already created this collection in mongo shell
collection = db['mongoPyPipe']

## interatively insert doc to collection
## > db.mongoPyPipe.insert({"id": i, "value": uuid})
for i in range(200):
	collection.insert({"id": i, "value": uuid.uuid4()})






