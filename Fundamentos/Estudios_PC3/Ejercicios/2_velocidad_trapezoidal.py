# -*- coding: utf-8 -*-

import Tkinter
import numpy as np
import matplotlib.pyplot as plt

#===============================================
#		Velocidad Trapezoidal
#===============================================


# Menos tiempo posible - Datos
q_dot_max = 2
q_dotdot_max = 2.5

q0 = -1.5
qf = 1.5

# Fórmulas
tb = q_dotdot_max/q_dot_max

tf = (tb*q_dot_max + qf - q0)/q_dot_max


# Realizar trayectoria 
dt = 0.01
t0 = 0
tt = 1+tf+1
t = np.linspace(-1,(tt-1),tt/dt)
q = np.zeros(len(t))
q_dot = np.zeros(len(t))
q_dot_dot = np.zeros(len(t))

for n in range(len(t)): 
	if 0<t[n]<= tb:
		q[n] = q0 + (0.5)*(q_dot_max/tb)*(t[n]**2)
		q_dot[n] = (q_dot_max/tb)*t[n]
		q_dot_dot[n] = (q_dotdot_max/tb)

	elif tb<t[n]<=(tf-tb):

		q[n] = q0 -0.5*q_dot_max*tb + q_dot_max*t[n]
		q_dot[n] = q_dot_max
		q_dot_dot[n] = 0

	elif (tf-tb)<t[n]<=tf:
		q[n] = qf - 0.5*(q_dot_max/tb)*(t[n]-tf)**2
		q_dot[n] = (-q_dot_max/tb)*(t[n]-tf)
		q_dot_dot[n] = -q_dot_max/tb

	elif t[n] < 0: 
		q[n] = q0

	elif t[n] > tf: 
		q[n] = qf

print("Tiempo de duración")
print(tf)

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

