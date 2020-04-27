import numpy as np
import rotaciones as r

p = np.array([[3],
              [5],
              [2]])
th = np.deg2rad(60)
u = np.array([[2],
              [0],
              [0]])
R = r.rodr(th, u)
pp2 = R.dot(p)
q = r.quaterion(R)
print(q)

print(pp2)
pp = r.vecquater(p, q)
print(pp)
