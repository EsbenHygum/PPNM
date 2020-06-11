import numpy as np
from solver import *
import json

N = 5.8e6
infectFactor = 2
Tr = 14 #Recovery time
Tc = Tr/infectFactor #Typical time between contacts
#y[0] is susceptible
#y[1] is infect
#y[2] is removed
def sir_model(t, y):
	dydt = [0, 0, 0]
	dydt[0] = -y[1]*y[0]/(N*Tc)
	dydt[1] = y[1]*y[0]/(N*Tc) - y[1]/Tr
	dydt[2] = y[1]/Tr
	return np.array(dydt)
a = 0
b = 200
h = 1
y1 = 200 #start number of infected
y0 = N - y1 #start number of susceptible
y2 = 0 #Start number of removed
t = np.array([a])
y = np.array([y0, y1, y2])

y_res, points = driver(sir_model, rungekutta34, t, b, h, y, 1e-3, 1e-3)

ts = points[0,:]
ys = points[1,:]
err = points[2,:]
S = []
I = []
R = []
for ll in range(len(ys)):
	S.append(ys[ll][0])
	I.append(ys[ll][1])
	R.append(ys[ll][2])

np.savetxt("sir_model2.txt", list(zip(ts, S, I, R)))

