import cv2

capture = cv2.VideoCapture(0) #cap abbreviated

while True:
    _, img = capture.read()
    cv2.imshow("From camera", img)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

capture.release()
cv2.destroyAllWindows()
