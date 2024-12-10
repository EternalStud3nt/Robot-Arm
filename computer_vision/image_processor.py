import cv2
from ultralytics import YOLO

class ImageProcessor:
    def __init__(self):
        self.model = YOLO("last.pt")

    def detect_objects(self, frame, name=None):
        """
        Detects objects in the frame and returns the labels and bounding boxes. 
        If a name is provided, only objects with that name are returned.
        """
        
        results = self.model(frame)
        detections = []
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                label = result.names[int(box.cls)]
                confidence = box.conf[0]
                if confidence > 0.3:
                    detections.append((label, (x1, y1, x2, y2)))
        
        if name:
            detections = [box for box in detections if box[0] == name]
        
        return detections

    def detect_grid_area(self, frame):
        """
        Detects the grid area in the frame and return the top left and bottom right coordinates
        """
        
        detected_cells = self.detect_objects(frame, "Cell")
        
        # Detect the top left and bottom right cell
        top_left_cell = None
        bottom_right_cell = None
        
        for cell in detected_cells:
            x1, y1, x2, y2 = cell[1]
            if top_left_cell is None:
                top_left_cell = (x1, y1)
            else:
                top_left_cell = (min(top_left_cell[0], x1), min(top_left_cell[1], y1))
                
            if bottom_right_cell is None:
                bottom_right_cell = (x2, y2)
            else:
                bottom_right_cell = (max(bottom_right_cell[0], x2), max(bottom_right_cell[1], y2))
                
        # return the top left and bottom right cell coordinates
        return top_left_cell, bottom_right_cell

    def draw_objects(self, frame):
        detections = self.detect_objects(frame)
        for label, (x1, y1, x2, y2) in detections:
            colors = {
                'X': (0, 0, 255),
                'O': (0, 255, 0),
                'Cell': (255, 255, 255),
            }
            color = colors.get(label, (255, 255, 255))
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"{label}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        return frame

    def draw_grid(self, frame):
        top_left, bottom_right = self.detect_grid_area(frame)
        cv2.rectangle(frame, top_left, bottom_right, (0, 255, 255), 2)
        return frame