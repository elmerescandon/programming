import numpy as np
import rotaciones as r

Rfa = np.array([[0, 0.866, -0.5],
                [-1, 0, 0],
                [0, 0.5, 0.866]])
Rx = r.rot(-90, 'x')
Ry = r.rot(90, 'y')

Rz = (Rx.T.dot(Rfa)).dot(Ry.T)
print(Rz)

# Comprobacion
Rcom = Rx.dot(Rz).dot(Ry)
print(np.round(Rcom, 4))
