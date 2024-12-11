from input.event import Event

class Grid:
    def __init__(self):
        # Create a 3x3 grid filled with empty spaces
        self.on_winner_detected = Event()
        self.on_turn_end = Event()
        self.elements = [[' ' for _ in range(3)] for _ in range(3)]
        
    def set_objects(self, elements):
        self.elements = elements
        
    def check_for_winner(self):       
        # Check rows for a winner
        winner = None
        
        for row in self.elements:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                winner = row[0]
        
        # Check columns for a winner
        for col in range(3):
            if self.elements[0][col] == self.elements[1][col] == self.elements[2][col] and self.elements[0][col] != ' ':
                winner = self.elements[0][col]
        
        # Check diagonals for a winner
        if self.elements[0][0] == self.elements[1][1] == self.elements[2][2] and self.elements[0][0] != ' ':
            winner = self.elements[0][0]
        if self.elements[0][2] == self.elements[1][1] == self.elements[2][0] and self.elements[0][2] != ' ':
            winner = self.elements[0][2]
            
        return winner
        
    def is_grid_full(self):
        for row in self.elements:
            for cell in row:
                if cell == ' ':
                    return False
        return True