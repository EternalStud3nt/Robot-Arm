import os
import platform

if platform.system() != 'Windows':
    from robot_arm.arm_controller import ArmController
    from robot_arm.robot_arm import RobotArm
    from tic_tac_toe.AI import AI
    from tic_tac_toe.grid import Grid
    from tic_tac_toe.grid_digitizer import GridDigitizer

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
    ai = AI(1, None, grid)
    ai.test_set_positions()

def start_camera_stream():
    from computer_vision.camera import Camera
    from computer_vision.image_processor import ImageProcessor
    import cv2
    
    # Create the camera and image processor objects
    camera = Camera()
    processor = ImageProcessor()
    
    # Get the live feed from the camera and process each frame, then display it in a window
    frame_0 = camera.get_feed_photo()
    
    # Get the grid area
    objects = processor.detect_objects(frame_0)
    cells = processor.filter_objects_by_name("Cell", objects)
    grid_area = processor.detect_grid_area(cells)
        
    for frame in camera.get_feed_video():
        objects = processor.detect_objects(frame)
        
        # Draw the grid and objects on the processed frame
        objects_in_grid = processor.filter_objects_within_grid(objects, grid_area)
        processed_frame = processor.draw_grid_and_objects(frame, grid_area, objects_in_grid)
        
        cv2.imshow("Live Feed", processed_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    camera.release()

def test_grid_translation():
    from tic_tac_toe.grid_digitizer import GridDigitizer
    from tic_tac_toe.grid import Grid
    
    grid_translator = GridDigitizer()
    grid = Grid()
    
    while True:
        key = input("Press 'r' to initialize grid, 'enter' to display grid, 'q' to quit: ").strip().lower()
        if key == 'q':
            break
        elif key == 'r':
            grid_translator.initialize_grid_area()
        elif key == '':
            cells = grid_translator.detect_grid_state()
            if cells:
                grid.set_state(cells)
                grid_translator.display_grid(grid)

def main():
    #start_camera_stream()
    pass
    
if __name__ == "__main__":
    main()