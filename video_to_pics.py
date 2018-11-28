import cv2
import numpy as np 
import random
video = "/home/abhiyaan/course.webm"

cap = cv2.VideoCapture(video)
i = 0
while(True):
    ret, frame = cap.read()
    if i%30==0:
       cv2.imwrite("data/" + str(i)+ str(random.randint(i,100000000))+ "blah" + "a.png", frame)