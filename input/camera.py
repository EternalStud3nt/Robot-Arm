import cv2

class Camera:
    def __init__(self, camera_index=0):
        self.camera = cv2.VideoCapture(camera_index)
        if not self.camera.isOpened():
            raise Exception("Error: Could not open webcam.")
    
    def capture_photo(self, filename="webcam_photo.jpg"):
        ret, frame = self.camera.read()
        if ret:
            cv2.imwrite(filename, frame)
            print(f"Photo saved as {filename}")
        else:
            print("Error: Could not capture photo.")
    
    def release(self):
        self.camera.release()
        cv2.destroyAllWindows()
