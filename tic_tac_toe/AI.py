import time
import random
from tic_tac_toe.player import Player
from robot_arm.robot_arm import RobotArm


class AI(Player):
    def __init__(self, id, game_manager, grid):
        super().__init__(id, game_manager, grid)
        
        self.arm = RobotArm()
        self.grab_index = 0
        self.grab_coordinates = [[9.36, -4.09, -44.42], [13.03, -4.39, -42.40], [9.09, -3.96, 54.40], [12.34, -3.84, 48.79]]
        self.grid_cell_coordinates = [
            # Lower row
            [[8.90, -3.57, 19.27], [8.35, -3.11, 2.59], [9.29, -3.30, -13.30]],
            # Middle row
            [[10.28, -3.20, 17.43], [10.89, -3.56, 4.77], [10.90, -3.30, -9.57]],
            # Upper row
            [[13.65, -3.63, 15.49], [12.08, -3.35, 1.39], [13.78, -3.39, -9.89]]
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
        self.arm.set_position(grab_position[0]-0.5, grab_position[1] + 3, grab_position[2])
        time.sleep(1)
        self.arm.set_position(grab_position[0], grab_position[1], grab_position[2])
        time.sleep(1)
        self.arm.move_forwards(1)
        time.sleep(1)
        self.arm.set_grip(30)
        time.sleep(1.5)
        self.arm.move_upwards(3)
        
    def release_piece(self):
        self.arm.set_grip(42)
        
        
    def test_set_positions(self):
        for row in range(3):
            for col in range(3):
                self.grab_piece()
                grid_position = self.grid_cell_coordinates[row][col]
                self.arm.set_position(grid_position[0], grid_position[1] + 2, grid_position[2])
                time.sleep(1)
                self.arm.set_position(grid_position[0], grid_position[1]+0.5, grid_position[2])
                time.sleep(1)
                self.release_piece()
                time.sleep(1)
                self.arm.move_upwards(3)
                self.grab_index = (self.grab_index + 1) % len(self.grab_coordinates)
                
        