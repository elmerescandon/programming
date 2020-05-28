import numpy as np
import sympy as sp
from sympy.matrices import Matrix
# Raúl Escandón - Fundamentos de Robótica 2020-1
# Funciones para representación de Cuerpos Rígidos

cos = np.cos
sin = np.sin
pi = np.pi


def rot(th, a):
    """
    Genera una matriz de Rotación alrededor de cualquier
    eje independiente usando los 9 parámetros para la matriz de rotación
    Entradas: th -> sexagesimales
              a -> eje de rotacion deseado
    """
    th = np.deg2rad(th)
    if (a == 'x'):
        R = np.array([[1,       0,        0],
                      [0, cos(th), -sin(th)],
                      [0, sin(th),  cos(th)]])
    elif (a == 'y'):
        R = np.array([[cos(th),      0, sin(th)],
                      [0,      1,      0],
                      [-sin(th),     0, cos(th)]])
    elif (a == 'z'):
        R = np.array([[cos(th), -sin(th), 0],
                      [sin(th), cos(th), 0],
                      [0,      0,    1]])
    return R


def ejeang(R):
    """
    Funcion que devuelve la forma eje-angulo
    a partir de una matriz de rotacion
    Input: R de SO3
    Output: - th (en radianes)
            - u (unitario de forma ux,uy,uz)
    """
    d1 = (R[1, 0] - R[0, 1])**2
    d2 = (R[2, 0] - R[0, 2])**2
    d3 = (R[2, 1] - R[1, 2])**2
    s = np.sqrt(d1+d2+d3)/2
    c = (R[0, 0] + R[1, 1] + R[2, 2] - 1)/2
    th = np.arctan2(s, c)

    temp = np.array([R[2, 1]-R[1, 2], R[0, 2]-R[2, 0], R[1, 0] - R[0, 1]])
    u = 1.0/(2.*np.sin(th))*temp

    return th, u


def skew(u):
    u1 = np.sqrt(u[1, 0]**2 + u[0, 0]**2 + u[2, 0]**2)
    u = u/u1
    su = np.array([[0, -u[2, 0], u[1, 0]],
                   [u[2, 0], 0, -u[0, 0]],
                   [-u[1, 0], u[0, 0], 0]])
    return su


def rodr(th, u):
    """
    Función que retorna una matriz de rotación R
    según un vector u(no necesariamente unitario) y
    un vector th - Notación Eje-Ángulo
    Input: th(deg) - u (ux,uy,uz)
    Output: R (3,3)
     """
    s = skew(u)
    th = np.deg2rad(th)
    Ro = np.eye(3) + s*np.sin(th) + s.dot(s)*(1-np.cos(th))
    return Ro


def matriz_so3(R):
    d = np.round(np.linalg.det(R), 2)
    i = np.round(R.dot(R.T), 2)
    t = i[0, 0] + i[1, 1] + i[2, 2]
    if ((d == 1) and (t == 3)):
        return True
    else:
        return False


def quaterion(R):
    """
    Funcion que retorna el vector de quaterion unitario
    a partir de una matriz de rotacion.
    No considera la forma adicional de operar cuando el angulo es 180
    Lo de vuelve de la forma:
    q = (w,ex,ey,ez)
    """
    omega = (1/2)*(np.sqrt(1+R[0, 0]+R[1, 1]+R[2, 2]))
    ex = (1/(4*omega))*(R[2, 1]-R[1, 2])
    ey = (1/(4*omega))*(R[0, 2]-R[2, 0])
    ez = (1/(4*omega))*(R[1, 0]-R[0, 1])
    q = np.array([[omega],
                  [ex],
                  [ey],
                  [ez]])
    return q


def rquater(q):
    """
    Funcion que retorna la matriz de rotacion
    so3 a partir de un vector de cuaternion
    unitario de forma
    q(w,ex,ey,ez)
    Si se trata de un angulo 0, devuelve la identidad
    """

    # Primera Fila
    r11 = 2*(q[0, 0]**2+q[1, 0]**2) - 1
    r12 = 2*(q[1, 0]*q[2, 0]-q[0, 0]*q[3, 0])
    r13 = 2*(q[1, 0]*q[3, 0]+q[0, 0]*q[2, 0])
    # Segunda Fila
    r21 = 2*(q[1, 0]*q[2, 0]+q[0, 0]*q[3, 0])
    r22 = 2*(q[0, 0]**2+q[2, 0]**2) - 1
    r23 = 2*(q[2, 0]*q[3, 0]-q[0, 0]*q[1, 0])
    # Tercera fila
    r31 = 2*(q[1, 0]*q[3, 0]-q[0, 0]*q[2, 0])
    r32 = 2*(q[2, 0]*q[3, 0]+q[0, 0]*q[1, 0])
    r33 = 2*(q[0, 0]**2+q[3, 0]**2) - 1
    R = np.array([[r11, r12, r13],
                  [r21, r22, r23],
                  [r31, r32, r33]])
    return R


