import json

class Dog(object):
    def __init__(self):
        with open("dogs.json","r") as data:
            self.db = json.load(data)
    def insert(self,dog_id,name,notes,owner):
        if str(dog_id) not in self.db["data"].keys():
            self.db["data"][dog_id] = {
                "name":name,
                "notes":notes,
                "owner":owner,
            }
            self.writeToDB()
        else:
            self.insert(dog_id+1,name,notes,owner)
    def writeToDB(self):
        with open("dogs.json","w") as data:
            json.dump(self.db,data)
        
    
    def update(self,dog_id,name=None,notes=None,owner=None):
        print name,notes,owner
        if name!=None:
            self.db["data"][str(dog_id)]["name"] = name
        if notes!=None:
            self.db["data"][str(dog_id)]["notes"] = notes
        if owner!=None:
            self.db["data"][str(dog_id)]["owner"] = owner
        self.writeToDB()

    def getDog(self,dog_id):
        return json.dumps(self.db["data"][str(dog_id)])
    def getAllDogs(self):
        return json.dumps(self.db["data"])
    def deleteDog(self,dog_id):
        del(self.db["data"][str(dog_id)])
        self.writeToDB()


    