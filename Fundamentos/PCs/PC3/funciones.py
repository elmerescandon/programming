import sympy as sp
import numpy as np
from sympy.matrices import Matrix
sp.init_printing()

sin = sp.sin
cos = sp.cos


def crossproduct(a, b):
    '''
    Funcion simbolica que retorna producto
    cruz de los vectores a y b (ambos arrays)
    '''
    x = Matrix([[a[1]*b[2] - a[2]*b[1]],
                [a[2]*b[0] - a[0]*b[2]],
                [a[0]*b[1] - a[1]*b[0]]])
    return x


def stroty(ang):

    Ry = Matrix([[sp.cos(ang), 0, sp.sin(ang), 0],
                 [0, 1,        0, 0],
                 [-sp.sin(ang), 0, sp.cos(ang), 0],
                 [0, 0, 0, 1]])
    return Ry


def strotz(ang):
    Rz = Matrix([[sp.cos(ang), -sp.sin(ang), 0, 0],
                 [sp.sin(ang),  sp.cos(ang), 0, 0],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1]])
    return Rz


def strotx(ang):
    Rx = Matrix([[1,       0,        0, 0],
                 [0, sp.cos(ang), -sp.sin(ang), 0],
                 [0, sp.sin(ang),  sp.cos(ang), 0],
                 [0, 0, 0, 1]])
    return Rx


def strasl(l1, l2, l3):
    Rx = Matrix([[1, 0, 0, l1],
                 [0, 1, 0, l2],
                 [0, 0, 1, l3],
                 [0, 0, 0, 1]])
    return Rx

def sdh(d, theta, a, alpha):

    T = Matrix([[sp.cos(theta), -sp.cos(alpha)*sp.sin(theta), sp.sin(alpha)*sp.sin(theta), a*sp.cos(theta)],
                [sp.sin(theta),  sp.cos(alpha)*sp.cos(theta), -
                 sp.sin(alpha)*sp.cos(theta), a*sp.sin(theta)],
                [0,                      sp.sin(alpha),            sp.cos(alpha),            d],
                [0,                               0,                     0,            1]])

    return T

# Grupo de funciones para la PC3 - Fundamentos de Robótica
# Raúl Escandón -

# Funciones Simbólicas

def linear_velocity_CoM(center_points,qs,z_axis,tipos):
    '''
    Velocidad lineal del centro de masa para articulaciones rotacionales
    Se asume que los center_points estan colocados de manera ordenada
    cp = [c1,c2,c3,...,cn]
    qs = [q1,q2,q3,...,qn]
    z_axis = [z_0,z_1,...,z_n]
    '''
    Js = []
    for n in center_points:
        Jv = sp.Matrix([])
        for m in qs:
            if tipos[qs.index(m)] == 'r':
                a = n.diff(m)
                Jv = sp.Matrix.hstack(Jv,a)
            elif tipos[qs.index(m)] == 'p':
                if center_points.index(n)>= qs.index(m):
                    Jv = sp.Matrix.hstack(Jv,z_axis[qs.index(m)])
                else:
                    Jv = sp.Matrix.hstack(Jv,sp.Matrix([[0],[0],[0]]))
        Js.append(Jv)
    return Js

def angular_velocity_CoM(center_points,axis,tipos):
    '''
    Velocidad angular del centro de masa para articulaciones
    rotacionales
    input: z = [z0,z1,...,zn]
    '''
    Js = []
    for n in range(len(center_points)):
        Jv = sp.Matrix([])
        for m in range(len(axis)):
            if n>=m and tipos[m]=='r':
                Jv = sp.Matrix.hstack(Jv,axis[m])
            else:
                Jv = sp.Matrix.hstack(Jv,sp.Matrix([[0],[0],[0]]))
        Js.append(Jv)
    return Js

def Mass_Matrix(Jv,Jw,R,m,I):
    Mass = sp.zeros(len(m),len(m))
    for a in range(len(m)):
        Mass = m[a]*(Jv[a].T)*(Jv[a]) + (Jw[a].T)*R[a]*I[a]*(R[a].T)*(Jw[a]) + Mass
    return sp.simplify(Mass)

def Christoffel_symbols(Mass_Matrix,qs,i,j,k):
    c1 = Mass_Matrix[i,j].diff(qs[k])
    c2 = Mass_Matrix[i,k].diff(qs[j])
    c3 = Mass_Matrix[j,k].diff(qs[i])
    return sp.simplify((1/2)*(c1+c2-c3))

def Coriolis_Matrix(Mass_Matrix,q_dots,qs):
    Coriolis = sp.zeros(Mass_Matrix.shape[1],Mass_Matrix.shape[1])
    for i in range(Coriolis.shape[1]):
        for j in range(Coriolis.shape[1]):
            for  k in range(len(qs)):
                c_ijk = Christoffel_symbols(Mass_Matrix,qs,i,j,k)
                c_ijk = c_ijk*q_dots[k]
                Coriolis[i,j] = c_ijk + Coriolis[i,j]
    return sp.simplify(Coriolis)

def GravitationalForce_vector(Jv,m,g):
    Gravitational = sp.zeros(len(m),1)
    for i in range(len(Jv)):
        for k in range(len(m)):
            g_acum = ((Jv[k][:,i]).T)*m[k]*g
            Gravitational[i] = -g_acum[0] + Gravitational[i]
    return sp.simplify(Gravitational)
