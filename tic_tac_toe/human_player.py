from tic_tac_toe.player import Player


class HumanPlayer(Player):
    def __init__(self,id, game_manager, grid):
        super().__init__(id, game_manager, grid)

    def make_move(self):
        old_grid = self.grid.cells
        