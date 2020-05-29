#!/usr/bin/python
### requerimets  pip opencv4.30 numpy
### Thermographic Cam Linux Python for Raspberry Pi
### TTCODE 2020

import numpy as np
import time
import cv2
import struct

global W
global R
global G
global O
global B
global P
global C
global GR

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
YL = '\033[93m'  # cyan
GR = '\033[37m'  # gray
LR = '\033[91m'  # LightRed     
LG = '\033[92m'  # LightGreen   
LY = '\033[93m'  # LightYellow  
LB = '\033[94m'  # LightBlue    
LM = '\033[95m'  # LightMagenta 
LC = '\033[96m'  # LightCyan   
Bli  = '\033[5m' # Blink   
camera_num = 0

global alto
global ancho

alto = 321
ancho = 240
cam = cv2.VideoCapture(camera_num , cv2.CAP_V4L )

cam.set(3,ancho)
cam.set(4,alto)

print  W + "### "+LB +" Thermographic Cam Linux "+ LR + "Powered by TTCODE "+ G +" v1.0 2020-05-29 "+ W + "|"
if not cam.isOpened():
    print("Was not able to open camera", camera_num)
    cam.release()

print("Camera %d open at size: (%d x %d) %d FPS" % (camera_num, cam.get(3), cam.get(4), cam.get(5)))

cv2.namedWindow('Thermal Camera - Press Q to quit', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Thermal Camera - Press Q to quit', 480, 642)

while(True):
    # Capture frame-by-frame
    ret, frame = cam.read()

    if not ret:
        print("Failed to fetch frame")
        time.sleep(0.1)
        continue
    #print("Frame OK!")
    colorframe = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    # Display the resulting frame
    cv2.imshow('Thermal Camera - Press Q to quit', colorframe)
    
    cam.set(cv2.CAP_PROP_CONVERT_RGB, 0)
    ret, frame = cam.read()
    if not ret:
        print("Failed to fetch frame")
        time.sleep(0.1)
        continue
    print("Watting scanning temp")
    #print(struct.unpack("h", frame[320][0])[0]/10)
    tempdump = (struct.unpack("h", frame[320][0])[0])

    tempraw = str(tempdump)
    temprawa = tempraw[:-1]
    temprawb = tempraw[-1:]
    temp = temprawa+'.'+temprawb
    tempint = int(temprawa)
    tempfloat = float(tempdump)
    temp0 =35
    temp1 = 36
    temp2 = 37
    temp3 = 38
    
    #print (R+temprawa+'.'+temprawb+W)
    #print (tempint)
    if (tempint <= temp0):
        print (LB+temp+W)
            
    if (tempint == temp1):
        print (LG+temp+W)
        print (G + "OK Good Temp for Human"+W)
 
    if (tempint == temp2):  
        print (O+temp+W)
        print (Bli + LR+"Alert!! Posible Positive COVID19"+W)
        
    if (tempint >= temp3):
        print (LR+temp+W)
        print (Bli + LR+"Alert!! Positive COVID19 Detected"+W)
 
    #print (P+tem+W)  
    #print (frame)
    #salida = frame.tostring()
    #salida = frame.tobytes()
    #print salida
    #print (struct.unpack('h',frame[0][0]))
    cam.set(cv2.CAP_PROP_CONVERT_RGB, 1)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    #yuvframe = cv2.cvtColor(frame, cv2.COLOR_RGB2YUV)
    #print(yuvframe[-1][0:3])
cam.release()
cv2.destroyAllWindows()
