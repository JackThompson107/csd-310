#https://github.com/JackThompson107/csd-310
import pymongo
import json
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.t6xba6x.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
students=db["students"]

docs = db.students.find({})
for doc in docs:
 print(doc)

doc2 = db.students.find_one(    { 
        "student_id": "1008",
        "first_name": "Bilbo",
        "last_name": "Baggins"
    })
 
print(doc2["student_id"])
print(doc2["last_name"])

result = db.collection.update_one(    {
        "student_id": "1007",
        "first_name": "Thorin",
        "last_name": "Oakenshield"
    }, {"$set": {"last_name": "Smith"}})

updated_id = db.students.find_one(    { 
        "student_id": "1007"
    })