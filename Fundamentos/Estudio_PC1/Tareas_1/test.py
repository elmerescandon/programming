import numpy as np                         # Ejecutar: shift+enter
# Para gráficos
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
cos = np.cos
sin = np.sin
pi = np.pi


def rotz(th):
    """
    Genera una matriz de rotación de un ángulo th alrededor del eje z
    """
    R = np.array([[cos(th), -sin(th), 0],
                  [sin(th),  cos(th), 0],
                  [0,        0, 1]])
    return R


Rb = rotz(np.deg2rad(20))
print(np.round(Rb, 2))
# Gráfica de los ejes coordenados
fig = plt.figure()
ax = plt.axes(projection='3d')

# Nombres para los ejes
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Ejes coordenados base
ax.plot([0, 1], [0, 0], [0, 0], 'r')   # [x1, x2], [y1, y2], [z1, z2]
ax.plot([0, 0], [0, 1], [0, 0], 'g')
ax.plot([0, 0], [0, 0], [0, 1], 'b')

# Ejes rotados
ax.plot([0, Rb[0, 0]], [0, Rb[1, 0]], [0, Rb[2, 0]], 'r--')   # [x1, x2], [y1, y2], [z1, z2]
ax.plot([0, Rb[0, 1]], [0, Rb[1, 1]], [0, Rb[2, 1]], 'g--')
ax.plot([0, Rb[0, 2]], [0, Rb[1, 2]], [0, Rb[2, 2]], 'b--')
plt.show()
