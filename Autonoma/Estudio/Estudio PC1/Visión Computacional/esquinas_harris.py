from __future__ import print_function
import cv2
import argparse
import cv2 as cv
import numpy as np

I = cv2.imread('box.jpg')
I = cv2.resize(I, (800, 600))
Igray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)


# Harris corners
neighborhood = 2  # Tamano de vecindad
apperture = 3  # Tamano de apertura (ventana)
alpha = 0.04  # Parametro alpha (o k)
score = cv2.cornerHarris(Igray, neighborhood, apperture, alpha)


# Normalizing
dst_norm = np.empty(score.shape, dtype=np.float32)
cv.normalize(score, dst_norm, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
dst_norm_scaled = cv.convertScaleAbs(dst_norm)
print(dst_norm)


# Drawing a circle around corners
for i in range(dst_norm.shape[0]):
    for j in range(dst_norm.shape[1]):
        if int(dst_norm[i, j]) > 145:
            cv.circle(I, (j, i), 3, (100, 30, 45), 2)
# Showing the result
cv.imshow('hola', I)
cv2.waitKey()
cv2.destroyAllWindows()
