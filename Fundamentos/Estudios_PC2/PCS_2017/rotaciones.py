import numpy as np
import sympy as sp
from sympy.matrices import Matrix

# Raúl Escandón - Fundamentos de Robótica 2020-1
# Funciones para representación de Cuerpos Rígidos
# Funciones para desarrollo de cinematica directa,
# inversa numerica y diferencial

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


def simquaterion(R):
    """
    Funcion que retorna el vector de quaterion unitario
    a partir de una matriz de rotacion.
    No considera la forma adicional de operar cuando el angulo es 180
    Lo de vuelve de la forma:
    q = (w,ex,ey,ez)
    """
    omega,ex,ey,ez = sp.symbols(r'\omega e_x e_y e_z')
    omega = (1/2)*(sp.sqrt(1+R[0, 0]+R[1, 1]+R[2, 2]))
    ex = (1/(4*omega))*(R[2, 1]-R[1, 2])
    ey = (1/(4*omega))*(R[0, 2]-R[2, 0])
    ez = (1/(4*omega))*(R[1, 0]-R[0, 1])
    q = Matrix([[omega],
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


def srot(th, a):
    '''
        Función simbólica que genera una matriz de rotación
        para el eje deseado
        Inputs: theta (símbolo) , a (caracter de eje)
        Output: Matriz simbólica de Rotación
    '''
    if (a == 'x'):
        R = Matrix([[1,       0,        0],
                    [0, sp.cos(th), -sp.sin(th)],
                    [0, sp.sin(th),  sp.cos(th)]])
    elif (a == 'y'):
        R = Matrix([[sp.cos(th),      0, sp.sin(th)],
                    [0,      1,      0],
                    [-sp.sin(th),     0, sp.cos(th)]])
    elif (a == 'z'):
        R = Matrix([[sp.cos(th), -sp.sin(th), 0],
                    [sp.sin(th), sp.cos(th), 0],
                    [0,      0,    1]])
    return R


def jacob_g(DH):
    '''
    Función simbólica que realiza el Jacobiano geométrico dado los parámetros
    Denavit-Hatenberg. Retorna una lista que contiene las matrices de
    transformación y la matríz del jacobiano Geométrico
    DH de la forma(d, theta, a, alpha,'p/r'prismatico/rotacional)
    '''
    T_ref = []  # Matriz que almacena los valores de T
    T = Matrix([[1, 0, 0, 0],  # Inicializar Matriz de trasnformacion
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])
    z0 = Matrix([[0], [0], [1]])
    p0 = Matrix([[0], [0], [0]])
    J = Matrix([])
    for i in range(len(DH)):
        Ti = sp.simplify(sdh(DH[i][0], DH[i][1], DH[i][2], DH[i][3]))
        T = T*Ti
        T_ref.append(T)

    for n in range(len(DH)):
        if (n == 0):
            z = z0
            p = p0
        else:
            z = T_ref[n-1][0:3, 2]
            p = T_ref[n-1][0:3, 3]

        if (DH[i][4] == 'r'):
            Jv = crossproduct(z, T_ref[len(DH)-1][0:3, 3] - p)
            if n == 2:
                print(z)
                print(p)
                print(T_ref[len(DH)-1][0:3, 3])
            Jw = z

        elif (DH[i][4] == 'p'):
            Jv = z
            Jw = 0
        J1 = sp.Matrix.vstack(Jv, Jw)
        J = sp.Matrix.hstack(J, J1)
    return T_ref, sp.simplify(J)
