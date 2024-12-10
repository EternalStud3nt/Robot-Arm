from computer_vision.image_processor import ImageProcessor
from computer_vision.camera import Camera
from tic_tac_toe.grid import Grid

class GridDigitizer:
    def __init__(self):
        self.image_processor = ImageProcessor()
        self.camera = Camera()
        self.grid_area = None
        self.grid = Grid()

    def capture_grid_area(self):
        # Capture frame from camera
        frame = self.camera.get_feed_photo()
        
        if frame is None:
            print("Failed to capture image from camera.")
            return None
        
        # Detect objects in the frame
        objects = self.image_processor.detect_objects(frame)
        
        # Detect grid area
        cells = self.image_processor.filter_objects_by_name("Cell", objects)
        grid_area = self.image_processor.detect_grid_area(cells)
        
        self.grid_area = grid_area
        print("Grid area captured successfully.")

    def capture_grid_state(self):
        # returns all objects that are within the grid area
        def get_grid_objects():
            if(self.grid_area is None):
                print("Grid area is not initialized.")
                return None
        
            # Capture frame from camera
            frame = self.camera.get_feed_photo()
            
            if frame is None:
                print("Failed to capture image from camera.")
                return
            
            # Detect objects in the frame
            objects = self.image_processor.detect_objects(frame)
            
            # Filter objects within the grid area
            grid_objects = self.image_processor.filter_objects_within_grid(objects, self.grid_area)
            return grid_objects
        
        grid_objects = get_grid_objects()
        if grid_objects is None:
            return None
        else:
            grid_width = self.grid_area[1][0] - self.grid_area[0][0]
            grid_height = self.grid_area[1][1] - self.grid_area[0][1]
            cell_width = grid_width // 3
            cell_height = grid_height // 3
            
            symbols = [[' ' for _ in range(3)] for _ in range(3)]
            for obj in grid_objects:
                if(obj[0] == "X" or obj[0] == "O"):
                    x1, y1, x2, y2 = obj[1]
                    center = ((x1 + x2) // 2, (y1 + y2) // 2)
                    obj_row = (center[1] - self.grid_area[0][1]) // cell_height
                    obj_col = (center[0] - self.grid_area[0][0]) // cell_width
                    symbols[obj_row][obj_col] = obj[0]
                
            self.grid.set_state(symbols)
            
        
        return symbols

    def display_grid_state(self):
        for row in self.grid.objects:
            print(' | '.join(row))
            print('-' * 10)