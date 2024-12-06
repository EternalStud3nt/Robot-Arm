from  tic_tac_toe.AI import AI
from tic_tac_toe.grid import Grid
from tic_tac_toe.game_manager import GameManager
from robot_arm.arm_controller import ArmController
from robot_arm.robot_arm import RobotArm

if __name__ == "__main__":
    arm = RobotArm()

    try:
        depth = float(input("Enter depth: "))
        height = float(input("Enter height: "))
        rotation = float(input("Enter base rotation: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    else:
        arm.set_depth(depth)
        arm.set_height(height)
        arm.set_rotation_xz(rotation)
#     grid = Grid()
#     game_manager = GameManager()
#     ai = AI(1, game_manager, grid)
#     ai.test_set_positions()
    
#     # controller = ArmController()
    
    
#     # ai.grab_piece()
#     # from robot_arm.arm_controller import ArmController  
# #     from tic_tac_toe.game_manager import GameManager
# #     gameManager = GameManager()
# #     gameManager.start_game()