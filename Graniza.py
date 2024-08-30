import cv2

photo=cv2.imread('i.jpg.')
gray=cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
gray=cv2.GaussianBlur(gray,(3,3),0)
cv2.imwrite("i_test.jpg", gray)

edges=cv2.Canny(gray,10,200)
cv2.imwrite("edges_test.jpg", edges)

kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))
closed=cv2.morphologyEx(edges,cv2.MORPH_CLOSE, kernel)
cv2.imwrite("closed_test.jpg",closed)

COUNTS=cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)