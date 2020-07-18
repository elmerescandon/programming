import cv2
import numpy as np

I = cv2.imread('cat.png', 0)
# Creación del filtro de media ==============
filter = np.ones((5, 5), np.float32)/25
# Aplicación del filtro (-1: mantener nro de canales)
Ifilt = cv2.filter2D(I, -1, filter)

# Filtro Gaussiano
Iblurg = cv2.GaussianBlur(I, (5, 5), 0)


# Demostración de derivada
# Gradiente
Isobelx = cv2.Sobel(I, cv2.CV_64F, 1, 0, ksize=5)
Isobely = cv2.Sobel(I, cv2.CV_64F, 0, 1, ksize=5)
# Laplaciano
I_laplace = cv2.Laplacian(I, cv2.CV_64F)


# Demostración de la imagen suaviaada
cv2.imshow('image1', I)
cv2.imshow('image2', Isobelx)
cv2.imshow('1', I_laplace)
cv2.waitKey(0)
cv2.destroyAllWindows()
