import numpy as np
import cv2

# Read the image and resize it
img = cv2.imread("computer vision/samples/edge detection/chessboard.png")
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply the Shi-Tomasi corner detection algorithm
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int32(corners)

# Draw the corners on the image
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)
    
for i in range(len(corners)):
    for j in range(i +1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        randColor = map(int, np.random.randint(0, 255, size=3))
        color = tuple(randColor)
        cv2.line(img, corner1, corner2, color, 1)
        


cv2.imshow("Frame", img)
cv2.waitKey(0)
cv2.destroyAllWindows()