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

def debug_grab_coordinates():
    from tic_tac_toe.AI import AI
    from tic_tac_toe.grid import Grid
    from tic_tac_toe.game_manager import GameManager

    game_manager = GameManager()
    ai = game_manager.bot_player
    ai.debug_grab_coordinates()

def test_grid_digitizer():
    from tic_tac_toe.grid_digitizer import GridDigitizer
    digitizer = GridDigitizer()
    
    while(True):
        prompt = input("Press r to capture grid area, enter to capture grid state, or q to quit: ")
        if prompt == 'r':
            digitizer.capture_grid_area()
        elif prompt == '':
            digitizer.capture_grid_state()
            digitizer.display_grid_state()
        elif prompt == 'q':
            break
        else:
            print("Invalid input. Please try again.")

def execute_game_loop():
    from tic_tac_toe.grid_digitizer import GridDigitizer
    from tic_tac_toe.grid import Grid
    from tic_tac_toe.game_manager import GameManager

    game_manager = GameManager()
    game_manager.start_game()

def main():
    debug_grab_coordinates()
    
if __name__ == "__main__":
    main()