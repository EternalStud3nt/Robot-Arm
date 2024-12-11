from input.event import Event

class Grid:
    def __init__(self):
        # Create a 3x3 grid filled with empty spaces
        self.on_winner_detected = Event()
        self.on_turn_end = Event()
        self.boxes = [[' ' for _ in range(3)] for _ in range(3)]
        
    def set_objects(self, boxes):
        self.boxes = boxes
        
    def check_for_winner(self):       
        # Check rows for a winner
        winner = None
        
        for row in self.boxes:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                winner = row[0]
        
        # Check columns for a winner
        for col in range(3):
            if self.boxes[0][col] == self.boxes[1][col] == self.boxes[2][col] and self.boxes[0][col] != ' ':
                winner = self.boxes[0][col]
        
        # Check diagonals for a winner
        if self.boxes[0][0] == self.boxes[1][1] == self.boxes[2][2] and self.boxes[0][0] != ' ':
            winner = self.boxes[0][0]
        if self.boxes[0][2] == self.boxes[1][1] == self.boxes[2][0] and self.boxes[0][2] != ' ':
            winner = self.boxes[0][2]
            
        return winner
        
    def is_grid_full(self):
        for row in self.boxes:
            for cell in row:
                if cell == ' ':
                    return False
        return True