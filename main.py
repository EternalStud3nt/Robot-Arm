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

def capture_photos():
    from computer_vision.camera import Camera
    camera = Camera()
    
    base_folder = "data/ml_photos"
    subfolder_index = 1
    while os.path.exists(os.path.join(base_folder, f"session_{subfolder_index}")):
        subfolder_index += 1
    session_folder = os.path.join(base_folder, f"session_{subfolder_index}")
    os.makedirs(session_folder)

    photo_index = 0
    while True:
        if input("Press 'q' to quit, any other key to capture photo: ") == 'q':
            break
        else:
            photo_index += 1
            camera.capture_photo(f"ml_photo_{photo_index}", session_folder, True)
    camera.release()

def start_camera_stream():
    from computer_vision.camera import Camera
    from ultralytics import YOLO

    camera = Camera()
    model = YOLO("last.pt")
    camera.start_live_feed(model)

def find_objects_in_image(image_path):
    from ultralytics import YOLO
    import cv2

    model = YOLO("last.pt")  # Load your custom-trained model
    image = cv2.imread(image_path)
    results = model.predict(image_path, save=True, show=True)

    
if __name__ == "__main__":
    #controller = ArmController()
    #control_robot()
    #test_robot_positioning()
    #capture_photos()
    start_camera_stream()
    pass