import numpy
import sympy as sp

def sTrasl(x, y, z):
    """ Matriz de transformada homogenea de traslacion
    """
    T = sp.Matrix([[1,0,0,x],
                    [0,1,0,y],
                    [0,0,1,z],
                    [0,0,0,1]])
    return T

def sTrotx(ang):
    """ Matriz de transformada homogenea alrededor de X
    """
    Tx = sp.Matrix([[1, 0,0,0],
                    [0, sp.cos(ang),-sp.sin(ang),0],
                    [0, sp.sin(ang), sp.cos(ang),0],
                    [0, 0, 0, 1]])
    return Tx

def sTroty(ang):
    """ Matriz de transformada homogenea alrededor de Y
    """
    Ty = sp.Matrix([[sp.cos(ang),0,sp.sin(ang),0],
                    [0,1,0,0],
                    [-sp.sin(ang),0,sp.cos(ang),0],
                    [0,0,0,1]])
    return Ty

def sTrotz(ang):
    """ Matriz de transformada homogenea alrededor de Z
    """
    Tz = sp.Matrix([[sp.cos(ang),-sp.sin(ang),0,0],
                    [sp.sin(ang), sp.cos(ang),0,0],
                    [0,0,1,0],
                    [0,0,0,1]])
    return Tz
def sTdh(d, th, a, alpha):
    """ Matriz de transformación homogénea de Denavit-Hartenberg
    """
    cth = sp.cos(th); sth = sp.sin(th)
    ca = sp.cos(alpha); sa = sp.sin(alpha)
    Tdh = sp.Matrix([[cth, -ca*sth,  sa*sth, a*cth],
                     [sth,  ca*cth, -sa*cth, a*sth],
                     [0,        sa,     ca,      d],
                     [0,         0,      0,      1]])
    return Tdh
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
    q = sp.Matrix([[omega],
                  [ex],
                  [ey],
                  [ez]])
    return q


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
