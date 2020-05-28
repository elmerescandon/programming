import cv2
import numpy as np

I = cv2.imread('coin.jpg')
Igray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
Igray = cv2.medianBlur(Igray, 5)
minDist = 30  # Distancia mínima entre centros de los círculos
THCanny = 150  # Umbral alto para el detector de Canny
minVotes = 100
circles = cv2.HoughCircles(Igray, cv2.HOUGH_GRADIENT, 1, minDist,
                           param1=THCanny, param2=minVotes, minRadius=10, maxRadius=200)
print(circles)
circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    # Dibuja el círculo exterior
    cv2.circle(I, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # Dibuja el centro del círculo
    cv2.circle(I, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow('detected circles', I)
cv2.waitKey(0)
cv2.destroyAllWindows()
