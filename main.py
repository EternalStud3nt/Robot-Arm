from  tic_tac_toe.AI import AI
from tic_tac_toe.grid import Grid
from tic_tac_toe.game_manager import GameManager
from robot_arm.arm_controller import ArmController
from robot_arm.robot_arm import RobotArm

def control_robot():
    arm = RobotArm()
    while True:
        try:
            depth = float(input("Enter depth: "))
            height = float(input("Enter height: "))
            rotation = float(input("Enter base rotation: "))
            close = input("Enter any key to close grip, none to open")
            if close:
                arm.set_grip(8)
            else:
                arm.set_grip(30)
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        else:
            arm.set_position(depth, height, rotation)

def test_robot_positioning():
    grid = Grid()
    game_manager = GameManager()
    ai = AI(1, game_manager, grid)
    ai.test_set_positions()

if __name__ == "__main__":
    #controller = ArmController()
    control_robot()
    #test_robot_positioning()