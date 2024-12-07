import time
import random
from tic_tac_toe.player import Player
from robot_arm.robot_arm import RobotArm


class AI(Player):
    def __init__(self, id, game_manager, grid):
        super().__init__(id, game_manager, grid)
        
        self.arm = RobotArm()
        self.grab_index = 0
        self.grab_coordinates = [[11, 0.5, -49], [13.8, 0.5, -49], [7.5, 0.5, 45], [10, 0.5, 42]]
        self.grid_cell_coordinates = [
            # Lower row
            [[7.50, 1.26, 37.53], [6.15, 1.55, 16.83], [6.47, 1.09, -2.76]],
            # Middle row
            [[10.86, 1.66, 29.22], [10.53, 1.28, 14.61], [9.95, 1.16, -1.44]],
            # Upper row
            [[13.80, 0.75, 23.96], [14.20, 0.45, 12.51], [13.50, 1.30, -2.16]]
        ]

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
        grab_position = self.grab_coordinates[self.grab_index]
        
        # Open the grip, move to the grab position with a height offset, close the grip and lift the piece
        self.arm.set_grip(70)
        time.sleep(1)
        self.arm.set_position(grab_position[0], grab_position[1] + 2, grab_position[2])
        time.sleep(1)
        self.arm.set_position(grab_position[0], grab_position[1], grab_position[2])
        time.sleep(1)
        self.arm.set_grip(30)
        time.sleep(1.5)
        self.arm.move_upwards(3)
        
    def release_piece(self):
        self.arm.set_grip(42)
        
        
    def test_set_positions(self):
        for row in range(3):
            for col in range(3):
                # grab a piece
                self.grab_piece()
                
                # move above the grid cell
                grid_position = self.grid_cell_coordinates[row][col]
                self.arm.set_position(grid_position[0], grid_position[1] + 2, grid_position[2])
                time.sleep(1)
                
                # move down to the grid cell
                self.arm.set_position(grid_position[0], grid_position[1], grid_position[2])
                time.sleep(1)
                
                # release the piece
                self.release_piece()
                time.sleep(1)
                
                # move up
                self.arm.move_upwards(3)
                
                self.grab_index = (self.grab_index + 1) % len(self.grab_coordinates)
                
        