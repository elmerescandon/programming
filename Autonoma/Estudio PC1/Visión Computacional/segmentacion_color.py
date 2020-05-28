import cv2
import numpy as np


I = cv2.imread("cat.png")
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)

# Se desea extraer solo el color marron en la imagen
# Límites superior e inferior para marrónn en HSV
lower_brown = np.array([15, 50, 50])
upper_brown = np.array([25, 255, 255])
# Máscara que selecciona píxeles dentro de los límites
mask = cv2.inRange(Ihsv, lower_brown, upper_brown)
# Applicación de la máscara: mantener solo lo amarillo
Ibrown = cv2.bitwise_and(I, I, mask=mask)
# Mostrar la imagen
cv2.imshow("Brown part of the image", Ibrown)
cv2.waitKey(0)
cv2.destroyAllWindows()
