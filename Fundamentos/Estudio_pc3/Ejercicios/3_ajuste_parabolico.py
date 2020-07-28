# -*- coding: utf-8 -*-

import Tkinter
import numpy as np
import matplotlib.pyplot as plt

#===============================================
#		Ajuste parabólico
#===============================================

pi = np.pi
# Puntos del ajuste 
q1 = 0
q2 = 2*pi
q3 = pi/2

t1 = 0
t2 = 2
t3 = 3

dt = 0.6

q1_dot = 0
q3_dot = 0