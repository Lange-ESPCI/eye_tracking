import cv2

name = input('Fichier vidéo à lire : ')

cap = cv2.VideoCapture(name)

i = 1
cv2.namedWindow(name, cv2.WINDOW_AUTOSIZE)

while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow(name,frame)
    i += 1
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
