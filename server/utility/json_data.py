import os
import json
from storage.user import User

class JsonData:
    @staticmethod
    def object_to_user(data):
        # if object cannot be converted into a User Class then exit early
        if "name" not in data and "password" not in data:
            return data
        
        # return User Class object
        return User(data["email"], data["name"], data["password"], data["balance"])

    @staticmethod
    def load_from_json(json_file):
        data = {}
        
        # check if json file exists
        file_exists = os.path.exists(json_file)
        
        # if exists then we dont have to do anything yet
        # since when a new user is created it will create the json anyways
        if not file_exists:
            return data
        
        # if file already exists, open json file and load json_file into 
        # dictionary, using helper function of object_to_user(data) 
        # which turns a dictionary into a user class object
        with open(json_file, "r") as file:
            data = json.load(file, object_hook=JsonData.object_to_user)  
        
        return data
     
    @staticmethod
    def save(data, json_file_path="storage.json"):
        # get all user class objects and turn them into dictionary style
        # User(username=robert_cacho, password=password123, balance=403)
        # will turn into because of the __dict__ function which turns objects into dictionaries
        # {"username": "robert_cacho", "password": "password123", "balance": 403}
        new_data = {}
        for key, val in data.items():
            new_data[key] = val.__dict__
        
        with open(json_file_path, "w+") as outfile:
            json.dump(new_data, outfile)