from utils import *
import numpy as np
import sympy as sp
from sympy.matrices import Matrix



pb_x,pb_y,pb_z,wb,eb_x,eb_y,eb_z = sp.symbols(r'p_{bx} p_{by} p_{bz} \omega_{b} \epsilon_{bx} \epsilon_{by} \epsilon_{bz}')
TT_IB = sTrasl(pb_x,pb_y,pb_z) # Traslación del sistema inercial al base (Transformación)
quater_B = Matrix([[wb],[eb_x],[eb_y],[eb_z]])
R_IB = symrquater(quater_B) # Rotación del sistema inercial al base (Transformación)
TR_IB = symtransmaxtrix(R_IB) # Rotación del sistema inercial al base
T_IB = TT_IB*TR_IB # Transformada homogénea de la base con respecto al sistema inercial
TQ = 2*Matrix([[-eb_x,wb,-eb_z,eb_y],
               [-eb_y,eb_z,wb,-eb_x],
               [-eb_z,-eb_y,eb_x,wb]])
print(T_IB[0:3,3])
