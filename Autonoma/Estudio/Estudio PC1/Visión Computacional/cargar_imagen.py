import numpy as np
import cv2
from matplotlib import pyplot as plt

# Cargar Imagen
# Tipos de argumentos en imread
# https://docs.opencv.org/3.4/d4/da8/group__imgcodecs.html
I = cv2.imread('cat.png')
# Python trabaja con modelo de color BGR y no con RGB

print(I[:, :, 2])
# Mostrando Open CV
cv2.imshow('image', I[:, :, 2])
cv2.waitKey(0)
cv2.destroyAllWindows()


# Mostrando Matplotlib
lrgb = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)
plt.imshow(lrgb)
plt.xticks([]), plt.yticks([]), plt.show()
