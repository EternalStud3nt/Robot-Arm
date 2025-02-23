from input.event import Event

class Player:
    def __init__(self, id, game_manager):
        self.id = id
        self.game_manager = game_manager
        self.on_move_completed = Event()
        self.symbol = None
        
        if(self.id == "human"):
            self.symbol = self.game_manager.human_player_symbol
        elif(self.id == "bot"):
            self.symbol = self.game_manager.bot_player_symbol            


    def make_move(self):
        raise NotImplementedError("Subclasses should implement this method.")