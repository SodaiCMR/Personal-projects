import cv2 as cv
from img_to_ascii import *
from PIL import Image
import os

cap = cv.VideoCapture('vegeta_ssj.mp4')
# cap = cv.VideoCapture('black_hole.mp4')

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_as_img = Image.fromarray(gray_frame)
    os.system('cls' if os.name == 'nt' else 'clear')
    image_to_ascii(frame_as_img)
    delay = int(1000 / 60)
    if cv.waitKey(delay) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
