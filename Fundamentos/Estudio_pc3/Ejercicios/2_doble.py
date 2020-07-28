# -*- coding: utf-8 -*-

import Tkinter
import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1,1,1,1,0,0,0,0],
			  [3,2,1,0,0,0,0,0],
			  [6,2,0,0,0,0,0,0],
			  [0,0,0,0,216,36,6,1],
			  [0,0,0,0,108,12,1,0],
			  [0,0,0,0,36,12,0,0],
			  [-27,-9,-3,-1,27,9,3,1],
			  [-27,-6,-1,0,27,6,1,0]])

s = np.array([[0.2],[0],[0],[0.8],[0],[0],[0],[0]])

coeffs = np.linalg.inv(A).dot(s)
print(coeffs)