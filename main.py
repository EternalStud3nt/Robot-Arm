#from computer_vision.camera import Camera

# camera = Camera()
# photo_index = 0
# 
# while True:
#     if(input("Press 'q' to quit, any other key to capture photo: ") == 'q'):
#         break
#     else:
#         photo_index += 1
#         camera.capture_photo("train_" + str(photo_index), "data/train")
#

if __name__ == "__main__":
    from robot_arm.controller import Controller
    controller = Controller()