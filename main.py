import os
import platform

def control_robot():
    from robot_arm.robot_arm import RobotArm
    
    if platform.system() == 'Windows':
        print("Robot control is not supported on Windows.")
        return

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
    from tic_tac_toe.AI import AI
    from tic_tac_toe.grid import Grid
    grid = Grid()
    ai = AI(1, None, grid)
    ai.test_grab()

def execute_game_loop():
    from tic_tac_toe.grid_digitizer import GridDigitizer
    from tic_tac_toe.grid import Grid
    from tic_tac_toe.game_manager import GameManager

    game_manager = GameManager()
    
    game_manager.start_game()

def main():
    execute_game_loop()
    
if __name__ == "__main__":
    main()