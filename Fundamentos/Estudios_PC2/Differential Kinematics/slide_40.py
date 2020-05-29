import sympy as sp
from sympy.matrices import Matrix
import numpy as np
import rotaciones as r

l1, l2, q1, q2 = sp.symbols(r'l_1 l_2 q_1 q_2')

x = l1*sp.cos(q1) + l2*sp.cos(q1+q2)
y = l1*sp.sin(q1) + l2*sp.sin(q1+q2)
theta = q1+q2

Jxq1 = sp.diff(x, q1)
Jxq2 = sp.diff(x, q2)
Jyq1 = sp.diff(y, q1)
Jyq2 = sp.diff(y, q2)
Jtq1 = sp.diff(theta, q1)
Jtq2 = sp.diff(theta, q2)

J = Matrix([[Jxq1, Jxq2],
            [Jyq1, Jyq2],
            [Jtq1, Jtq2]])
J
