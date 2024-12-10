import cv2
import os
import time

class Camera:
    def __init__(self, camera_index=0):
        self.camera = cv2.VideoCapture(camera_index)
        if not self.camera.isOpened():
            raise Exception("Error: Could not open webcam.")
    
    def capture_photo(self, filename="webcam_photo.jpg", save_location="./photos", show_preview=False):
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
            
            if show_preview:
                # Display the captured photo
                cv2.imshow("Captured Photo", frame)
                cv2.waitKey(1)  # Display the image for 1 millisecond to ensure it shows up
                time.sleep(1)  # Wait for 1 second
                cv2.destroyAllWindows()
            return frame
        else:
            print("Error: Could not capture photo.")
            return None
            
    def release(self):
        self.camera.release()
        cv2.destroyAllWindows()

    def get_feed_photo(self):
        ret, frame = self.camera.read()
        if not ret:
            print("Error: Could not read frame.")
            return None
        return frame

    def get_feed_video(self):
        while True:
            frame = self.get_feed_photo()
            if frame is None:
                break
            yield frame
        self.release()

    def capture_train_photos(self):
        base_folder = "data/ml_photos"
        subfolder_index = 1
        while os.path.exists(os.path.join(base_folder, f"session_{subfolder_index}")):
            subfolder_index += 1
        session_folder = os.path.join(base_folder, f"session_{subfolder_index}")
        os.makedirs(session_folder)

        photo_index = 0
        while True:
            if input("Press 'q' to quit, any other key to capture photo: ") == 'q':
                break
            else:
                photo_index += 1
                self.capture_photo(f"ml_photo_{photo_index}", session_folder, True)
        self.release()
