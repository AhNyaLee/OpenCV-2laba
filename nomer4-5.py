import cv2
import numpy as np

my_photo = cv2.imread('i.jpg')
filterd_image  = cv2.medianBlur(my_photo,7)
img_grey = cv2.cvtColor(filterd_image,cv2.COLOR_BGR2GRAY)
ret,thresh_img = cv2.threshold(img_grey, 100, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#create an empty image for contours
img_contours = np.uint8(np.zeros((my_photo.shape[0],my_photo.shape[1])))

cv2.drawContours(img_contours, contours, -1, (255,255,255), 1)
for contour in contours:
    M = cv2.moments(contour)

    # Проверка, что момент не нулевой (т.е., контур достаточно большой)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        print(f"Центр масс для контура: ({cX}, {cY})")

cv2.imshow('res', img_contours) # выводим итоговое изображение в окно

cv2.waitKey()
cv2.destroyAllWindows()
total_area = 0
for contour in contours:
    area = cv2.contourArea(contour)
    total_area += area

print(f"Общая площадь всех объектов: {total_area}")
