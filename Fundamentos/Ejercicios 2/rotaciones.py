import numpy as np

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
    su = np.array([[0, -u[2], u[1]],
                   [u[2], 0, -u[0]],
                   [-u[1], u[0], 0]])
    return su


def rodr(th, u):
    s = skew(u)
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
