import cv2
import numpy as np
import matplotlib.pyplot as plt

net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

# Clases de los pesos
clases = [] # Lees los valores string del código
with open("coco.names", "r") as f:
    clases = [line.strip() for line in f.readlines()]
nombres_capas = net.getLayerNames()
capas_salida = [nombres_capas[i[0]-1] for i in net.getUnconnectedOutLayers()]

# Colores para graficar rectángulos
colors = np.random.uniform(0, 255, size=(len(clases), 3))


# Cargar la imagen
I = cv2.imread("images_prueba/sala.jpg")
height, width, channels = I.shape

# Extraer algunas características de la imagen
blob = cv2.dnn.blobFromImage(I, 0.00392, (416, 416), (0,0,0), True, crop=False)
# Detección de objetos usando la red neuronal
net.setInput(blob)
salidas_red = net.forward(capas_salida)
print(salidas_red)

# Mostrar la información en la pantalla
IDs_clases = []
confiabilidades = []
boxes = []
for salida in salidas_red:
    for deteccion in salida:
        scores = deteccion[5:]
        ID_clase = np.argmax(scores)
        confiabilidad = scores[ID_clase]
        # Objeto detectado
        if confiabilidad > 0.5:
            # Centro del objeto
            x_centro = int(deteccion[0]*width)
            y_centro = int(deteccion[1]*height)
            # Tamaño del objeto
            w = int(deteccion[2]*width)
            h = int(deteccion[3]*height)
            # Coordenadas del rectángulo alrededor del objeto
            x = int(x_centro - w/2)
            y = int(y_centro - h/2)
            boxes.append([x, y, w, h])
            confiabilidades.append(float(confiabilidad))
            IDs_clases.append(ID_clase)

indices = cv2.dnn.NMSBoxes(boxes, confiabilidades, 0.5, 0.4)

font = cv2.FONT_HERSHEY_PLAIN
Iout = I.copy()
for i in range(len(boxes)):
    if i in indices:
        x, y, w, h = boxes[i]
        label = str(clases[IDs_clases[i]])
        color = colors[i]
        cv2.rectangle(Iout, (x,y), (x+w, y+h), color, 2)
        cv2.putText(Iout, label, (x,y+30), font, 2, color, 3)


# Mostrar la imagen usando matplotlib o cv2
USE_PLT = False

# Iout = cv2.resize(Iout, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
# if (USE_PLT):
#     plt.figure(figsize=(9,9))
#     plt.imshow(cv2.cvtColor(Iout, cv2.COLOR_BGR2RGB))
#     plt.axis('off');
#     plt.show()
# else:
#     cv2.imshow("Image", Iout)
#     cv2.imwrite('images_resultado/sala_resultados.jpg',Iout)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
