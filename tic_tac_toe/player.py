from grid import Grid

class Player:
    def __init__(self, symbol, grid):
        self.symbol = symbol
        self.grid = grid
        
    def draw(self, row, col):
        self.grid.draw(row, col, self.symbol)