import cv2
from ultralytics import YOLO

class ImageProcessor:
    def __init__(self):
        self.model = YOLO("last.pt")

    def detect_objects(self, frame):
        """
        Detects objects in the frame and returns the labels and bounding boxes.
        """
        if frame is None:
            return []
        
        results = self.model(frame)
        
        objects = []
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                label = result.names[int(box.cls)]
                confidence = box.conf[0]
                if confidence > 0.35:
                    object = (label, (x1, y1, x2, y2))
                    objects.append(object)
        
        return objects

    def filter_objects_by_name(self, name, objects):
        """
        Filters the detected objects by the given name.
        """
        return [object for object in objects if object[0] == name]
    
    def filter_objects_within_grid(self, objects, grid_area):
        """
        Returns only the objects that are within the grid area.
        """
        if not grid_area or not objects:
            return objects
        
        filtered_objects = []
        for object in objects:
            object_center = ((object[1][0] + object[1][2]) // 2, (object[1][1] + object[1][3]) // 2)
            is_within_grid = grid_area[0][0] < object_center[0] < grid_area[1][0] and grid_area[0][1] < object_center[1] < grid_area[1][1]
            if is_within_grid:
                filtered_objects.append(object)
        
        return filtered_objects

    def detect_grid_area(self, cells):
        """
        Detects the grid area from the provided cells and returns the top left and bottom right coordinates.
        """
        if not cells:
            return None, None
        
        cell_positions = []
        total_width = 0
        total_height = 0
        
        for cell in cells:
            x1, y1, x2, y2 = map(int, cell[1])
            # Add the center of the box to the list of cell positions
            center = ((x1 + x2) // 2, (y1 + y2) // 2)
            cell_positions.append(center)
            # Calculate the width and height of the cell
            total_width += (x2 - x1)
            total_height += (y2 - y1)
                
        # Calculate the average width and height of a cell
        cell_width = total_width // len(cells)
        cell_height = total_height // len(cells)
        
        # Find the top left and bottom right coordinates of the grid area
        top_left = min(cell_positions, key=lambda x: x[0] + x[1])
        bottom_right = max(cell_positions, key=lambda x: x[0] + x[1])
        
        # Offset the top left and bottom right coordinates
        top_left = (top_left[0] - cell_width * 2, top_left[1] - cell_height * 2)
        bottom_right = (bottom_right[0] + cell_width * 2, bottom_right[1] + cell_height * 2)
        
        return top_left, bottom_right
    
    def draw_bounding_box(self, frame, object):
        label, (x1, y1, x2, y2) = object
        
        colors = {
                'X': (0, 0, 255),
                'O': (0, 255, 0),
                'Cell': (255, 255, 255),
            }
        color = colors.get(label, (255, 255, 255))
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, f"{label}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        return frame

    def draw_objects(self, frame, objects):
        if not objects:
            return frame
        
        for object in objects:
            frame = self.draw_bounding_box(frame, object)
        return frame

    def draw_grid(self, frame, grid_area):
        if grid_area is None:
            return frame
        
        top_left, bottom_right = grid_area
        
        if top_left is None or bottom_right is None:
            return frame
        
        overlay = frame.copy()
        cv2.rectangle(overlay, top_left, bottom_right, (0, 255, 255), -1)
        alpha = 0.05  # Transparency factor.
        cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)
        cv2.rectangle(frame, top_left, bottom_right, (0, 255, 255), 2)
        return frame

    def draw_grid_and_objects(self, frame, grid_area, objects):
        frame_with_grid = self.draw_grid(frame, grid_area)
        frame_with_objects = self.draw_objects(frame_with_grid, objects)
        return frame_with_objects