def cruz(a, b):
    c = np.array([[a[1, 0]*b[2, 0] - a[2, 0]*b[1, 0]],
                  [a[2, 0]*b[0, 0] - a[0, 0]*b[2, 0]],
                  [a[0, 0]*b[1, 0] - a[1, 0]*b[0, 0]]])

    return c


def rod_vect(p, u, th):
    """
    Función que retorna un vector
    y recibe el vector de giro (no necesariamente normalizado)
    y el theta.
    Input: vector (p) , u, th
    Output: vector resultante (p)
    """
    u1 = np.sqrt(u[1, 0]**2 + u[0, 0]**2 + u[2, 0]**2)
    u = u/u1
    temp = cruz(u, p)
    pb = p*np.cos(th) + temp*np.sin(th) + u*(u.T.dot(p))*(1-np.cos(th))
    return pb


def productoquater(a, b):
    """
    Función que retorna el producto de dos cuaterniones unitarios
    de la forma (w,ex,ey,ez)
    Inputs: a y b
    Output: q (quaternion de forma)(w,ex,ey,ez)
    """
    askew = np.array([[a[0, 0], -a[1, 0], -a[2, 0], -a[3, 0]],
                      [a[1, 0],  a[0, 0], -a[3, 0],  a[2, 0]],
                      [a[2, 0],  a[3, 0],  a[0, 0], -a[1, 0]],
                      [a[3, 0], -a[2, 0],  a[1, 0],  a[0, 0]]])
    q = askew.dot(b)
    return q


def vecquater(v, q):
    """
    Función que retorna el vector dado una transformación
    y un cuaternion
    Inputs: v(vector columna) y q(cuaternion de forma (w,ex,ey,ez))
    Output: vp (vector rotado)(x,y,z)
    """
    qconj = np.array([[q[0, 0]],
                      [-q[1, 0]],
                      [-q[2, 0]],
                      [-q[3, 0]]])
    vq = np.array([[0],
                   [v[0, 0]],
                   [v[1, 0]],
                   [v[2, 0]]])
    temp = productoquater(q, vq)
    vpq = productoquater(temp, qconj)
    vp = np.array([[vpq[1, 0]],
                   [vpq[2, 0]],
                   [vpq[3, 0]]])
    return vp


def transmaxtrix(R, p):
    """
    Función que retorna la matriz de transformación
    homogénea tras tener una matriz de rotación
    y un vector de traslación
    Input: R(3x3) y P(x,y,z)
    Output: T(4x4)
    """
    T = np.array([[R[0, 0], R[0, 1], R[0, 2], p[0, 0]],
                  [R[1, 0], R[1, 1], R[1, 2], p[1, 0]],
                  [R[2, 0], R[2, 1], R[2, 2], p[2, 0]],
                  [0, 0, 0, 1]])
    return T


def vect_tmatrix(T, p):
    """
    Función que retorna el vector posición de al ser rotado
    y trasladado por una matriz de trasnformación homogénea
    Input: T(4x4) y p(x,y,z) - Vector Columna
    Output: V(x,y,z) - Vector Columna
    """
    pt = np.array([[p[0, 0]],
                   [p[1, 0]],
                   [p[2, 0]],
                   [1]])
    pt = T.dot(pt)
    v = np.array([[pt[0, 0]],
                  [pt[1, 0]],
                  [pt[2, 0]]])
    return v


def trot(ang, a):
    """
    Función que retorna la matriz de transformación
    homogénea a partir de una rotación en el eje
    Input: angulo (rad) y char (x,y,z)
    Output: Matriz homogénea (4x4)
    """
    if (a == 'y'):
        T = np.array([[sp.cos(ang),  0, sp.sin(ang), 0],
                      [0,            1,           0, 0],
                      [-sp.sin(ang), 0, sp.cos(ang), 0],
                      [0,            0,           0, 1]])
    elif (a == 'z'):
        T = np.array([[sp.cos(ang), -sp.sin(ang), 0, 0],
                      [sp.sin(ang),  sp.cos(ang), 0, 0],
                      [0,                      0, 1, 0],
                      [0,                      0, 0, 1]])
    elif(a == 'x'):
        T = np.array([[1,           0,            0, 0],
                      [0, sp.cos(ang), -sp.sin(ang), 0],
                      [0, sp.sin(ang),  sp.cos(ang), 0],
                      [0,           0,            0, 1]])
    return T


def trasl(l1, l2, l3):
    """
    Función que retorna la matriz de transformación
    homogénea a partir de una traslación
    Input: 3 inputs de formato número (x,y,z)
    Output: Matriz homogénea (4x4)
    """
    T = np.array([[1, 0, 0, l1],
                  [0, 1, 0, l2],
                  [0, 0, 1, l3],
                  [0, 0, 0, 1]])
    return T

# Funciones Simbólicas


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
