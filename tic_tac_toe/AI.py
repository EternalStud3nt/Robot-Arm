from player import Player
import random

class AI(Player):
    def __init__(self, symbol, grid):
        super().__init__(symbol, grid)

    def calculate_next_move(self):
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