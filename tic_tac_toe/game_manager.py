from tic_tac_toe.grid import Grid
from tic_tac_toe.AI import AI
from tic_tac_toe.human_player import HumanPlayer
from input.event import Event
from computer_vision.image_processor import ImageProcessor
import cv2
from computer_vision.camera import Camera
from tic_tac_toe.grid_digitizer import GridDigitizer

class GameManager:
    def __init__(self):
        # Create grid instance
        self.grid = Grid()
        self.grid.on_turn_end.subscribe(self.on_turn_over)
        self.grid.on_winner_detected.subscribe(self.on_winner_detected)
        
        # Create event for move requests
        self.on_move_requested = Event()
        
        # Define player symbols
        self.human_player_symbol = 'X'
        self.bot_player_symbol = 'O'
        
        # Create player instances
        self.bot_player = AI("bot", self, self.grid)
        self.human_player = HumanPlayer("human", self, self.grid)
        
        # Initialize game state
        self.winner = None
        self.player_turn = None
        self.game_over = False
        
        self.image_processor = ImageProcessor()
        self.camera = Camera()
        
        self.grid_translator = GridDigitizer()
        
    def display_grid(self):
        self.grid_translator.display_grid_state(self.grid)
            
    def on_turn_over(self):
        if self.game_over:
            return
        
        self.display_grid()
        
        if self.player_turn == None:
            print("Human starts with the first move...")
            self.player_turn = "human"
        
        else:
            if self.player_turn == "human":
                self.player_turn = "bot"
            elif self.player_turn == "bot":
                self.player_turn = "human"
        
        self.on_move_requested.invoke(self.player_turn)
        
    def on_winner_detected(self, winner_symbol):
        self.display_grid()
        self.game_over = True
        
        if winner_symbol == self.human_player_symbol:
            print("Human wins!")
            self.winner = "human"
        elif winner_symbol == self.bot_player_symbol:
            print("Bot wins!")
            self.winner = "bot"
        else:
            print("It's a draw!")
        
    def start_game(self):
        self.on_turn_over()

