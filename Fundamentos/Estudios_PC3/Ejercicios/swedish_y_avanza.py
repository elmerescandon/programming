# -*- coding: utf-8 -*-
import Tkinter
import numpy as np
import matplotlib.pyplot as plt


def fk_swed_y(phi,r,l): 
	'''
	Función que retorna el twist en un plano 
	de un robot omnidireccional holonómico con 3 ruedas
	tipo Swedish(90).
	Input: np.array(ph1,ph2,ph3) / radio / longitud
	Output: np.array(x,y,alpha)
	'''
	x = (r/3)*(2*phi[1] - phi[0] - phi[2])
	y = (r*np.sqrt(3)/3)*(phi[0]-phi[2])
	alpha = (-r/(3*l))*(phi[0]+phi[1]+phi[2])

	return np.array([x,y,alpha])

def fkinv_swed_y(twist,r,l): 
	'''
	Función que retorna el twist en un plano 
	de un robot omnidireccional holonómico con 3 ruedas
	tipo Swedish(90).
	Input np.array(x,y,alpha) / radio / longitud
	Output np.array(ph1,ph2,ph3) 
	'''
	phi1 = (1/r)*(np.sqrt(3)*twist[0]/2 - 0.5*twist[1] - l*twist[2])
	phi2 = (1/r)*(twist[1] - l*twist[2])
	phi3 = (-1/r)*(np.sqrt(3)*twist[0]/2 + 0.5*twist[1] + l*twist[2])
	return np.array([phi1,phi2,phi3])


print(fk_swed_y(np.array([10,10,10]),0.05,0.3))