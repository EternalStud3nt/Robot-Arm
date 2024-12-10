from input.event import Event

class Grid:
    def __init__(self):
        # Create a 3x3 grid filled with empty spaces
        self.on_winner_detected = Event()
        self.on_turn_end = Event()
        self.objects = [[' ' for _ in range(3)] for _ in range(3)]
        
    def set_objects(self, cells):
        self.objects = cells

    def draw(self, row, col, symbol):
        if symbol not in ['X', 'O']:
            raise ValueError("Symbol must be 'X' or 'O'")
        self.objects[row][col] = symbol
        print(f"A player placed {symbol} at ({row}, {col})...")
        
        self.check_for_winner(True)
        self.on_turn_end.invoke()
        
    def check_for_winner(self, notify=False):
        # Check rows for a winner
        winner = None
        
        for row in self.objects:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                winner = row[0]
        
        # Check columns for a winner
        for col in range(3):
            if self.objects[0][col] == self.objects[1][col] == self.objects[2][col] and self.objects[0][col] != ' ':
                winner = self.objects[0][col]
        
        # Check diagonals for a winner
        if self.objects[0][0] == self.objects[1][1] == self.objects[2][2] and self.objects[0][0] != ' ':
            winner = self.objects[0][0]
        if self.objects[0][2] == self.objects[1][1] == self.objects[2][0] and self.objects[0][2] != ' ':
            winner = self.objects[0][2]
        
        if notify:
            if winner or self.is_grid_full():
                self.on_winner_detected.invoke(winner)
            
        if winner:
            return True
        else:
            return False
        
    def is_grid_full(self):
        for row in self.objects:
            for cell in row:
                if cell == ' ':
                    return False
        return True