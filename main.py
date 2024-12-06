from  tic_tac_toe.AI import AI
from tic_tac_toe.grid import Grid
from tic_tac_toe.game_manager import GameManager

if __name__ == "__main__":
    grid = Grid()
    game_manager = GameManager()
    ai = AI(1, game_manager, grid)
    
    ai.grab_piece()
    # from robot_arm.arm_controller import ArmController  
    # controller = ArmController()
#     from tic_tac_toe.game_manager import GameManager
#     gameManager = GameManager()
#     gameManager.start_game()