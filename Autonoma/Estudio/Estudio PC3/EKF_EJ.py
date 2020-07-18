# %% Añadir Librerías
import numpy as np
import sympy as sp

# %% Diferenciación del modelo de medición
xt,yt,phirt,phiyt,xt_1,yt_1,phirt_1,phiyt_1,dt = sp.symbols(r'x y \phi_r \phi_y x_{t-1} y_{t-1} \phi_{r_{t-1}} \phi_{y_{t-1}} dt')
v,u_r,g = sp.symbols(r'v u_r g')
eps_x,eps_y, eps_phir,eps_phiy = sp.symbols(r'\epsilon_x \epsilon_y \epsilon_{\phi_r} \epsilon_{\phi_y}')
estado = sp.Matrix([[xt_1 + dt*v*sp.cos(phiyt_1) + eps_x],
                    [yt_1 + dt*v*sp.sin(phiyt_1) + eps_y],
                    [dt*u_r + eps_phir],
                    [dt*(-g/v)*sp.tan(phirt_1)+eps_phiy]])
display(estado)

# %% Matrix Fx
diff_var = sp.Matrix([xt_1,yt_1,phirt_1,phiyt_1])
display(estado.jacobian(diff_var))

# %% Matrix Fu
diff_var_u = sp.Matrix([v,u_r])
display(estado.jacobian(diff_var_u))

# %% Matriz Error Fe
diff_var_eps = sp.Matrix([eps_x,eps_y,eps_phir,eps_phiy])
display(estado.jacobian(diff_var_eps))


# %% Estado
x_gps, y_gps,delta_x,delta_y,delta_ang1,delta_ang2 = sp.symbols(r'x_gps y_gps \delta_x \delta_y \delta_a1 \delta_a2')
x_p1,y_p1,x_p2,y_p2 = sp.symbols(r'x_p1 y_p1 x_p2 y_p2')
z = sp.Matrix([[x_gps + delta_x +delta_x],
               [y_gps + delta_y + delta_y],
               [sp.atan2(yt-y_p1,xt-x_p1) + delta_ang1],
               [sp.atan2(yt-y_p2,xt-x_p2) + delta_ang2]])
z_diff =
