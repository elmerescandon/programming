from funciones import *
import sympy as sp
from sympy.matrices import Matrix

sin = sp.sin
cos = sp.cos

q1,q2,l1,d2,Izz1,Izz2,m1,m2 = sp.symbols(r'q_1 q_2 l_1 d_2 I_{zz_1} I_{zz_2} m_1 m_2')
qd1,qd2,g,m1,m2 = sp.symbols(r'\dot{q_1} \dot{q_2} g m_1 m_2')
pc1 = sp.Matrix([[(l1/2)*cos(q1)],
                 [(l1/2)*sin(q1)],
                 [0]])
pc2 = sp.Matrix([[(l1)*cos(q1)],
                 [(l1)*sin(q1)],
                 [d2]])
I1 = sp.Matrix([[0,0,0],
                [0,0,0],
                [0,0,Izz1]])
I2 = sp.Matrix([[0,0,0],
                [0,0,0],
                [0,0,Izz2]])
R1 =  sp.Matrix([[cos(q1),-sin(q1),0],
                 [sin(q1),cos(q1),0],
                 [0,0,1]])
R2 =  sp.Matrix([[1,0,0],
                 [0,1,0],
                 [0,0,1]])
z = [R1[0:3,2],R2[0:3,2]]
tipos_z= ['r','p']
cp = [pc1,pc2]
qs = [q1,q2]
Jv = linear_velocity_CoM(cp,qs,z,tipos_z)
Jw = angular_velocity_CoM(cp,z,tipos_z)
R = [R1,R2]
m = [m1,m2]
I = [I1,I2]
q_dots = [qd1,qd2]
g_vec = sp.Matrix([[0],[-g],[0]])

matrix_m = Mass_Matrix(Jv,Jw,R,m,I)
matrix_c = Coriolis_Matrix(matrix_m,q_dots,qs)
vector_g = GravitationalForce_vector(Jv,m,g_vec)
display(matrix_m)
display(matrix_c)
display(vector_g)
