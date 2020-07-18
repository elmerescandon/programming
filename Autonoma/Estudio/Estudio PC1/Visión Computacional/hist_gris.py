import numpy as np
import cv2
from matplotlib import pyplot as plt

# Cargar la imagen en modo gris
I = cv2.imread('cat.png')
# cv2.imshow("Building", I), cv2.waitKey(0)


# Calcular el histograma en escala de grises  ===============================
# (I, canal 0, mask=None, tamaño, rango)
# hist = cv2.calcHist([I], [0], None, [256], [0, 256])


# Mostrar el histograma usando matplotlib
# plt.plot(hist)
# plt.show()

# Histograma a color =======================================================
# Histograma de cada canal RGB (solo se muestra R)
rhist = np.histogram(I[:, :, 0], bins=32, range=(0, 256))
ghist = np.histogram(I[:, :, 1], bins=32, range=(0, 256))
bhist = np.histogram(I[:, :, 2], bins=32, range=(0, 256))

# Retor

# Centros
bin_edges = rhist[1]

bin_centers = (bin_edges[1:] + bin_edges[0:len(bin_edges)-1])/2

# Vector de características ("features")
hist_features = np.concatenate((rhist[0], ghist[0], bhist[0]))


# Gráfico (subplot para cada canal …)
fig = plt.figure(figsize=(12, 3))
lin = np.linspace(0, 95, num=96)

plt.subplot(221)
plt.bar(bin_centers, rhist[0])
plt.xlim(0, 256)
plt.title('R Hist')

plt.subplot(222)
plt.bar(bin_centers, ghist[0])
plt.xlim(0, 256)
plt.title('G Hist')

plt.subplot(223)
plt.bar(bin_centers, bhist[0])
plt.xlim(0, 256)
plt.title('B Hist')

plt.subplot(224)
plt.bar(lin, hist_features)
plt.title('B Hist')
plt.show()
