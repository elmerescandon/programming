from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
def gaussian(pos, mu, Sigma):
    """
    Retorna la distribución Gaussiana multivariable de pos
    """
    n = mu.shape[0]
    Sigma_det = np.linalg.det(Sigma)
    Sigma_inv = np.linalg.inv(Sigma)
    N = np.sqrt((2*np.pi)**n * Sigma_det)
    # Calcular (x-mu)T.Sigma-1.(x-mu) de forma vectorizada para todas las variables de entrada
    fac = np.einsum('...k,kl,...l->...', pos-mu, Sigma_inv, pos-mu)
    return np.exp(-fac / 2) / N

N = 40
X = np.linspace(-2, 2, N); Y = np.linspace(-2, 2, N); X, Y = np.meshgrid(X, Y)

# Vector de media
mu = np.array([0., 0.])
# Matriz de covarianza
P = np.array([[2 , 0],
              [0,  2]])

# Empaquetar X, Y en un solo arreglo tridimensional
pos = np.empty(X.shape + (2,)); pos[:,:,0] = X; pos[:,:,1] = Y
# Distribución gaussiana
Z = gaussian(pos, mu, P)

# Gráfico
fig = plt.figure()
# 3D
ax1 = fig.add_subplot(2,1,1,projection='3d')
ax1.plot_surface(X, Y, Z, rstride=3, cstride=3, linewidth=1, antialiased=True, cmap=cm.viridis)
ax1.set_xticks([]); ax1.set_yticks([]); ax1.set_zticks([])
ax1.set_xlabel(r'$x_1$'); ax1.set_ylabel(r'$x_2$'); ax1.set_zlabel(r'$z$')
# Vista en 2D
ax2 = fig.add_subplot(2,1,2,projection='3d')
ax2.contourf(X, Y, Z, zdir='z', offset=0, cmap=cm.viridis)
ax2.view_init(90, 270)
ax2.set_xticks([]); ax2.set_yticks([]); ax2.set_zticks([])
ax2.set_xlabel(r'$x_1$'); ax2.set_ylabel(r'$x_2$')
ax2.set_xlim3d([-4, 4])
ax2.set_ylim3d([-2, 2])
plt.show()
