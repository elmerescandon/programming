import numpy as np
import rotaciones as r

R1 = r.rot(90, 'x')
R2 = r.rot(30, 'z')
R3 = r.rot(50, 'y')

R = R1.dot(R2).dot(R3)

p = np.array([[3], [5], [1]])
pf = R.T.dot(p)
print(pf)

pn = R.dot(pf)
print(pn)
