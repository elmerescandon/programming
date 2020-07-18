# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np



def leer_landmarks(filename):
    """
    Retorna una lista de landmarks en el sistema inercialLee los landmarks

    El formato es un diccionario que contiene las posiciones de cada landmark,
    asociadas a su ID: {ID, (x, y)}
    """
    landmarks = dict()
    f = open(filename)
    for linea in f:
        linea_s = linea.split('\n')
        linea_spl  = linea_s[0].split(' ')
        landmarks[int(linea_spl[0])] = (float(linea_spl[1]), float(linea_spl[2]))
    return landmarks


def leer_sensor_odom(filename):
    """
    Lee los datos de odometría y del sensor (rango y distancia)

    El formato retornado para cada instante de tiempo es un diccionario con
    claves 'odom' y 'sensor', donde 'odom' contiene los valores r1, r2 , t
    (del) modelo de movimiento, y 'sensor' contiene las lecturas de rango

    """
    sensor_data = dict()
    lm_ids = []; ranges=[];
    first_time = True
    timestamp = 0
    f = open(filename)
    for line in f:
        line_s = line.split('\n')
        line_spl = line_s[0].split(' ')
        if (line_spl[0]=='ODOMETRY'):
            sensor_data[timestamp,'odom'] = {'r1':float(line_spl[1]),'t':float(line_spl[2]),'r2':float(line_spl[3])}
            if first_time:
                first_time = False
            else:
                sensor_data[timestamp,'sensor'] = {'id':lm_ids,'rango':ranges}
                lm_ids=[]; ranges = [];
            timestamp = timestamp+1
        if(line_spl[0]=='SENSOR'):
            lm_ids.append(int(line_spl[1]))
            ranges.append(float(line_spl[2]))
        sensor_data[timestamp-1,'sensor'] = {'id':lm_ids,'rango':ranges}
    return sensor_data


def plot_robot(mu, sigma, landmarks, map_limits):
    """
    Visualiza el estado del filtro de Kalman

    Muestra la media y la desviación estándar de la estimación, y la posición
    de los landmarks

    """
    lx=[]; ly=[]
    for i in range (len(landmarks)):
        lx.append(landmarks[i+1][0])
        ly.append(landmarks[i+1][1])
    # MEdia de la estimación
    estimated_pose = mu
    # Calcular y graficar el elipse de covarianza
    covariance = sigma[0:2,0:2]
    eigenvals, eigenvecs = np.linalg.eig(covariance)
    # Máximo y mínimo autovalor
    max_ind = np.argmax(eigenvals)
    max_eigvec = eigenvecs[:,max_ind]
    max_eigval = eigenvals[max_ind]
    # Menor autovalor y autovector
    min_ind = 0
    if max_ind == 0:
        min_ind = 1
    #min_eigvec = eigenvecs[:,min_ind]
    min_eigval = eigenvals[min_ind]
    # Valor de chi-cuadrado para el intervalo de confianza de sigma
    chisquare_scale = 2.2789
    # Calcular ancho y alto de la elipse de covarianza
    width = 2 * np.sqrt(chisquare_scale*max_eigval)
    height = 2 * np.sqrt(chisquare_scale*min_eigval)
    angle = np.arctan2(max_eigvec[1],max_eigvec[0])
    # Generar la elipse de covarianza
    ell = Ellipse(xy=[estimated_pose[0],estimated_pose[1]], width=width, height=height, angle=angle/np.pi*180)
    ell.set_alpha(0.25)
    # Graficar el filtro y la covarianza
    plt.clf()
    plt.gca().add_artist(ell)
    plt.plot(lx, ly, 'bo',markersize=10)
    plt.quiver(estimated_pose[0], estimated_pose[1], np.cos(estimated_pose[2]), np.sin(estimated_pose[2]), angles='xy',scale_units='xy')
    plt.axis(map_limits)
    plt.pause(0.001)
