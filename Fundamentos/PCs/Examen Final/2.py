# Examen Final 2020-1
# Fundamentos de Robótica
# Elmer Raúl Escandón Tufino
# ==================================
# %%Inicializar librerías
import symbolic as sym
import sympy as sp
import numpy as np
import numeric as num
import copy


# %% Funciones a utilizar



# %% Pregunta 1: Robot de GDL
# dh(d, theta, a, alpha):
q = np.array([np.pi/2,0.2,np.pi/6,np.pi/3,0.2])
l2 = 0.4
l3 = 0.3
q2=q[1]; q3= q[2]; q4=q[3];q5=q[4]
q1 = q[0];q2=q[1];q3=q[2];q4=q[3];q5=q[4]
T01 = num.dh(0,q1, 0, 0)
T12 = num.dh(q2,0,0,np.pi/2)
T23 = num.dh(0,q3,l2,np.pi)
T34 = num.dh(0,q4,l3,np.pi/2)
T45 = num.dh(q5,np.pi/2,0,0)
T05 = T01.dot(T12).dot(T23).dot(T34).dot(T45)
pos = T05[0:3,3]
R = T05[0:3,0:3]
angles = num.rpy(R)

print("Posicion en el espacio cartesiano:")
print(np.round(pos,2))
print("Posicion en angulos de Roll,Pitch,Yaw")
print(np.round(np.rad2deg(angles),2))

# Obtención de Jacobiano
def fk(q):
    q2=q[1]; q3= q[2]; q4=q[3];q5=q[4]
    q1 = q[0];q2=q[1];q3=q[2];q4=q[3];q5=q[4]
    T01 = num.dh(0,q1, 0, 0)
    T12 = num.dh(q2,0,0,np.pi/2)
    T23 = num.dh(0,q3,l2,np.pi)
    T34 = num.dh(0,q4,l3,np.pi/2)
    T45 = num.dh(q5,np.pi/2,0,0)
    T05 = T01.dot(T12).dot(T23).dot(T34).dot(T45)
    pos = T05[0:3,3]
    R = T05[0:3,0:3]
    angles = num.rpy(R)
    pose = np.hstak((pos,angles))
    return pose

def  jacob_a(q):

    JT = np.zeros((5,6))
    # Transformacion homogenea inicial (usando q)
    T= fk(q)
    pos = T[0:3,3]
    R = T[0:3,0:3]
    angles = num.rpy(R)
    pose = np.hstak((pos,angles))
    # Iteracion para la derivada de cada columna
    for i in xrange(3):
        # Copiar la configuracion articular inicial
        dq = copy(q)
        # Incrementar la articulacion i-esima usando un delta
        dq[i]=dq[i]+delta#incremento de delta en la artic. i
        # Transformacion homogenea luego del incremento (q+delta)
        dT=fk_pata_pos(dq,pata)
        dquater = rot2quaternion(dT[0:3,0:3])
        dposition = dT[0:3,3] # Posición en el espacio cartesiano
        # Pose tiene la forma = x,y,z,ew,ex,ey,ez
        dpose = np.hstack((dposition,dquater))
        # Aproximacion del Jacobiano de posicion usando diferencias finitas
        JT[[i],:]=(dpose-pose)/delta#se va ajustando artic. por artic.
    J = JT.T
    return J
