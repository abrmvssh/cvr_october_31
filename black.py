import cv2
from pprint import pprint
import sys
import numpy
sqrlen = 100
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    print(frame.shape)
    height, wighth, _ = frame.shape
    frame[:sqrlen,:sqrlen] = [0,0,0]
    frame[:sqrlen,wighth - sqrlen :] = [0, 0, 0]
    frame[height - sqrlen:, :sqrlen] = [0, 0, 0]
    frame[height - sqrlen:, wighth - sqrlen:] = [0, 0, 0]
    frame[height // 2 - sqrlen // 2 :height // 2 + sqrlen // 2,wighth // 2 - sqrlen // 2 : wighth // 2 + sqrlen] = [100, 100, 253]
    cv2.imshow('camera', frame)
    key = cv2.waitKey(1000)
    print(key)




