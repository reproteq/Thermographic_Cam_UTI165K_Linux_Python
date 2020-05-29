
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

W = '\033[0m'
R = '\033[31m'
G = '\033[32m'
O = '\033[33m'
B = '\033[34m'
P = '\033[35m'
C = '\033[36m'
GR = '\033[37m'

camera_num = 0

global alto
global ancho

alto = 321
ancho = 240
cam = cv2.VideoCapture(camera_num , cv2.CAP_V4L )

cam.set(3,ancho)
cam.set(4,alto)

print  W + " |"+R +" T"+ R + "T"+ G +" v1.0 2020-05-29 "+ W + " |"
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
    print("TTCODE Frame OK! for temp calculation")
    #print(struct.unpack("h", frame[320][0])[0]/10)
    tempraw = (struct.unpack("h", frame[320][0])[0])
    tempdec = tempraw[:-2]
    print R,tempdec ,W
    
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
