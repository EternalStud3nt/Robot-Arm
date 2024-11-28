import cv2
import os

class Camera:
    def __init__(self, camera_index=0):
        self.camera = cv2.VideoCapture(camera_index)
        if not self.camera.isOpened():
            raise Exception("Error: Could not open webcam.")
    
    
    def capture_photo(self, filename="webcam_photo.jpg", save_location="."):
        ret, frame = self.camera.read()
        
        # Ensure the filename has a valid image extension
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            filename += ".jpg"
        
        # Create save location if it doesn't exist
        if not os.path.exists(save_location):
            os.makedirs(save_location)
            
        # if the frame was captured successfully, save it
        if ret:
            full_path = os.path.join(save_location, filename)
            cv2.imwrite(full_path, frame)
            print(f"Photo saved as {full_path}")
        else:
            print("Error: Could not capture photo.")
            
        cv2.imshow("Captured Photo", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return frame
        
    
    def release(self):
        self.camera.release()
        cv2.destroyAllWindows()
