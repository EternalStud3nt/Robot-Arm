from computer_vision.image_processor import ImageProcessor
from computer_vision.camera import Camera

class GridDigitizer:
    def __init__(self):
        self.image_processor = ImageProcessor()
        self.camera = Camera()
        self.grid_area = None

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

    def detect_grid_state(self):
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
        else
            
        
        return cells

    def display_grid(self, grid):
        for row in grid.cells:
            print(' | '.join(row))
            print('-' * 10)