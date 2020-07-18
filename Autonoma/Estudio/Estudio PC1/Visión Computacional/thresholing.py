import cv2

I = cv2.imread('cat.png', 0)

# T - 150, valor de blanco que se usará 255
retval = lbw = cv2.threshold(I, 150, 255, cv2.THRESH_BINARY)
print(retval)

cv2.imshow('1', retval[1])
cv2.imwrite('gato_negro.png', retval[1])
cv2.waitKey(0)
cv2.destroyAllWindows()
