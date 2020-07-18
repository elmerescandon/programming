# Examen Final 2019-1
# Fundamentos de Robótica
# ==================================
# %%Inicializar librerías
import symbolic as sym
import sympy as sp
from sympy.matrices import Matrix
sp.init_printing()

# %%Pregunta 1 : Hallar la matriz de masa

# Símbolos
d1,q1,q2,d2,L2,q3 = sp.symbols(r'd_1 q_1 q_2 d_2 L_2 q_3')

# Inicializar las matrices obtenidas
art = ['p','r','p']  # Tipo de articulación
# Centros de masa de los eslabones
Cp_1 = Matrix([[0],[q1],[0]])
Cp_2 = Matrix([[sp.cos(q2)*d2],[d1 + q1 + sp.sin(q2)*d2],[0]])
Cp_3 = Matrix([[sp.cos(q2)*L2],[d1 + q1 + sp.sin(q2)*L2 + sp.sin(q2+sp.pi/2)*q3],[0]])
# Matrices de inercial con respecto al sistema del CoM
Ixx1,Ixy1,Ixz1,Iyx1,Iyy1,Iyz1,Izx1,Izy1,Izz1 = sp.symbols(r'I_{xx_1} I_{xy_1} I_{xz_1} I_{yx_1} I_{yy_1} I_{yz_1} I_{zx_1} I_{zy_1} I_{zz_1}')
I1 = Matrix([[Ixx1,Ixy1,Ixz1],
             [Iyx1,Iyy1,Iyz1],
             [Izx1,Izy1,Izz1]])

Ixx2,Ixy2,Ixz2,Iyx2,Iyy2,Iyz2,Izx2,Izy2,Izz2 = sp.symbols(r'I_{xx_2} I_{xy_2} I_{xz_2} I_{yx_2} I_{yy_2} I_{yz_2} I_{zx_2} I_{zy_2} I_{zz_2}')
I2 = Matrix([[Ixx2,Ixy2,Ixz2],
             [Iyx2,Iyy2,Iyz2],
             [Izx2,Izy2,Izz2]])

Ixx3,Ixy3,Ixz3,Iyx3,Iyy3,Iyz3,Izx3,Izy3,Izz3 = sp.symbols(r'I_{xx_3} I_{xy_3} I_{xz_3} I_{yx_3} I_{yy_3} I_{yz_3} I_{zx_3} I_{zy_3} I_{zz_3}')
I3 = Matrix([[Ixx3,Ixy3,Ixz3],
             [Iyx3,Iyy3,Iyz3],
             [Izx3,Izy3,Izz3]])

# Paso 1: Obtener las velocidades lineales de los centros de masa
cp = [Cp_1,Cp_2,Cp_3]
qs = [q1,q2,q3]
z_0 = Matrix([[0],[0],[1]])
z_1 = Matrix([[0],[0],[1]])
z_2 = Matrix([[0],[0],[1]])
z = [z_0,z_1,z_2]
Jv = sym.linear_velocity_CoM(cp,qs,z,art)

# %%Paso 2: Obtener las velocidad angulares de los centros de masa
Jw = sym.angular_velocity_CoM(cp,z,art)

# Paso 3: Obtener la matriz de masa
m1,m2,m3 = sp.symbols(r'm_1 m_2 m_3')
m = [m1,m2,m3]
I = [I1,I2,I3]
R_0 = Matrix([[1,0,0],
              [0,1,0],
              [0,0,1]])
R_1 = sym.srot(q2,'z')
R_2 = sym.srot(q2,'z')
R = [R_0,R_1,R_2]
# display(Jw)
# display(Jv)
M = sym.Mass_Matrix(Jv,Jw,R,m,I)
display(M)


# %% Pregunta 2: Obtener la matriz de Coriolis
a1,a2,a3,q1,q2,q1_dot,q2_dot = sp.symbols(r'a_1 a_2 a_3 q_1 q_2 \dot{q_1} \dot{q_2}')
mass = Matrix([[a1,a2*sp.sin(q2)],
               [a2*sp.sin(q2),a3]])
q_dots = [q1_dot,q2_dot]
qs = [q1,q2]

C = sym.Coriolis_Matrix(mass, q_dots, qs)
display(C)
