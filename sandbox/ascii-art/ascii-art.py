import cv2 as cv
import numpy as np
import os

video_size = (352, 240)
reversed_video_size = (240, 352)

outpath = os.path.join("ascii-art", "asciied_video.mp4v")
cap = cv.VideoCapture('vegeta_ssj.mp4')
ascii_map = ["@", "S", "%", "?", "*", "+", ";", ":", ",", ".", "-", "&", "é", "_", "#"]
asciied_frame = np.zeros(reversed_video_size, dtype=np.uint8)
fourcc = cv.VideoWriter.fourcc(*'XVID')
out = cv.VideoWriter(outpath, fourcc, 20, video_size)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    resized_frame = cv.resize(gray_frame, video_size, interpolation=cv.INTER_AREA)
    for row in range(resized_frame.shape[0]):
        for col in range(resized_frame.shape[1]):
            min_value = int(resized_frame[row, col] // 17) - 1
            mapped_index = max(0, min_value)
            text = ascii_map[mapped_index]
            cv.putText(asciied_frame, text, (row,col), cv.FONT_HERSHEY_PLAIN, 0.4, (255, 255, 255) ,1)
            # out.write(asciied_frame)
            # print(ascii_map[mapped_index])
            # asciied_frame[row, col] = ascii_map[mapped_index]

    # out.write(asciied_frame)
    # cv.imshow('video', resized_frame)
    cv.imshow("img", asciied_frame)
    delay = int(1000 / 60)
    if cv.waitKey(delay) == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()
