from tic_tac_toe.grid import Grid

class Player:
    def __init__(self, id, game_manager, grid):
        self.id = id
        self.game_manager = game_manager
        self.grid = grid
        self.symbol = None
        
        if(self.id == "human"):
            self.symbol = self.game_manager.human_player_symbol
        elif(self.id == "bot"):
            self.symbol = self.game_manager.bot_player_symbol
            
        self.game_manager.on_move_requested.subscribe(self.on_move_requested)
            
        
    def draw(self, row, col):
        self.grid.draw(row, col, self.symbol)
        
    def on_move_requested(self, player_turn):
        if player_turn == self.id:
            self.move()

    def move(self):
        raise NotImplementedError("Subclasses should implement this method.")