from tic_tac_toe.player import Player


class HumanPlayer(Player):
    def __init__(self,id, game_manager, grid):
        super().__init__(id, game_manager, grid)

    def move(self):
        while True:
            try:
                row, col = map(int, input(f"Enter your move (row,col): ").split(','))
                if self.grid.cells[row][col] != ' ':
                    print("Cell is already occupied. Try again.")
                    continue
                self.grid.draw(row, col, self.symbol)
                break
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column as numbers between 0 and 2.")