from werkzeug.security import check_password_hash
from storage.user import User
from utility.json_data import JsonData
from storage.room import Room
import string
import random

class Storage:
    def __init__(self, game, json_file="storage.json"):
        self.file = json_file
        self.game = game
        self.rooms = {}
        self.users = JsonData.load_from_json(json_file)
            
    def user_exists(self, user):
            return user in self.users   

    def authenticate(self, user, password):
        if not self.user_exists(user):
            return {"status": "Incorrect username or password"}
        
        if check_password_hash(self.users[user].password, password):
            data = self.users[user].get_info()
            data["success"] = True
            return data

        return {"error": "Invalid password"}

    def user_in_room(self, user):
        for room_id, room in self.rooms.items():
            if user in room.get_players():
                return {room_id: user}
        return False

    # getters 
    def get_users(self):
        # turning class into json object
        json_object = { k: v.get_info() for (k,v) in self.users.items() }
        return json_object

    def get_rooms(self):
        # turning class into json object
        json_object = { k: v.get_info() for (k,v) in self.rooms.items() }
        return json_object

    # setters
    def create_user(self, email, user, password):
        if self.user_exists(user):
            return {"status": "User already exists"}
        self.users[user] = User(email, user, password, 300)
        self.save()

        data = self.users[user].get_info()
        data["success"] = True
        return data

    def delete_user(self, user):
        deleted_user = self.users.pop(user, {"error": "User not found"})
        self.save()
        return deleted_user
    
    def update_balance(self, user, balance):
        if not self.user_exists(user):
            return {"status": "Cannot update balance: User doesnt exist"}
        
        self.users[user].set_balance(balance)
        self.save()

    def create_room(self, user, id):
        if not self.user_exists(user):
            print("error creating a room")
            return {"status": f"Could not create a room for {user}"}
        
        self.rooms[id] = Room(user, id)
        return self.rooms[id].get_info()

    def room_exists(self, room_id):
        return room_id in self.rooms

    def join_room(self, user, id):
        if not self.room_exists(id):
            return False
        
        joined_successfully = self.rooms[id].add_player(user)
        
        # joined_successfully can either be True or False
        return joined_successfully

    def get_room(self, room_id):
        return self.rooms[room_id]
        
    def leave_room(self, user_id, room_id):
        return self.rooms[room_id].remove_player(user_id)
        
    
    def save(self):
        JsonData.save(self.users, self.file)