import numpy as np
import sympy as sp
from sympy.matrices import Matrix
import matplotlib.pyplot as plt


def fk_2(q1,q2,q3):
    cos = np.cos
    sin = np.sin
    sqrt = np.sqrt
    l1 = 125
    l2 = 25
    l3 = 105
    l4 = 120
    d1 = 75
    forw_k = np.array([ [-l1 - l3*sin(q2) - l4*sin(q2 + q3)],
                        [d1 + l2*cos(q1) - l3*sin(q1)*cos(q2) - l4*sin(q1)*cos(q2 + q3)],
                        [-l2*sin(q1) - l3*cos(q1)*cos(q2) - l4*cos(q1)*cos(q2 + q3)],
                        [0.5*sqrt(sin(q1)*sin(q2 + q3) - sin(q1) - sin(q2 + q3) + 1)],
                        [0.5*(sin(q2 + q3) - 1)*cos(q1)/sqrt(sin(q1)*sin(q2 + q3) - sin(q1) - sin(q2 + q3) + 1)],
                        [0.5*cos(q1)*cos(q2 + q3)/sqrt(sin(q1)*sin(q2 + q3) - sin(q1) - sin(q2 + q3) + 1)],
                        [-0.5*(sin(q1) - 1)*cos(q2 + q3)/sqrt(sin(q1)*sin(q2 + q3) - sin(q1) - sin(q2 + q3) + 1)]])
    # Primero x,y,z,omega,ex,ey,ez

    return np.array([forw_k[0,0],forw_k[1,0],forw_k[2,0],forw_k[3,0],forw_k[4,0],forw_k[5,0],forw_k[6,0]])


def jacob_2(q1,q2,q3):
    cos = np.cos
    sin = np.sin
    sqrt = np.sqrt
    l1 = 125
    l2 = 25
    l3 = 105
    l4 = 120
    d1 = 75
    J_f2  = np.array([[0, -l3*cos(q2) - l4*cos(q2 + q3), -l4*cos(q2 + q3)], [-l2*sin(q1) - l3*cos(q1)*cos(q2) - l4*cos(q1)*cos(q2 + q3), (l3*sin(q2) + l4*sin(q2 + q3))*sin(q1), l4*sin(q1)*sin(q2 + q3)], [-l2*cos(q1) + l3*sin(q1)*cos(q2) + l4*sin(q1)*cos(q2 + q3), (l3*sin(q2) + l4*sin(q2 + q3))*cos(q1), l4*sin(q2 + q3)*cos(q1)], [0.25*(sin(q2 + q3) - 1)*cos(q1)/sqrt(sin(q1)*sin(q2 + q3) - sin(q1) - sin(q2 + q3) + 1), 0.25*(sin(q1) - 1)*cos(q2 + q3)/sqrt(sin(q1)*sin(q2 + q3) - sin(q1) - sin(q2 + q3) + 1), 0.25*(sin(q1) - 1)*cos(q2 + q3)/sqrt(sin(q1)*sin(q2 + q3) - sin(q1) - sin(q2 + q3) + 1)], [-0.25*(sin(q1) - 1)**2*(sin(q2 + q3) - 1)**2/(sin(q1)*sin(q2 + q3) - sin(q1) - sin(q2 + q3) + 1)**(3/2), 0.25*cos(q1)*cos(q2 + q3)/sqrt(sin(q1)*sin(q2 + q3) - sin(q1) - sin(q2 + q3) + 1), 0.25*cos(q1)*cos(q2 + q3)/sqrt(sin(q1)*sin(q2 + q3) - sin(q1) - sin(q2 + q3) + 1)], [-0.25*(sin(q1) - 1)*cos(q2 + q3)/sqrt(sin(q1)*sin(q2 + q3) - sin(q1) - sin(q2 + q3) + 1), 1.0*(0.5*sin(q2 + q3) + 0.125*cos(2*q2 + 2*q3) - 0.375)*cos(q1)/((sin(q2 + q3) - 1)*sqrt(sin(q1)*sin(q2 + q3) - sin(q1) - sin(q2 + q3) + 1)), 1.0*(0.5*sin(q2 + q3) + 0.125*cos(2*q2 + 2*q3) - 0.375)*cos(q1)/((sin(q2 + q3) - 1)*sqrt(sin(q1)*sin(q2 + q3) - sin(q1) - sin(q2 + q3) + 1))], [-0.25*cos(q1)*cos(q2 + q3)/sqrt(sin(q1)*sin(q2 + q3) - sin(q1) - sin(q2 + q3) + 1), (sin(q1) - 1)**2*(-0.5*sin(q2 + q3) - 0.125*cos(2*q2 + 2*q3) + 0.375)/(-sin(q1) - sin(q2 + q3) + cos(-q1 + q2 + q3)/2 - cos(q1 + q2 + q3)/2 + 1)**(3/2), (sin(q1) - 1)**2*(-0.5*sin(q2 + q3) - 0.125*cos(2*q2 + 2*q3) + 0.375)/(-sin(q1) - sin(q2 + q3) + cos(-q1 + q2 + q3)/2 - cos(q1 + q2 + q3)/2 + 1)**(3/2)]])
    return J_f2


