
# -*- coding: utf-8 -*-
import cv2
import numpy as np

# Eliminar la parte negra del panorama
def trim(frame):
    # Cortar la imagen
    if not np.sum(frame[0]): return trim(frame[1:])
    if not np.sum(frame[-1]): return trim(frame[:-2])
    if not np.sum(frame[:,0]): return trim(frame[:,1:])
    if not np.sum(frame[:,-1]): return trim(frame[:,:-2])
    return frame

# I1 = cv2.imread('tumi_der.JPG')
# I2 = cv2.imread('tumi_med.JPG')
#
# I1 = cv2.imread('tumi_med.JPG')
# I2 = cv2.imread('tumi_izq2.JPG')


I_der = cv2.imread('tumi_der_mod.JPG')
I_mid = cv2.imread('tumi_med_mod.JPG')
I_izq = cv2.imread('tumi_izq2_mod.JPG')

I_der_gr = cv2.cvtColor(I_der, cv2.COLOR_BGR2GRAY)
I_mid_gr = cv2.cvtColor(I_mid, cv2.COLOR_BGR2GRAY)
I_izq_gr = cv2.cvtColor(I_izq, cv2.COLOR_BGR2GRAY)

# Inicializar el descriptor ORB
orb = cv2.ORB_create()
# 'Keypoints' y descriptores para cada imagen (usando ORB)
keypts_der, descript_der = orb.detectAndCompute(I_der_gr, None)
keypts_mid, descript_mid = orb.detectAndCompute(I_mid_gr, None)
keypts_izq, descript_izq = orb.detectAndCompute(I_izq_gr, None)

# Matcher entre las imágenes
match = cv2.BFMatcher()
matches_der_mid = match.knnMatch(descript_der, descript_mid, k=2)
good_matches_mid_der = []

# IMAGEN MEDIA Y DERECHA ==================================================

# Escoger los mejores puntos obtenidos por ORB entre Imagen derecha y media
for m,n in matches_der_mid:
    if m.distance < 0.7*n.distance:
        good_matches_mid_der.append(m)
print(len(good_matches_mid_der))



# Dibujar los "matches" (las correspondencias)
draw_params = dict(matchColor=(0,255,0), singlePointColor = None, flags = 2)
Imatch = cv2.drawMatches(I_mid, keypts_mid, I_der, keypts_der, good_matches_mid_der, None, **draw_params)
Imatch_2 = cv2.resize(Imatch, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_LINEAR)
cv2.imshow("Correspondencias originales", Imatch_2)

# Encontrar la homografía dados los puntos correspondientes
MIN_MATCH_COUNT = 10
print(len(good_matches_mid_der))
# Good hasta acá
if len(good_matches_mid_der) > MIN_MATCH_COUNT:
    src_pts_dermid = np.float32([ keypts_der[m.queryIdx].pt for m in good_matches_mid_der ]).reshape(-1,1,2)
    dst_pts_dermid = np.float32([ keypts_mid[m.trainIdx].pt for m in good_matches_mid_der ]).reshape(-1,1,2)
    M, mask = cv2.findHomography(src_pts_dermid, dst_pts_dermid, cv2.RANSAC,5.0)
    h,w = I_der_gr.shape
    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
    dst_der_mid = cv2.perspectiveTransform(pts, M)
    img2 = cv2.polylines(I_mid_gr, [np.int32(dst_der_mid)], True, 255, 3, cv2.LINE_AA)
    # img2 = cv2.resize(img2, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_LINEAR)
    # cv2.imshow("Area de superposicion", img2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    print("Estamos bien")
else:
    print ("No se encuentran suficientes correspondencias - {}/{}".
           format(len(good_matches),MIN_MATCH_COUNT))



# Panorama usando la homografía
I_mid_der = cv2.warpPerspective(I_der, M, (I_mid.shape[1] + I_der.shape[1], I_mid.shape[0]))
I_mid_der[0:I_mid.shape[0],0:I_mid.shape[1]] = I_mid
I_mid_der = trim(I_mid_der)
I_mid_der_s = cv2.resize(I_mid_der, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_LINEAR)

cv2.imshow("Panorama mitad derecho", trim(I_mid_der_s))
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# UUNIÓN DE IMAGEN MEDIA/DERECHA CON IZQUIERDA=========================
matches_mid_izq = match.knnMatch(descript_mid, descript_izq, k=2)
good_matches_mid_izq = []

# Escoger los mejores puntos obtenidos por ORB entre Imagen media y izq
for m,n in matches_mid_izq:
    if m.distance < 0.7*n.distance:
        good_matches_mid_izq.append(m)
print(len(good_matches_mid_izq))

# Dibujar los "matches" (las correspondencias)
draw_params = dict(matchColor=(0,255,0), singlePointColor = None, flags = 2)
Imatch_3= cv2.drawMatches(I_mid, keypts_mid, I_izq, keypts_izq, good_matches_mid_izq, None, **draw_params)
Imatch_3 = cv2.resize(Imatch_3, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_LINEAR)
cv2.imshow("Correspondencias asdsa", Imatch_3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

if len(good_matches_mid_izq) > MIN_MATCH_COUNT:
    src_pts_midizq = np.float32([ keypts_mid[m.queryIdx].pt for m in good_matches_mid_izq ]).reshape(-1,1,2)
    dst_pts_midizq = np.float32([ keypts_izq[m.trainIdx].pt for m in good_matches_mid_izq ]).reshape(-1,1,2)
    M, mask = cv2.findHomography(src_pts_midizq, dst_pts_midizq, cv2.RANSAC,5.0)
    h,w = I_mid_gr.shape
    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
    dst_mid_izq = cv2.perspectiveTransform(pts, M)
    img2 = cv2.polylines(I_izq_gr, [np.int32(dst_mid_izq)], True, 255, 3, cv2.LINE_AA)
    img2 = cv2.resize(img2, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_LINEAR)
    cv2.imshow("Area de superposicion", img2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    print("Estamos bien")
else:
    print ("No se encuentran suficientes correspondencias - {}/{}".
           format(len(good_matches),MIN_MATCH_COUNT))



# Panorama usando la homografía
I_mid_izq = cv2.warpPerspective(I_mid, M, (I_izq.shape[1] + I_mid.shape[1], I_izq.shape[0]))
I_mid_izq[0:I_izq.shape[0],0:I_izq.shape[1]] = I_izq
I_mid_izq = trim(I_mid_izq)
I_mid_izq_s = cv2.resize(I_mid_izq, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_LINEAR)
cv2.imshow("Panorama completo", trim(I_mid_izq_s))
cv2.imwrite("panorama_2.jpg",I_mid_izq)
cv2.waitKey(0)
cv2.destroyAllWindows()
