from tic_tac_toe.grid import Grid
from tic_tac_toe.AI import AI
from tic_tac_toe.human_player import HumanPlayer
from input.event import Event
from tic_tac_toe.grid_digitizer import GridDigitizer

class GameManager:
    def __init__(self):
        # Create grid instance
        self.grid = Grid()
        
        # Subscribe to grid events
        self.grid.on_turn_end.subscribe(self.on_move_completed)
        self.grid.on_winner_detected.subscribe(self.on_winner_detected)
        
        # Define player symbols
        self.human_player_symbol = 'X'
        self.bot_player_symbol = 'O'
        
        self.grid_digitizer = GridDigitizer()
        
        # Create player instances
        self.bot_player = AI("bot", self)
        self.bot_player.on_move_completed.subscribe(self.on_move_completed)
        self.human_player = HumanPlayer("human", self)
        self.human_player.on_move_completed.subscribe(self.on_move_completed)
        
        # Initialize game state
        self.winner = None
        self.player_turn = None
        self.game_over = False
        
        
    def start_game(self):
        input("Capturing grid area. Press Enter when ready...")
        self.grid_digitizer.capture_grid_area()
        self.grid = self.grid_digitizer.capture_grid_state()
        self.grid_digitizer.display_grid_state()
        print("Grid area captured successfully!")
        
        self.player_turn = "human"
        print(f"Player {self.player_turn} starts the game!")
        self.human_player.make_move()
        
    def on_move_completed(self):
        self.grid = self.grid_digitizer.capture_grid_state()
        self.grid_digitizer.display_grid_state()
        
        winner = self.grid.check_for_winner()
        if winner:
            self.on_winner_detected(winner)
            return
        elif self.grid.is_grid_full():
            self.on_grid_full()
            return
        
        self.player_turn = "bot" if self.player_turn == "human" else "human"
        if(self.player_turn == "human"):
            self.human_player.make_move()
        elif self.player_turn == "bot":
            self.bot_player.make_move()
    
    def on_winner_detected(self, winner):
        print(f"{winner} wins!")
        self.game_over = True
    
    def on_grid_full(self):
        print("It's a tie!")
        self.game_over = True

