import cv2

cam = cv2.VideoCapture(0)
while True:
    variable1, frame = cam.read()
    cv2.imshow('Webcam Feed', frame)
    cv2.waitKey(1)