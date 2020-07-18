# Cargar librerías
from functions import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Obstacles
qobst = np.array([[10., 4.],[3., 3.],[17.,16.]])
# Grid
xv = np.arange(0,20,1); yv = np.arange(0,22,1); x, y = np.meshgrid(xv, yv)
# Parameters
rho = 4
# Calculate attractive potential
Utot = np.zeros(x.shape)
ftot = np.zeros((x.shape[0], x.shape[1], 2))
for i in range(x.shape[0]):
    for j in range(x.shape[1]):
        U, f = repulsive_pots(np.array([x[i,j], y[i,j]]), qobst, rho)
        Utot[i,j] = U
        ftot[i,j,:] = f
plt.figure()
plt.imshow(Utot); plt.quiver(x, y, ftot[:,:,0], ftot[:,:,1])
# Starting point
pi = np.array([2., 18.])
traj = pi
for i in range(40):
    U, f = repulsive_pots(pi, qobst, rho)
    pi = pi + 0.5*f
    traj = np.vstack([traj, pi])
plt.axis([xv[0], xv[-1], yv[0], yv[-1]])
plt.plot(traj[:,0], traj[:,1], 'k'); plt.plot(traj[:,0], traj[:,1], 'o'); plt.plot(traj[0,0], traj[0,1], 'ro')
# Plot
plt.show()

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, Utot, cmap=cm.coolwarm, rstride=1, cstride=1,
                       linewidth=0, antialiased=False)
plt.show()