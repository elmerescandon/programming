import sympy as sp
from sympy.matrices import Matrix
sp.init_printing()

# ========================================
# Funciones de Representaciones Espaciales
# ========================================

def crossproduct(a, b):
    '''
    Funcion simbolica que retorna producto
    cruz de los vectores a y b (ambos arrays)
    '''
    x = Matrix([[a[1] * b[2] - a[2] * b[1]],
                [a[2] * b[0] - a[0] * b[2]],
                [a[0] * b[1] - a[1] * b[0]]])
    return x

def strot(ang, axis):
    '''
    Funcion simbolica que retorna matriz de rotacion
    simbolica, tiene como entrada el ángulo giro
    y un caractér que represente el eje (x,y,z)
    '''
    if (axis == 'y'):
        R = Matrix([[sp.cos(ang), 0, sp.sin(ang), 0],
                    [0, 1,        0, 0],
                    [-sp.sin(ang), 0, sp.cos(ang), 0],
                    [0, 0, 0, 1]])
    elif axis == 'z':
        R = Matrix([[sp.cos(ang), -sp.sin(ang), 0, 0],
                    [sp.sin(ang),  sp.cos(ang), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])
    elif axis == 'x':
        R = Matrix([[1,       0,        0, 0],
                    [0, sp.cos(ang), -sp.sin(ang), 0],
                    [0, sp.sin(ang),  sp.cos(ang), 0],
                    [0, 0, 0, 1]])
    return R


def strasl(l1, l2, l3):
    '''
    Retorna matriz de transformación homogénea de
    traslación dado un vector l en la forma de 3
    inputs.
    '''
    Rx = Matrix([[1, 0, 0, l1],
                 [0, 1, 0, l2],
                 [0, 0, 1, l3],
                 [0, 0, 0, 1]])
    return Rx

def srot(th, a):
    """
    Genera una matriz de Rotación alrededor de cualquier
    eje independiente usando los 9 parámetros para la matriz de rotación
    Entradas: th -> sexagesimales
              a -> eje de rotacion deseado
    """
    # th = sp.deg2rad(th)
    cos = sp.cos
    sin = sp.sin
    if (a == 'x'):
        R = Matrix([[1,       0,        0],
                    [0, cos(th), -sin(th)],
                    [0, sin(th),  cos(th)]])
    elif (a == 'y'):
        R = Matrix([[cos(th),      0, sin(th)],
                    [0,      1,      0],
                    [-sin(th),     0, cos(th)]])
    elif (a == 'z'):
        R = Matrix([[cos(th), -sin(th), 0],
                    [sin(th), cos(th), 0],
                    [0,      0,      1]])
    return R
# ========================================
# Funciones para obtención de cinemática
# ========================================

def sdh(d, theta, a, alpha):

    T = Matrix([[sp.cos(theta), -sp.cos(alpha) * sp.sin(theta),  sp.sin(alpha) * sp.sin(theta), a * sp.cos(theta)],
                [sp.sin(theta),  sp.cos(alpha) * sp.cos(theta), -sp.sin(alpha) * sp.cos(theta), a * sp.sin(theta)],
                [0,                      sp.sin(alpha),            sp.cos(alpha),            d],
                [0,                               0,                     0,            1]])

    return T

def jacob_g(DH):
    '''
    Función simbólica que realiza el Jacobiano geométrico dado los parámetros
    Denavit-Hatenberg. Retorna una lista que contiene las matrices de
    transformación y la matríz del jacobiano Geométrico
    DH de la forma(d, theta, a, alpha,'p/r'prismatico/rotacional)
    '''
    T_ref = []  # Matriz que almacena los valores de T
    T = Matrix([[1, 0, 0, 0],  # Inicializar Matriz de tranformacion
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])
    z0 = Matrix([[0], [0], [1]])
    p0 = Matrix([[0], [0], [0]])
    J = Matrix([])
    for i in range(len(DH)):
        Ti = sp.simplify(sdh(DH[i][0], DH[i][1], DH[i][2], DH[i][3]))
        T = T * Ti
        T_ref.append(T)

    for n in range(len(DH)):
        if (n == 0):
            z = z0
            p = p0
        else:
            z = T_ref[n - 1][0:3, 2]
            p = T_ref[n - 1][0:3, 3]

        if (DH[i][4] == 'r'):
            Jv = crossproduct(z, T_ref[len(DH) - 1][0:3, 3] - p)
            if n == 2:
                print(z)
                print(p)
                print(T_ref[len(DH) - 1][0:3, 3])
            Jw = z

        elif (DH[i][4] == 'p'):
            Jv = z
            Jw = 0
        J1 = sp.Matrix.vstack(Jv, Jw)
        J = sp.Matrix.hstack(J, J1)
    return T_ref, sp.simplify(J)



# ================================================
# Funciones para obteción dinámica Euler-Lagrange
# ===============================================

def linear_velocity_CoM(center_points, qs, z_axis, tipos):
    '''
    Velocidad lineal del centro de masa para articulaciones rotacionales
    Se asume que los center_points estan colocados de manera ordenada
    Inputs:
        cp = [c1,c2,c3,...,cn]
        qs = [q1,q2,q3,...,qn]
        z_axis = [z_0,  z_1,...,z_n]
        tipos = ['p','  r','r'] (Type of joints)
    Output:
        Js (Matriz simbólica con la velocidad lineal para todos los
            centros de masa de cada eslabón del robot)
    '''
    Js = []
    for n in center_points:
        Jv = sp.Matrix([])
        for m in qs:
            if tipos[qs.index(m)] == 'r':
                a = n.diff(m)
                Jv = sp.Matrix.hstack(Jv, a)
            elif tipos[qs.index(m)] == 'p':
                if center_points.index(n) >= qs.index(m):
                    Jv = sp.Matrix.hstack(Jv, z_axis[qs.index(m)])
                else:
                    Jv = sp.Matrix.hstack(Jv, sp.Matrix([[0], [0], [0]]))
        Js.append(Jv)
    return Js

def angular_velocity_CoM(center_points, axis, tipos):
    '''
    Velocidad angular del centro de masa para articulaciones
    rotacionales
    input:
        cp = [c1,c2,c3,...,cn]
        z = [z0,z1,...,zn]
        tipos = ['p','r','r',...] (Type of joints)
    output:
        Js = Matriz simbólica de jacobiano para la velocidad angular
        del centro de masa de cada eslabón del robot
    '''
    Js = []
    for n in range(len(center_points)):
        Jv = sp.Matrix([])
        for m in range(len(axis)):
            if n >= m and tipos[m] == 'r':
                Jv = sp.Matrix.hstack(Jv, axis[m])
            else:
                Jv = sp.Matrix.hstack(Jv, sp.Matrix([[0], [0], [0]]))
        Js.append(Jv)
    return Js

def Mass_Matrix(Jv, Jw, R, m, I):
    '''
    Matriz de masa simbólica dado un:
    - Jacobiano de velocidad lineal del CoM
    - Jacobiano de velocidad angular del CoM
    - Matrices de rotación de los sitemas
    - vector de masa de cada eslabón (m=[m1,m2,m3,...,mn])
    - Matriz de inercia para cada eslabón con respecto
      al sistema de referencia de su centro de masa
    '''
    Mass = sp.zeros(len(m), len(m))
    for a in range(len(m)):
        Mass = m[a] * (Jv[a].T) * (Jv[a]) + (Jw[a].T) * R[a] * I[a] * (R[a].T) * (Jw[a]) + Mass
    return Mass

def Christoffel_symbols(Mass_Matrix, qs, i, j, k):
    c1 = Mass_Matrix[i, j].diff(qs[k])
    c2 = Mass_Matrix[i, k].diff(qs[j])
    c3 = Mass_Matrix[j, k].diff(qs[i])
    return sp.simplify((1 / 2) * (c1 + c2 - c3))

def Coriolis_Matrix(Mass_Matrix, q_dots, qs):
    Coriolis = sp.zeros(Mass_Matrix.shape[1], Mass_Matrix.shape[1])
    for i in range(Coriolis.shape[1]):
        for j in range(Coriolis.shape[1]):
            for k in range(len(qs)):
                c_ijk = Christoffel_symbols(Mass_Matrix, qs, i, j, k)
                c_ijk = c_ijk * q_dots[k]
                Coriolis[i, j] = c_ijk + Coriolis[i, j]
    return sp.simplify(Coriolis)

def GravitationalForce_vector(Jv, m, g):
    Gravitational = sp.zeros(len(m), 1)
    for i in range(len(Jv)):
        for k in range(len(m)):
            g_acum = ((Jv[k][:, i]).T) * m[k] * g
            Gravitational[i] = -g_acum[0] + Gravitational[i]
    return sp.simplify(Gravitational)
