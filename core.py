
import numpy as np
import time
import cv2
import struct

camera_num = 0
global alto
global ancho

alto = 321
ancho = 240
cam = cv2.VideoCapture(camera_num , cv2.CAP_V4L )


cam.set(3,ancho)
cam.set(4,alto)
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
    print(struct.unpack("h", frame[320][0])[0]/10)
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
