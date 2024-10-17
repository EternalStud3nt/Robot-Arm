from input.event import Event

class Grid:
    def __init__(self):
        # Create a 3x3 grid filled with empty spaces
        self.on_winner_detected = Event()
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]

    def draw(self, row, col, symbol):
        if symbol not in ['X', 'O']:
            raise ValueError("Symbol must be 'X' or 'O'")
        self.grid[row][col] = symbol
        self.check_for_winner()
        
    def check_for_winner(self):
        # Check rows for a winner
        winner = None
        
        for row in self.grid:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                winner = row[0]
        
        # Check columns for a winner
        for col in range(3):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] and self.grid[0][col] != ' ':
                winner = self.grid[0][col]
        
        # Check diagonals for a winner
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0] != ' ':
            winner = self.grid[0][0]
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[0][2] != ' ':
            winner = self.grid[0][2]
        
        
        if(winner):
            self.on_winner_detected(winner)