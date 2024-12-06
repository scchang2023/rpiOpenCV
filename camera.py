import cv2
cv2.namedWindow("camera")
cap = cv2.VideoCapture(0)
cap.set(3, 360)
cap.set(4, 240)
while True:
    _, frame = cap.read()
    cv2.imshow('original', frame)
    k = cv2.waitKey(5) & 0xFF
    if k==27:
        break

cv2.destroyAllWindows()        