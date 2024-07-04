import cv2
import numpy as np
video=cv2.VideoCapture(0)
kernel = np.ones((6, 6), np.uint8)
hsv_min = np.array([0, 0, 0], np.uint8)
hsv_max = np.array([0, 30, 255], np.uint8)
while True:
    ok,img=video.read()
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv_img, hsv_min, hsv_max)
    result = cv2.bitwise_and(hsv_img,  hsv_img, mask=thresh)
    img_erosion = cv2.erode(result, kernel, iterations=2)
    img_dilation = cv2.dilate(result, kernel, iterations=1)
    if not ok:
        print("удалось прочитать кадр ")
        break
    else:
        cv2.imshow('treshold', result)
        cv2.imshow('Erosion', img_erosion)
        cv2.imshow('Dilation', img_dilation)
    if cv2.waitKey(1) & 0xFF == 27:
        cv2.destroyAllWindows()
        break

