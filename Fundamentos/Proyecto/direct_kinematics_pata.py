import numpy as np
import sympy as sp
from gradiente import *
import matplotlib.pyplot as plt


def jacob_1(q11,q12,q13):
    cos = np.cos
    sin = np.sin
    J1_np = np.array([[0, -105*cos(q12) - 120*cos(q12 + q13), -120*cos(q12 + q13)],
                      [-25*sin(q11) + 105*cos(q11)*cos(q12) + 120*cos(q11)*cos(q12 + q13), -105*sin(q11)*sin(q12) - 120*sin(q11)*sin(q12 + q13), -120*sin(q11)*sin(q12 + q13)],
                      [105*sin(q11)*cos(q12) + 120*sin(q11)*cos(q12 + q13) + 25*cos(q11), 105*sin(q12)*cos(q11) + 120*sin(q12 + q13)*cos(q11), 120*sin(q12 + q13)*cos(q11)]])
    return  J1_np

def fk_1(q11,q12,q13):
    cos = np.cos
    sin = np.sin
    F1_np = np.array([[-105*sin(q12) - 120*sin(q12 + q13) + 125],
                      [105*sin(q11)*cos(q12) + 120*sin(q11)*cos(q12 + q13) + 25*cos(q11) + 75],
                      [25*sin(q11) - 105*cos(q11)*cos(q12) - 120*cos(q11)*cos(q12 + q13)]])
    return np.array([F1_np[0,0],F1_np[1,0],F1_np[2,0]])


q_vector = []
epsilon = 1e-3
max_iter = 100 # Maximum number of iterations
alpha = 0.32
xd = np.array([125, 100,-225]) # Valor deseado en el espacio cartesiano
q = np.rad2deg(np.array([0, 30,30])) # Valor inicial en el espacio articular
q_vector = np.zeros((max_iter,3))
num = 0
for i in range(max_iter):
    q1 = q[0]; q2 = q[1];q3=q[2] # q = [0,0,0]
    f = fk_1(q1,q2,q3)
    J1 = jacob_1(q1,q2,q3)
    e = xd-f
    #q = q + np.linalg.inv(J1).dot(e) # Metodo de Newton
    q = q + (np.linalg.inv(J1)).dot(e)
    q_vector[i,:] = f# q%(np.pi*2)
    if (np.linalg.norm(e)< epsilon):
        print(i)
        num = i
        break

plt.subplot(311)
plt.plot(np.linspace(0,num,num),q_vector[0:num,0])
plt.grid();
plt.xlabel('Iteración(n)')
plt.ylabel('X(mm)')
plt.subplot(312)
plt.plot(np.linspace(0,num,num),q_vector[0:num,1])
plt.grid();
plt.xlabel('Iteración(n)')
plt.ylabel('Y(mm)')
plt.subplot(313)
plt.plot(np.linspace(0,num,num),q_vector[0:num,2])
plt.grid();
plt.xlabel('Iteración(n)')
plt.ylabel('Z(mm)')
plt.show()
