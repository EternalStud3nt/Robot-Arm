from tic_tac_toe.player import Player

class HumanPlayer(Player):
    def __init__(self,id, game_manager):
        super().__init__(id, game_manager)

    def make_move(self):
        input("Press Enter when you have made your move...")
        self.on_move_completed.invoke()
