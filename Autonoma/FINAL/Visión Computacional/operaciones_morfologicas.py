import cv2

I = cv2.imread('gato_negro.png', 0)
# Elemento estructural (kernel)
k = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
# Operaciones morfológicas
Ierosion = cv2.erode(I, k, iterations=1)
Idilation = cv2.dilate(I, k, iterations=1)
Iopening = cv2.morphologyEx(I, cv2.MORPH_OPEN, k)
Iclosing = cv2.morphologyEx(I, cv2.MORPH_CLOSE, k)
cv2.imshow('original', I)
cv2.imshow('eroded', Ierosion)
cv2.imshow('dilated', Idilation)
cv2.imshow('opened', Iopening)
cv2.imshow('closed', Iclosing)
cv2.waitKey(0)
