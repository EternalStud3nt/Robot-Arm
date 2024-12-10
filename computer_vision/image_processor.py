import cv2
from ultralytics import YOLO

class ImageProcessor:
    def __init__(self):
        self.model = YOLO("last.pt")

    def detect_objects(self, frame):
        results = self.model(frame)
        detections = []
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                label = result.names[int(box.cls)]
                confidence = box.conf[0]
                if confidence > 0.3:
                    detections.append((label, (x1, y1, x2, y2)))
        return detections

    def detect_object(self, frame, name):
        detections = self.detect_objects(frame)
        
        target_objects = []
        for box in detections:
            if box[0] == name:
                target_objects.append(box)
        return target_objects

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


