import numpy as np
import rotaciones as r

R21 = r.rot(180, 'z').dot(r.rot(-30, 'x'))
p21 = np.array([[4],
                [3],
                [4]])
print(R21)
