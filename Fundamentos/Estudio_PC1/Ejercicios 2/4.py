import numpy as np
import rotaciones as r

M = np.array([[0.7905, -0.3864, 0.4752],
              [0.6046, 0.3686, -0.7061],
              [0.0977, 0.8455, 0.5250]])

q = r.quaterion(M)
print(q)
