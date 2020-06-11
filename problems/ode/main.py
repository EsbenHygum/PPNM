import numpy as np
from solver import *

def orbit(t, y):
	dydt = [0, 0]
	dydt[0] = y[1]
	ecc = 0.05
	dydt[1] = 1 - y[0] + ecc*y[0]*y[0]
	return np.array(dydt)

a = 0
b = 50
y0 = 1
y1 = -0.5
t = np.array([a])
y = np.array([y0, y1])
h = 0.1

y_res, points = driver(orbit, rungekutta34, t, b, h, y, 1e-2, 1e-2)

ts = points[0,:]
ys = points[1,:]
errs = points[2,:]
y = []
for ll in range(len(ys)):
	y.append(ys[ll][0])

np.savetxt("orbit.dat", list(zip(ts, y, errs)))

