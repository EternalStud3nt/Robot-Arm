from input.event import Event

class Grid:
    def __init__(self):
        # Create a 3x3 grid filled with empty spaces
        self.on_winner_detected = Event()
        self.cells = [[' ' for _ in range(3)] for _ in range(3)]

    def draw(self, row, col, symbol):
        if symbol not in ['X', 'O']:
            raise ValueError("Symbol must be 'X' or 'O'")
        self.cells[row][col] = symbol
        self.check_for_winner()
        
    def check_for_winner(self, notify=False):
        # Check rows for a winner
        winner = None
        
        for row in self.cells:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                winner = row[0]
        
        # Check columns for a winner
        for col in range(3):
            if self.cells[0][col] == self.cells[1][col] == self.cells[2][col] and self.cells[0][col] != ' ':
                winner = self.cells[0][col]
        
        # Check diagonals for a winner
        if self.cells[0][0] == self.cells[1][1] == self.cells[2][2] and self.cells[0][0] != ' ':
            winner = self.cells[0][0]
        if self.cells[0][2] == self.cells[1][1] == self.cells[2][0] and self.cells[0][2] != ' ':
            winner = self.cells[0][2]
        
        if winner:
            if notify:
                self.on_winner_detected(winner)
            return True
        else:
            return False