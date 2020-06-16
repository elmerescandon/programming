from sympy.utilities.lambdify import implemented_function
import numpy as np
import sympy as sp
from sympy.matrices import Matrix
from rotaciones import *

q11, q12, q13, q21, q22, q23, q31, q32, q33, q41, q42, q43, l1, l2, l3, l4, d1  = sp.symbols("q11 q12 q13 q21 q22 q23 q31 q32 q33 q41 q42 q43 l1 l2 l3 l4 d1")

# Matrices de transformación homogénea i con respecto a i-1
# Pata 1
T1_01 = sdh(l1,q11,0,sp.pi/2)
T1_12 = sdh(l2,q12,-l3,0)
T1_23 = sdh(0,q13,-l4,0)

# Pata 2
T2_01 = sdh(l1,sp.pi+q21, 0, sp.pi/2)
T2_12 = sdh(l2,q22,l3, 0)
T2_23 = sdh(0,q23,l4, 0)

# Pata 3
T3_01 = sdh(l1, sp.pi+q31, 0, sp.pi/2)
T3_12 = sdh(l2, q32, l3, 0)
T3_23 = sdh(0, q33, l4, 0)

# Pata 4
T4_01 = sdh(l1, q41, 0, sp.pi/2)
T4_12 = sdh(l2, q42, -l3, 0)
T4_23 = sdh(0, q43, -l4, 0)

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

# Derivadas

D1 =T1_B3[0:3,3]
D2 =T2_B3[0:3,3]
D3 =T3_B3[0:3,3]
D4 =T4_B3[0:3,3]

J1 = T1_B3[0:3,3].jacobian(sp.Matrix([q11, q12, q13]))
J2 = T2_B3[0:3,3].jacobian(sp.Matrix([q21, q22, q23]))
J3 = T3_B3[0:3,3].jacobian(sp.Matrix([q31, q32, q33]))
J4 = T4_B3[0:3,3].jacobian(sp.Matrix([q41, q42, q43]))


J1 = J1.subs({d1:75,l1:125, l2:25, l3:105,l4:120})
D1 = D1.subs({d1:75,l1:125, l2:25, l3:105,l4:120})
