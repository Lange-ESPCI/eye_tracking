from imutils.video import VideoStream
import imutils
import time
import cv2

print("Début de l'acquisition vidéo...")

vs = VideoStream(src="nvarguscamerasrc ! video/x-raw(memory:NVMM), " \
        "width=(int)1280, height=(int)720, format=(string)NV12, " \
        "framerate=(fraction)60/1 ! nvvidconv ! video/x-raw, " \
        "format=(string)BGRx ! videoconvert ! video/x-raw, " \
        "format=(string)BGR ! appsink").start()

start_time = time.time()

while True:
    frame = vs.read()

#    frame = imutils.resize(frame, width=500)
#    cv2.imshow("Frame", frame)

#    key = cv2.waitKey(30) & 0xFF
#   if key == 27:
#      break

    current_time = time.time()
    print("FPS : {}".format(1/(current_time - start_time)))
    start_time = current_time

vs.stop()
cv2.destroyAllWindows()
