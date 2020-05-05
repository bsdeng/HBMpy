import numpy as np
import math as mt

nT = 8
nh = 1
n = 2*nh+1
pi = 3.1415922653

s = (nT, n)
Ga = np.zeros(s)

for i in range(0, nT):
    Ga[i][0] = 1
    for j in range(1, 2):
        Ga[i][2*j-1] = mt.cos(j*(i+1)*2*pi/nT)
        Ga[i][2*j] = mt.sin(j*(i+1)*2*pi/nT)

print(Ga)

s = (n, nT)
Gp = np.zeros(s)

for i in range(0, nT):
    Gp[0][i] = (1/nT)
    for j in range(1, 2):
        Gp[2*j-1][i] = (1/nT)*2*mt.cos(j*(i+1)*2*pi/nT)
        Gp[2*j][i] = (1/nT)*2*mt.sin(j*(i+1)*2*pi/nT)

print(Gp)
