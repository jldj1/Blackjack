from flask import Flask, jsonify
from routes.auth import auth
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from db.database import storage_db
from utility.tools import Tools
application = Flask(__name__)
application.config["SECRET_KEY"] = "ASLJKDKALSD!"

socketio = SocketIO(application)

application.register_blueprint(auth, url_prefix="/auth")

@application.route("/", methods=["GET"])
def home_page():
    return jsonify({"success": "HELLO CLASS"})

@socketio.on("move")
def handleMove(data):
    print("Got message:", data)
    room_id = data["channel"]
    emit("move", data, room=room_id)

@socketio.on("leave_room")
def leaveRoom(data):
    room_id = data["channel"]
    user_id = data["player_name"]
    leave_room(room_id)
    storage_db.leave_room(user_id, room_id)
    
@socketio.on("join")
def syncGame(data):
    # data being passed in
    # data{"channel": channel_id, "player_name": player trying to join}
    
    # extracting channel id and player name
    room_id = data["channel"]
    player_name = data["player_name"]
    
    # boolean to check if player is trying to join a new room
    is_new_room = not storage_db.room_exists(room_id)

    # if room id is new then create a room for it else add player to already existing room
    if is_new_room:
        storage_db.create_room(player_name, room_id)
    else:
        joined_successfully = storage_db.join_room(player_name, room_id)
        
        # if did not join successfully then create a new room 
        if not joined_successfully:
            room_id = Tools.get_random_id(5)
            storage_db.create_room(player_name, room_id)
        
    room = storage_db.get_room(room_id)
    
    join_room(room_id)
    
    # emit("sync_game", game_state, broadcast=True)
    emit("sync_game", room.get_info(), room=room_id)

if __name__ == "__main__":
    
    # if production make sure to have host=0.0.0.0
    #socketio.run(application, host='0.0.0.0')
    # if running locally make sure to not have that
    socketio.run(application, debug=True)
