import cv2
from ultralytics import YOLO
import numpy as np
from camera import Camera

class ImageProcessor:
    def __init__(self):
        self.camera = Camera()

    def draw_objects(self, img):
        # Load the YOLO model
        model = YOLO("../ML Data/best.pt")

        # Define colors for each class
        class_colors = {
            0: (255, 0, 0),  # Red
            1: (0, 255, 0),  # Green
            2: (0, 0, 255),  # Blue
            # Add more colors as needed
        }

        # Detect objects in the image
        results = model.predict(source=img, conf=0.25, save=False)

        # Iterate through detected objects
        for result in results[0].boxes:
            # Get bounding box coordinates
            x1, y1, x2, y2 = map(int, result.xyxy[0])
            confidence = result.conf[0]
            
            # Get the class id
            class_id = int(result.cls[0])
            # Get the color for the class
            color = class_colors.get(class_id, (255, 255, 255))  # Default to white if class_id not found

            # Draw the bounding box with the class-specific color
            cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
            # Put the label above the bounding box with the class-specific color
            label = f"{class_id} {confidence:.2f}"
            cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
            
        # Show the image
        cv2.imshow("Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
                        
            

if __name__ == "__main__":
    #camera = Camera()
    #img = camera.capture_photo()
    #get the image from the same of the script named test.jpg
    img = cv2.imread("test.jpg")
    processor = ImageProcessor()
    processor.draw_objects(img)