from input.event import Event

class Grid:
    def __init__(self):
        # Create a 3x3 grid filled with empty spaces
        self.on_winner_detected = Event()
        self.on_turn_end = Event()
        self.rows = [[' ' for _ in range(3)] for _ in range(3)]
        
    def set_rows(self, rows):
        self.rows = rows
        
    def check_for_winner(self):       
        # Check rows for a winner
        winner = None
        
        for row in self.rows:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                winner = row[0]
        
        # Check columns for a winner
        for col in range(3):
            if self.rows[0][col] == self.rows[1][col] == self.rows[2][col] and self.rows[0][col] != ' ':
                winner = self.rows[0][col]
        
        # Check diagonals for a winner
        if self.rows[0][0] == self.rows[1][1] == self.rows[2][2] and self.rows[0][0] != ' ':
            winner = self.rows[0][0]
        if self.rows[0][2] == self.rows[1][1] == self.rows[2][0] and self.rows[0][2] != ' ':
            winner = self.rows[0][2]
            
        return winner
        
    def is_grid_full(self):
        for row in self.rows:
            for cell in row:
                if cell == ' ':
                    return False
        return True