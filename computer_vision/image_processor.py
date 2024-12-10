import cv2
from ultralytics import YOLO

class ImageProcessor:
    def __init__(self):
        self.model = YOLO("last.pt")

    def detect_objects(self, frame):
        """
        Detects objects in the frame and returns the labels and bounding boxes.
        """
        
        results = self.model(frame)
        
        objects = []
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                label = result.names[int(box.cls)]
                confidence = box.conf[0]
                if confidence > 0.3:
                    object = (label, (x1, y1, x2, y2))
                    objects.append(object)
        
        return objects

    def filter_objects(self, name, objects):
        """
        Filters the detected objects by the given name.
        """
        return [object for object in objects if object[0] == name]

    def detect_grid_area(self, cells):
        """
        Detects the grid area from the provided cells and returns the top left and bottom right coordinates.
        """
        
        if not cells:
            return None, None
        
        cell_positions = []
        # print number of cells and positions
        #print("Number of cells: ", len(cells))
        
        for cell in cells:
            x1, y1, x2, y2 = map(int, cell[1])
            # Add the center of the box to the list of cell positions
            center = ((x1 + x2) // 2, (y1 + y2) // 2)
            cell_positions.append(center)
                
        # Find the top left and bottom right coordinates of the grid area
        top_left = min(cell_positions, key=lambda x: x[0] + x[1])
        bottom_right = max(cell_positions, key=lambda x: x[0] + x[1])
        
        return top_left, bottom_right

    def draw_objects(self, frame, objects):
        for label, (x1, y1, x2, y2) in objects:
            colors = {
                'X': (0, 0, 255),
                'O': (0, 255, 0),
                'Cell': (255, 255, 255),
            }
            color = colors.get(label, (255, 255, 255))
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"{label}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        return frame

    def draw_grid(self, frame, cells):
        top_left, bottom_right = self.detect_grid_area(cells)
        
        if top_left is None or bottom_right is None:
            return frame
        
        overlay = frame.copy()
        cv2.rectangle(overlay, top_left, bottom_right, (0, 255, 255), -1)
        alpha = 0.5  # Transparency factor.
        cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)
        cv2.rectangle(frame, top_left, bottom_right, (0, 255, 255), 2)
        return frame