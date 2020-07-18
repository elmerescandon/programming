import cv2
import numpy as np

I = cv2.imread('utec.jpg')
I_gray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(I, 100, 250)  # , apertureSize=3)
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

for i in range(len(lines)):
    for rho, theta in lines[i]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        print('hola')
        cv2.line(I, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow('1', I)
cv2.waitKey()
cv2.destroyAllWindows()
