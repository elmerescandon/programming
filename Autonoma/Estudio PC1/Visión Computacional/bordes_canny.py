import cv2
import numpy as np


I = cv2.imread('utec.jpg', 0)


# Los parámetros derecha definen la histéresis para escoger las líneas que se acpetan

I_canny = cv2.Canny(I, 100, 250)

cv2.imshow('1', I)
cv2.imshow('2', I_canny)
cv2.waitKey()
print(I_canny)
cv2.destroyAllWindows()
