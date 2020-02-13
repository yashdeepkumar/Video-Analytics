
# Program To Read video 
# and Extract Frames 
import cv2 
vidObj = cv2.VideoCapture(1)
count = 1704
success = 1
while success: 
    success, image = vidObj.read() 
    cv2.imwrite("image/frame%d.jpg" % count, image) 
    count += 1
