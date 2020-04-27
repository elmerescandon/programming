import numpy as np
import rotaciones as r


# Parte A
R2 = r.rodr(30, np.array([[1], [1], [1]]))
R = r.rot(90, 'x').dot(R2).dot(r.rot(50, 'y'))


# Parte B
q = r.quaterion(R)
RP = r.rquater(q)

# Parte C
p = np.array([[3], [5], [1]])
pb = R.dot(p)
print(np.round(pb, 2))

pq = r.vecquater(p, q)
print(np.round(pq, 2))
