import numpy as np
import cv2
import os


cap = cv2.VideoCapture('./cat_video.mov')
path = 'cat'
os.mkdir(path)

name_id = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if frame is None:
        print("You've reached the end of the video. Thanks for using it. All images are in the 'cat' folder.")
        break
    if (frame.any()):
        im_path = os.path.join(path, 'cat_{0:06d}.jpg'.format(name_id))
        cv2.imwrite(im_path, frame)
        name_id += 1
