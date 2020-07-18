import cv2
import numpy as np

# Lectura de la imagen RGB
I = cv2.imread("cat.png")
cv2.imshow("Original image", I)
cv2.waitKey(0)
# Conversión a escala de grises
Igray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image", Igray)
cv2.waitKey(0)
# Conversión a HSV
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
# Extracción del componente Hue
Ihue = Ihsv[:, :, 0]
cv2.imshow("Hue", Ihue)
cv2.waitKey(0)
