import cv2

IA = cv2.imread('kafka.jpg')
I = cv2.resize(IA, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_LINEAR)
Igray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
print("\nIMPORTANTE: Para cerrar las imagenes, presionar cualquier tecla")

# Inicializar detector ORB
orb = cv2.ORB_create()

# "Keypoints" con ORB
keypts = orb.detect(I,None)
# Calcular los descriptores con ORB
keypts, descript_orb = orb.compute(I, keypts)

# Dibuja los "keypoints" (sin incluir tamaño ni orientación)
Iorb = I.copy()
cv2.drawKeypoints(I, keypts, Iorb, color=(0,255,0), flags=0)

cv2.imshow('Usando ORB', Iorb)
cv2.imwrite('images_descriptores/iorb.jpg',Iorb)
cv2.waitKey(0)
cv2.destroyAllWindows()
