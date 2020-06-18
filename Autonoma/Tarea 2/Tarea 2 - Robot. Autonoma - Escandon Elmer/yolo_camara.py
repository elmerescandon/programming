# Cargar librerías
import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

# Pesos pre-entrenados y configuación de la red neuronal
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

# Instancia que capturará el video
cam = cv2.VideoCapture(0)

# Clases de los pesos
clases = [] # Lees los valores string del código
with open("coco.names", "r") as f:
    clases = [line.strip() for line in f.readlines()]
nombres_capas = net.getLayerNames() # Arquitectura de YOLOv3

# Capas de salida, muestran el porcentaje de clasificación
capas_salida = [nombres_capas[i[0]-1] for i in net.getUnconnectedOutLayers()]

# Colores para graficar rectángulos
colors = np.random.uniform(0, 255, size=(len(clases), 3))
Isize = None # Variable para almacenar el tamaño de la imagen

while(cam.isOpened()):
    retval, frame = cam.read() #   retval=1 (valid img) / frame es la imagen
    if retval==True:    # Solo si se tiene una imagen válida
        if (Isize==None):
            Isize = frame.shape
            print("Tamaño de la imagen: ", Isize) #
        frame = cv2.flip(frame, 1)

        # PROCESAMIENTO DE RED NEURONAL CONVOLUCIONAL YOLOv3 ==================
        # Cargar la imagen
        t = time.time() # Medir el tiempo en realizar la detección
        height, width, channels = frame.shape

        # Extraer algunas características de la imagen
        # sigma = 0.00392, sin reducción de media, cambio de BGR a RGB
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0,0,0), True, crop=False)

        # Detección de objetos usando la red neuronal
        net.setInput(blob)
        salidas_red = net.forward(capas_salida) # 3 capas retornan valores de clasificación

        elapsed = time.time()  - t # Finalizar tiempo medido
        print("Tiempo entrenamiento:{}".format(elapsed))

        IDs_clases = [];confiabilidades = [];boxes = []

        t = time.time() # Tomar el tiempo en graficar la imagen

        for salida in salidas_red: # Para cada vector de capa de salida (3)
            for deteccion in salida:
                scores = deteccion[5:] # Lista con los porcentajes
                ID_clase = np.argmax(scores) # Clase del objeto de mayor prob.
                confiabilidad = scores[ID_clase] # % del de mayor prob.

                if confiabilidad > 0.5:  # Objeto detectado

                    x_centro = int(deteccion[0]*width) # Centro del objeto
                    y_centro = int(deteccion[1]*height)

                    w = int(deteccion[2]*width)  # Tamaño del objeto
                    h = int(deteccion[3]*height)

                    x = int(x_centro - w/2) # Coordenadas del rectángulo
                    y = int(y_centro - h/2) # alrededor del objeto

                    boxes.append([x, y, w, h]) # Tamaño de la caja
                    confiabilidades.append(float(confiabilidad))
                    IDs_clases.append(ID_clase)

        indices = cv2.dnn.NMSBoxes(boxes, confiabilidades, 0.5, 0.4)
        font = cv2.FONT_HERSHEY_PLAIN

        # Dibujar las cajas en la imagen
        for i in range(len(boxes)):
            if i in indices:
                x, y, w, h = boxes[i]
                label = str(clases[IDs_clases[i]])
                color = colors[i]
                cv2.rectangle(frame, (x,y), (x+w, y+h), color, 2)
                cv2.putText(frame, label, (x,y+30), font, 2, color, 3)

        # Si reconoce más de 3 objetos, guardar el frame en .jpg
        if len(boxes) >= 3:
            cv2.imwrite('imagen_yolov3.jpg',frame)
        elapsed  = time.time() - t # Tiempo de dibujo de cajas
        print("Tiempo en dibujar:{}".format(elapsed))

        cv2.imshow('My camera', frame)         # Mostrar la imagen de la cámara

        if (cv2.waitKey(30) & 0xFF) == ord('q'): # Salir
            break
    else:
        break

# Cuando termine de usarse la cámara, eliminar los recursos
cam.release()
cv2.destroyAllWindows()
