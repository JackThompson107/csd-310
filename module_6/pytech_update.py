#https://github.com/JackThompson107/csd-310
import pymongo
import json
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.t6xba6x.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
students=db["students"]

print("DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY")
docs = db.students.find({})
for doc in docs:
 print(doc)

#result = db.collection.update_one({"student_id": "1007"}, {"$set": {"last_name": "Smith"}})

result = db.collection.update_one(    {
        "student_id": "1007",
        "first_name": "Thorin",
        "last_name": "Oakenshield"
    }, {"$set": {        "student_id": "1007",
        "first_name": "Thorin", "last_name": "Smith"}})



updated_id = db.students.find_one(    { 
        "student_id": "1007"
    })
 
print("Updated last name: "+ str(updated_id["last_name"]))

print("End of program, press any key to exit...")