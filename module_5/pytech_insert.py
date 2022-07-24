#https://github.com/JackThompson107/csd-310
import pymongo
import json
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.t6xba6x.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
students=db["students"]

new_students = [
    {
        "student_id": "1007",
        "first_name": "Thorin",
        "last_name": "Oakenshield"
    },
    { 
        "student_id": "1008",
        "first_name": "Bilbo",
        "last_name": "Baggins"
    },
    {
        "student_id": "1009",
        "first_name": "Frodo",
        "last_name": "Baggins"
    }
]
for new_student in new_students:
    new_id = students.insert_one(new_student).inserted_id
    print("Inserted student record " + str(new_id))

print("End of program, press any key to exit...")