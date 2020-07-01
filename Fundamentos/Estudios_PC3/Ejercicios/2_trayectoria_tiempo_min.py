# -*- coding: utf-8 -*-

import Tkinter
import numpy as np
import matplotlib.pyplot as plt

#===============================================
#		Trayectoria de tiempo mínimo
#===============================================


# Menos tiempo posible - Usar Bang Bang 
q_dot_max = 2
q_dotdot_max = 2.5

q0 = -1.5
qf = 1.5

tf = 2*np.sqrt((qf-q0)/q_dotdot_max)
ts = tf/2

# Realizar trayectoria 
dt = 0.01
t0 = 0


tt = 1+tf+1


t = np.linspace(0,tf,tf/dt)
q = np.zeros(len(t))
q_dot = np.zeros(len(t))
q_dot_dot = np.zeros(len(t))

for n in range(len(t)): 
	if 0<t[n]<= ts:
		q[n] = q0 + (0.5)*q_dotdot_max*(t[n]**2)
		q_dot[n] = q_dotdot_max*t[n]
		q_dot_dot[n] = q_dotdot_max
	elif ts<t[n]<=tf:
		q[n] = qf -0.5*q_dotdot_max*(t[n]-tf)**2
		q_dot[n] = -q_dotdot_max*(t[n]-tf)
		q_dot_dot[n] = -q_dotdot_max
	elif t[n] < 0: 
		q[n] = q0
	elif t[n] > tf: 
		q[n] = qf


plt.title("Trayectoria Bang Bang")
plt.subplot(311)
plt.plot(t,q)
plt.grid()
plt.xlabel("Tiempo(s)")
plt.ylabel("Posicion (rad)")
plt.subplot(312)
plt.plot(t,q_dot)
plt.grid()
plt.xlabel("Tiempo(s)")
plt.ylabel("Velocidad (rad/s)")
plt.subplot(313)
plt.plot(t,q_dot_dot)
plt.grid()
plt.xlabel("Tiempo(s)")
plt.ylabel("Velocidad (rad/s)")
plt.show()