w = 0.5
ex = -0.5
ey = 0.5
ez = 0.5
q_vector = []
epsilon = 1e-2
max_iter = 2000 # Maximum number of iterations
alpha = 0.00003
xd = np.array([-125, 100,-225,w,ex,ey,ez]) # Valor deseado en el espacio cartesiano
q = np.deg2rad(np.array([-30, 60,45])) # Valor inicial en el espacio articular
q_vector = np.zeros((max_iter,7))
num = 0
for i in range(max_iter):
    q1 = q[0]; q2 = q[1];q3=q[2] # q = [0,0,0]
    f = fk_2(q1,q2,q3)
    J1 = jacob_2(q1,q2,q3)
    e = xd-f
    # q = q + np.linalg.pinv(J1).dot(e) # Metodo de Newton
    q = q + alpha*((J1.T).dot(e))
    q = q%(np.pi*2)
    q_vector[i,:] = f# q%(np.pi*2)
    num = i
    if (np.linalg.norm(e)< epsilon):
        print('SALIR')
        break

print(e)
grid = plt.GridSpec(4, 4, wspace=0.4, hspace=0.3)
plt.suptitle(r'alfa = 0.00003, max_iteraciones = 2000', fontsize=16)
plt.subplot(grid[0,0:2])
plt.plot(np.linspace(0,num,num),q_vector[0:num,0])
plt.xlabel(r'Iteración(n)')
plt.ylabel(r'X(mm)')
plt.grid();



plt.subplot(grid[0,2:4])
plt.plot(np.linspace(0,num,num),q_vector[0:num,1])
plt.grid();
plt.xlabel(r'Iteración(n)')
plt.ylabel(r'Y(mm)')


plt.subplot(grid[1,0:2])
plt.plot(np.linspace(0,num,num),q_vector[0:num,2])
plt.grid();
plt.xlabel(r'Iteración(n)')
plt.ylabel(r'Z(mm)')


plt.subplot(grid[1,2:4])
plt.plot(np.linspace(0,num,num),q_vector[0:num,3])
plt.grid();
plt.xlabel(r'Iteración(n)')
plt.ylabel(r'omega')


plt.subplot(grid[2,0:2])
plt.plot(np.linspace(0,num,num),q_vector[0:num,4])
plt.grid();
plt.xlabel(r'Iteración(n)')
plt.ylabel(r'eps-x')


plt.subplot(grid[2,2:4])
plt.plot(np.linspace(0,num,num),q_vector[0:num,5])
plt.grid();
plt.xlabel(r'Iteración(n)')
plt.ylabel(r"eps-y")
plt.subplot(grid[3,:])


plt.plot(np.linspace(0,num,num),q_vector[0:num,6])
plt.grid();
plt.xlabel(r'Iteración(n)')
plt.ylabel(r'eps-z')
plt.show()
