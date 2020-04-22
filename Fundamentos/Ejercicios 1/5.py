import sympy as sp
from sympy.matrices import Matrix
import numpy as np

p, s, a = sp.symbols("p s a")
M = Matrix([[0.3536,  -0.6124,         a],
            [p,   0.1268,   -0.3536],
            [0.1268,        s,    0.6124]])

N = M*M.T
print(N)
