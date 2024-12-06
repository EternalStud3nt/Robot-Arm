import time
import random
from tic_tac_toe.player import Player
from robot_arm.robot_arm import RobotArm


class AI(Player):
    def __init__(self, id, game_manager, grid):
        super().__init__(id, game_manager, grid)
        
        self.arm = RobotArm()
        self.grab_index = 0
        self.grap_positions = [[0, 0, 0]]
        self.grid_positions = [[1, 1, 1]]

    def make_move(self):
        def calculate_next_move():
            # Check if AI can win in the next move
            for row in range(3):
                for col in range(3):
                    if self.grid.cells[row][col] == ' ':
                        self.grid.cells[row][col] = self.symbol
                        if self.grid.check_for_winner():
                            return row, col
                        self.grid.cells[row][col] = ' '

            # Check if opponent can win in the next move and block them
            opponent_symbol = 'O' if self.symbol == 'X' else 'X'
            for row in range(3):
                for col in range(3):
                    if self.grid.cells[row][col] == ' ':
                        self.grid.cells[row][col] = opponent_symbol
                        if self.grid.check_for_winner():
                            self.grid.cells[row][col] = self.symbol
                            return row, col
                        self.grid.cells[row][col] = ' '

            # Otherwise, choose a random empty cell
            empty_cells = []
            for row in range(3):
                for col in range(3):
                    if self.grid.cells[row][col] == ' ':
                        empty_cells.append((row, col))
            
            random_cell = random.choice(empty_cells)
            return random_cell

        row, col = calculate_next_move()
        self.draw(row, col)
        
    def grab_piece(self):
        grab_position = self.grab_positions[self.grab_index]
        
        # Open the grip, move to the grab position with a height offset, close the grip and lift the piece
        self.arm.set_grip(70)
        time.sleep(0.2)
        self.arm.set_position(grab_position[0], grab_position[1] + 2, grab_position[2])
        time.sleep(0.2)
        self.arm.set_position(grab_position[0], grab_position[1], grab_position[2])
        time.sleep(0.5)
        self.arm.move_forwards(0.3)
        time.sleep(0.5)
        self.arm.set_grip(30)
        self.arm.move_upwards(3)
        