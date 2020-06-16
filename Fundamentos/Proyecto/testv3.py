from utils import *
import numpy as np
import sympy as sp
from sympy.matrices import Matrix

q11, q12, q13 = sp.symbols("q11 q12 q13")
q21, q22, q23 = sp.symbols("q21 q22 q23")
q31, q32, q33 = sp.symbols("q31 q32 q33")
q41, q42, q43 = sp.symbols("q41 q42 q43")

l1, l2, l3, l4 = sp.symbols("l1 l2 l3 l4")
d1 = sp.symbols("d1")

# Matrices de transformación homogénea i con respecto a i-1
# Pata 1
T1_01 = sTdh(l1, q11, 0, sp.pi/2)
T1_12 = sTdh(l2, q12, -l3, 0)
T1_23 = sTdh(0, q13, -l4, 0)

# Pata 2
T2_01 = sTdh(l1, sp.pi+q21, 0, sp.pi/2)
T2_12 = sTdh(l2, q22, l3, 0)
T2_23 = sTdh(0, q23, l4, 0)

# Pata 3
T3_01 = sTdh(l1, sp.pi+q31, 0, sp.pi/2)
T3_12 = sTdh(l2, q32, l3, 0)
T3_23 = sTdh(0, q33, l4, 0)

# Pata 4
T4_01 = sTdh(l1, q41, 0, sp.pi/2)
T4_12 = sTdh(l2, q42, -l3, 0)
T4_23 = sTdh(0, q43, -l4, 0)

# Patas Respecto a la base

# Pata 1
T1_03 = sp.simplify(T1_01*T1_12*T1_23)
T1_B0 = sTroty(-sp.pi/2)*sTrotx(sp.pi)*sTrasl(0,-d1,0)
T1_B3 = sp.simplify(T1_B0*T1_03)

# Pata 2
T2_03 = sp.simplify(T2_01*T2_12*T2_23)
T2_B0 = sTroty(-sp.pi/2)*sTrasl(0,d1,0)
T2_B3 = sp.simplify(T2_B0*T2_03)

# Pata 3
T3_03 = sp.simplify(T2_01*T3_12*T3_23)
T3_B0 = sTroty(-sp.pi/2)*sTrotx(sp.pi)*sTrasl(0,d1,0)
T3_B3 = sp.simplify(T3_B0*T3_03)

# Pata 4
T4_03 = sp.simplify(T4_01*T4_12*T4_23)
T4_B0 = sTroty(-sp.pi/2)*sTrasl(0,-d1,0)
T4_B3 = sp.simplify(T4_B0*T4_03)
#Parametros de Denavit-Hartenberg
#Pata 1
DH1 = [[l1,   q11, 0, sp.pi/2,'r'],
    [ l2, q12,  -l3,       0,'r'],
    [  0,q13, -l4, 0,'r']]

#Pata 2
DH2 = [[l1, sp.pi+q21, 0, sp.pi/2,'r'],
      [ l2, q22,  l3,       0,'r'],
      [ 0,q23, l4, 0,'r']]

#Pata 3
DH3 = [[l1, sp.pi+q31, 0, sp.pi/2,'r'],
      [ l2, q32,  l3,       0,'r'],
      [ 0,q33, l4, 0,'r']]

#Pata 4
DH4 = [[l1,   q41, 0, sp.pi/2,'r'],
      [ l2, q42,  -l3,       0,'r'],
      [  0,q43, -l4, 0,'r']]

#Jacobianos Geometricos
[T1,JG1] = jacob_g(DH1)
[T2,JG2] = jacob_g(DH2)
[T3,JG3] = jacob_g(DH3)
[T4,JG4] = jacob_g(DH4)

#Jacobiano geometrico (respecto a la base)

#Pata 1
RB_10 = T1_B0[0:3,0:3]
XB_10 = sp.Matrix.vstack(sp.Matrix.hstack(RB_10,sp.zeros(3,3)),sp.Matrix.hstack(sp.zeros(3,3),RB_10))
JB_1 = XB_10*JG1


#Pata 2
RB_20 = T2_B0[0:3,0:3]
XB_20 = sp.Matrix.vstack(sp.Matrix.hstack(RB_20,sp.zeros(3,3)),sp.Matrix.hstack(sp.zeros(3,3),RB_20))
JB_2 = XB_20*JG2a

#Pata 3
RB_30 = T3_B0[0:3,0:3]
XB_30 = sp.Matrix.vstack(sp.Matrix.hstack(RB_30,sp.zeros(3,3)),sp.Matrix.hstack(sp.zeros(3,3),RB_30))
JB_3 = XB_30*JG3

#Pata 4
RB_40 = T4_B0[0:3,0:3]
XB_40 = sp.Matrix.vstack(sp.Matrix.hstack(RB_40,sp.zeros(3,3)),sp.Matrix.hstack(sp.zeros(3,3),RB_40))
JB_4 = XB_40*JG4


# Cinemática diferencial de base flotante
pb_x,pb_y,pb_z,wb,eb_x,eb_y,eb_z = sp.symbols(r'p_{bx} p_{by} p_{bz} \omega_{b} \epsilon_{bx} \epsilon_{by} \epsilon_{bz}')
TT_IB = sTrasl(pb_x,pb_y,pb_z) # Traslación del sistema inercial al base (Transformación)
quater_B = Matrix([[wb],[eb_x],[eb_y],[eb_z]])
R_IB = symrquater(quater_B) # Rotación del sistema inercial al base (Transformación)
TR_IB = symtransmaxtrix(R_IB) # Rotación del sistema inercial al base
T_IB = TT_IB*TR_IB # Transformada homogénea de la base con respecto al sistema inercial
TQ = 2*Matrix([[-eb_x,wb,-eb_z,eb_y],
               [-eb_y,eb_z,wb,-eb_x],
               [-eb_z,-eb_y,eb_x,wb]])


# Actualización de sistemas de referncia con respecto a la base
T1_I3 = T_IB*T1_B3
T2_I3 = T_IB*T2_B3
T3_I3 = T_IB*T3_B3
T4_I3 = T_IB*T4_B3

sk_d = symskew(T_IB[0:3,3]-T1_I3[0:3,3]) # Skew Matrix de la diferencia de pb - pi
vel_jb = sk_d*TQ
eye = Matrix([[1,0,0],
              [0,1,0],
              [0,0,1]])
zeros = Matrix([[0,0,0],
                [0,0,0],
                [0,0,0]])
Jb_base = Matrix([[eye,vel_jb],
             [zeros,TQ]])

Jg_1 = Matrix.vstack(R_IB*JB_1[0:3,0:3],R_IB*JB_1[3:6,0:3])
Jg_1 = Matrix.hstack(Jb_base,Jg_1)
print(sp.simplify(Jg_1))
