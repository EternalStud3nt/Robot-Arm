import os
import platform

if platform.system() != 'Windows':
    from robot_arm.arm_controller import ArmController
    from robot_arm.robot_arm import RobotArm
    from tic_tac_toe.AI import AI
    from tic_tac_toe.grid import Grid
    from tic_tac_toe.game_manager import GameManager
    from tic_tac_toe.AI import AI
    from tic_tac_toe.grid import Grid
    from tic_tac_toe.game_manager import GameManager

def control_robot():
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
    grid = Grid()
    game_manager = GameManager()
    ai = AI(1, game_manager, grid)
    ai.test_set_positions()

def start_camera_stream():
    from computer_vision.camera import Camera
    from computer_vision.image_processor import ImageProcessor
    import cv2
    
    # Create the camera and image processor objects
    camera = Camera()
    processor = ImageProcessor()
    
    # Get the live feed from the camera and process each frame, then display it in a window
    for frame in camera.get_feed_video():
        processed_frame = processor.draw_objects(frame)
        cv2.imshow("Live Feed", processed_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    camera.release()
    
if __name__ == "__main__":
    #controller = ArmController()
    #control_robot()
    #test_robot_positioning()
    #capture_photos()
    start_camera_stream()
    pass