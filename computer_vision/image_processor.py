import cv2
from ultralytics import YOLO

class ImageProcessor:
    def __init__(self):
        self.model = YOLO("last.pt")

    def process_frame(self, frame):
        results = self.model(frame)
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                label = result.names[int(box.cls)]
                confidence = box.conf[0]

                colors = {
                    0: (255, 0, 0),
                    1: (0, 255, 0),
                    2: (0, 0, 255),
                }

                color = colors.get(int(box.cls), (255, 255, 255))
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, f"{label} ({confidence * 100:.1f}%)", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, color, 1)
        return frame
