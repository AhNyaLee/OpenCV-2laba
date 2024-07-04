import cv2
import numpy as np
video=cv2.VideoCapture(0)

hsv_min = np.array([160, 70, 80], np.uint8)  # Нижняя граница для второго диапазона красного
hsv_max = np.array([180, 130, 160], np.uint8)
while True:
    ok,img=video.read()
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv_img, hsv_min, hsv_max)
    result = cv2.bitwise_and(hsv_img,  hsv_img, mask=thresh)
    if not ok:
        print("удалось прочитать кадр ")
        break
    else:
        cv2.imshow('treshold', result)
    if cv2.waitKey(1) & 0xFF == 27:
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        break

