class Room:
    def __init__(self, owner_id, game_id):
        self.owner = owner_id
        self.id = game_id
        self.symbols = ["O"]
        self.players = {owner_id: "X"}
        
    def get_id(self):
        return self.id
    
    def get_players(self):
        return self.players        
        
    def in_room(self, player: str):
        return player in self.players
    
    def add_player(self, player: str):
        if self.in_room(player):
            return False
        
        if len(self.symbols) == 0:
            return False

        self.players[player] = self.symbols.pop()
        return True    
        
    def remove_player(self, player: str):
        del self.players[player]
        return True
    
    def get_owner(self):
        return self.owner

    def get_info(self):
        return {"channel": self.id, "players": self.players, "symbols": self.symbols }