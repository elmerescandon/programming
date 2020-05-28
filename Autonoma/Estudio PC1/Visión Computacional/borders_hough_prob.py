import numpy as np
import cv2

I = cv2.imread('utec.jpg')
gray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength, maxLineGap)
for i in range(len(lines)):
    for x1, y1, x2, y2 in lines[i]:
        cv2.line(I, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('1', I)
cv2.waitKey()
cv2.destroyAllWindows()
