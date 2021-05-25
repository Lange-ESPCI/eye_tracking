from imutils.video import VideoStream
import time
import cv2

vs = VideoStream(src="nvarguscamerasrc ! video/x-raw(memory:NVMM), " \
        "width=(int)1280, height=(int)720, format=(string)NV12, " \
        "framerate=(fraction)120/1 ! nvvidconv ! video/x-raw, " \
        "format=(string)BGRx ! videoconvert ! video/x-raw, " \
        "format=(string)BGR ! appsink").start()

fourcc = cv2.VideoWriter_fourcc('X', '2', '6', '4')
cw = cv2.VideoWriter('test.mp4', fourcc, 120.000005, (1280, 720))

start_time = time.time()

while time.time() < start_time + 4.0:
    frame = vs.read()

    cw.write(frame)

cw.release()
vs.stop()
