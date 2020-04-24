import numpy as np
import rotaciones as r

Rx = np.round(r.rot(90, 'x'), 3)
omega = np.cos(np.deg2rad(90)/2)
omega_s = np.sin(np.deg2rad(90)/2)
u = np.array([[1*omega_s], [0], [0]])
print(omega)
print(u)
