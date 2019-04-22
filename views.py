from flask import render_template, request

from models import Dog
from app import app
import json



@app.route('/dogs',methods = ['POST', 'GET'])
def Dogs():
    dogs = Dog()
    if request.method == "GET":
        return dogs.getAllDogs()
    elif request.method == "POST":
        print request.json.keys()
        name = request.json["name"] 
        notes = request.json["notes"]
        owner = request.json["owner"]
        print name,notes,owner
        dogs.insert(0,name,notes,owner)
        return json.dumps({"sucess": True})

@app.route('/dogs/<int:dog_id>', methods = ["GET","PUT","DELETE"])
def dog(dog_id):
    dog = Dog()
    if request.method == "GET":
        return dog.getDog(dog_id)
    if request.method == "PUT":
        print request.json
        Name = request.json["name"] 
        Notes = request.json["notes"]
        Owner = request.json["owner"]
        dog.update(dog_id,Name,Notes,Owner)
        return json.dumps({"sucess": True})
    if request.method == "DELETE":
        dog.deleteDog(dog_id)
        return json.dumps({"sucess": True})