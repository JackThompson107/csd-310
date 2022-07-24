#https://github.com/JackThompson107/csd-310
import pymongo
import json
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.t6xba6x.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
students=db["students"]

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
docs = db.students.find({})
for doc in docs:
 print("Student ID: "+str(doc["student_id"]))
 print("First Name: "+str(doc["first_name"]))
 print("Last Name: "+str(doc["last_name"]))
 print("")

print("-- INSERT STATEMENTS --")
new_stu = students.insert_one({"student_id": "1010","first_name": "John","last_name": "Doe"})
new_id = new_stu.inserted_id
print("Inserted student record into the students collection with document_id: " + str(new_id))
new_stud = db.students.find_one(    { 
        "student_id": "1010"
    })
print("Student ID: "+str(new_stud["student_id"]))
print("First Name: "+str(new_stud["first_name"]))
print("Last Name: "+str(new_stud["last_name"]))
print("")

new_stud = db.students.delete_one(    { 
        "student_id": "1010"
    })

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
docs = db.students.find({})
for doc in docs:
 print("Student ID: "+str(doc["student_id"]))
 print("First Name: "+str(doc["first_name"]))
 print("Last Name: "+str(doc["last_name"]))
 print("")

print("End of program, press any key to exit...")