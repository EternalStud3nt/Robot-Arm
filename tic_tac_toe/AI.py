import time
import random
from tic_tac_toe.player import Player
from robot_arm.robot_arm import RobotArm
from tic_tac_toe.grid import Grid


class AI(Player):
    def __init__(self, id, game_manager):
        super().__init__(id, game_manager)
        
        self.arm = RobotArm()
        self.grab_index = 0
        self.grab_coordinates = [[8.9, 0.2, -42.8], [12.6, 0.2, -42.2], [9.1, 0.2, 55.3], [12.3, 0.2, 53]]
        self.grid_cell_coordinates = [
            # Lower row
            [[6, 1.25, 26], [4.6, 1.25, 6], [6.5, 1.25, -16]],
            # Middle row
            [[9.5, 1.25, 21], [9, 1.25, 4], [9.5, 1.25, -13]],
            # Upper row
            [[13, 1.25, 17], [13, 3], [13, 1.25, -10]]
        ]
        
        self.reset_arm_position()

    def make_move(self):
        (row, col) = self.calculate_best_move(self.game_manager.grid, self.symbol)
        self.place_object_to_grid(row, col)
            
    def calculate_best_move(self, grid, symbol):
        opponent_symbol = 'O' if symbol == 'X' else 'X'
        
        # Check if AI can win in the next move
        for row in range(3):
            for col in range(3):
                if grid.elements[row][col] == ' ':
                    elements = [r[:] for r in grid.elements]
                    elements[row][col] = symbol
                    new_grid = Grid()
                    new_grid.set_objects(elements)
                    if new_grid.check_for_winner():
                        return row, col
        
        # Check if opponent can win in the next move and block them
        for row in range(3):
            for col in range(3):
                if grid.elements[row][col] == ' ':
                    elements = [r[:] for r in grid.elements]
                    elements[row][col] = opponent_symbol
                    new_grid = Grid()
                    new_grid.set_objects(elements)
                    if new_grid.check_for_winner():
                        return row, col
        
        # Place symbol in a random available cell
        available_moves = [(row, col) for row in range(3) for col in range(3) if grid.elements[row][col] == ' ']
        return random.choice(available_moves)
        
    def place_object_to_grid(self, row, col):
        self.grab_piece()
        time.sleep(0.5)
        pos = self.grid_cell_coordinates[row][col]
        self.arm.set_position(pos[0], pos[1] + 2, pos[2])
        time.sleep(0.5)
        self.arm.set_position(pos[0], pos[1] + 0.3, pos[2])
        time.sleep(0.5)
        self.release_piece()
        time.sleep(0.5)
        self.reset_arm_position()
        time.sleep(0.5)
        self.on_move_completed.invoke()

    def reset_arm_position(self):
        self.arm.set_position(8, 8, 90)
        
    def grab_piece(self):
        grab_position = self.grab_coordinates[self.grab_index]
        
        # Open the grip, move to the grab position with a height offset, close the grip and lift the piece
        self.arm.set_grip(20)
        time.sleep(1)
        self.arm.set_position(grab_position[0] - 2, grab_position[1] + 2, grab_position[2])
        time.sleep(1)
        self.arm.set_position(grab_position[0] - 2, grab_position[1], grab_position[2])
        time.sleep(1)
        self.arm.set_position(grab_position[0], grab_position[1], grab_position[2])
        time.sleep(1)
        self.arm.set_grip(5)
        time.sleep(1.5)
        self.arm.set_position(6, 8, 0)
        
        self.grab_index = (self.grab_index + 1) % len(self.grab_coordinates)
        
    def release_piece(self):
        self.arm.set_grip(25)
        
    def debug_grab_coordinates(self):
        while True:
            input("Press Enter to grab the next piece...")
            self.grab_piece()

    def debug_grid_cell_coordinates(self):
        while True:
            for row_index, row in enumerate(self.grid_cell_coordinates):
                for col_index, cell in enumerate(row):
                    self.place_object_to_grid(row_index, col_index)
            self.reset_arm_position()
            time.sleep(1)

