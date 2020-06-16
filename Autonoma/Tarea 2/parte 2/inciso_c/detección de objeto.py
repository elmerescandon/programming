import numpy as np
import cv2
from matplotlib import pyplot as plt

# Cargar Imagen ------------------------------------------------------
Im = cv2.imread('kafka.jpg')
I1 = cv2.resize(Im, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_LINEAR)
print(I1.shape)
I1gray = cv2.cvtColor(I1, cv2.COLOR_BGR2GRAY)

# FANN para la imagen ------------------------------------------------
orb = cv2.ORB_create() # Inicializar el descriptor ORB
# 'Keypoints' y descriptores para cada imagen (usando ORB)
keypts1, descript1 = orb.detectAndCompute(I1gray, None)
# Matching usando FLANN
FLANN_INDEX_LSH = 6
# Número mínimo de puntos para "match"
MIN_MATCH_COUNT = 10
# Parámetros sugeridos para FLANN con ORB
index_params= dict(algorithm = FLANN_INDEX_LSH, table_number = 6,
                   key_size = 12, multi_probe_level = 1)
# Número de veces que el índice se debe buscar en el árbol
search_params = dict(checks = 50)
# Instancia de FLANN
flann = cv2.FlannBasedMatcher(index_params, search_params)

# Iorb = I1.copy()
# cv2.drawKeypoints(I1, keypts1, Iorb, color=(0,255,0), flags=0)
# plt.figure(figsize=(12,12))
# Lectura de Cámara --------------------------------------------------
# Activar imagen
cam = cv2.VideoCapture(0)
# Variable para almacenar el tamaño de la imagen
Isize = None
print("\nIMPORTANTE: Para detener la cámara presionar \"q\"")
# Iorb = cv2.cvtColor(Iorb,cv2.COLOR_BGR2RGB)
while(cam.isOpened()):
    retval, frame = cam.read()
    # Solo si se tiene una imagen válida
    if retval==True:
        if (Isize==None):   # Mostrar el tamaño de la imagen solo 1 vez
            Isize = frame.shape
            print("Tamaño de la imagen: ", Isize)
        #frame = cv2.flip(frame,1)  # Voltear horizontalmente (opcional)
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        keypts2, descript2 = orb.detectAndCompute(frame_gray, None)

        # Usando K-NN para match
        matches = flann.knnMatch(descript1, descript2, k=2)
        # Almacenamiento de los buenos "matches"
        good_matches = []
        for match in matches:
            if (len(match)<2): continue # Descartar "matches" que tienen menos de 2 componentes
            m,n = match
            if m.distance < (0.7*n.distance):
                good_matches.append(m)

        print(len(good_matches))
        if (len(good_matches) > MIN_MATCH_COUNT): # Homografía entre los mejores "matches"
            print("SI ES BUENO LO QUE MIDO ")
            src_pts = np.float32([ keypts1[m.queryIdx].pt for m in good_matches ]).reshape(-1,1,2)
            dst_pts = np.float32([ keypts2[m.trainIdx].pt for m in good_matches ]).reshape(-1,1,2)
            # Homografía entre pares de puntos
            M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
            matchesMask = mask.ravel().tolist()
            # Borde del elemento detectado
            h,w = I1gray.shape
            pts = np.float32([[0,0], [0,h-1], [w-1,h-1], [w-1,0] ]).reshape(-1,1,2)
            dst = cv2.perspectiveTransform(pts, M)
            cv2.drawKeypoints(frame, keypts2, frame, color=(0,255,0), flags=0)
            # Gráfico sobre la imagen
            frame = cv2.polylines(frame, [np.int32(dst)], True, (255,0,0), 3, cv2.LINE_AA)
        else:
            print("No hay suficientes correspondencias - {}/{}".format(len(good_matches),MIN_MATCH_COUNT))
            matchesMask = None
        # if (generar_video): # Si se desea grabar el video, se almacena en "out"
        #     out.write(frame)
        # Imagen originalqq
        # frame =  cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        # plt.subplot(1,2,1); plt.imshow(frame)
        # plt.title('Cámara'); plt.axis('off')
        # plt.subplot(1,2,2); plt.imshow(Iorb)
        # plt.title('Descriptores de la imagen '); plt.axis('off')
        # Imagen HoG
        # plt.pause(0.0005)

        cv2.imshow('My camera', frame) # Mostrar la imagen de la cámara
        # Esperar 30ms entre imágenes
        # Si se presiona 'q' se termina el bucle
        if (cv2.waitKey(30) & 0xFF) == ord('q'):
            break
    else:
        break

plt.imshow()
# Cuando termine de usarse la cámara, eliminar los recursos
cam.release()
cv2.destroyAllWindows()

# Detección de características mediante FANN
