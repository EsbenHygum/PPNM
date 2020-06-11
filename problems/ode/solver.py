import numpy as np
from math import *

def rungekutta34(t: float, yt, h: float, f):
	k0 = f(t, yt)
	k1 = f(t + 0.5*h, yt + 0.5*h*k0)
	k2 = f(t + 0.5*h, yt + 0.5*h*k1)
	k3 = f(t + h, yt + h*k2)
	k_up = 1/6*k0 + 1/3*k1 + 1/3*k2 + 1/6*k3
	k_low = 1/6*k0 + 4/6*k1 + 1/6*f(t + h, yt + h + k0)
	yt_h = yt + h*k_up
	yt_h_error = (k_up - k_low)*h
	err = np.linalg.norm(yt_h_error)
	return yt_h, err

def driver(f, stepper, t, b: float, h: float, y, acc: float, prec: float):
	a = t[-1]
	t0 = t[-1]
	ts = []
	ys = []
	errors = []
	while b - t0 > prec:
		if t0 >= b: break
		if t0 + h > b:
			h = b - t0
		yt, err = stepper(t0, y, h, f)
		tolerance = (acc + np.linalg.norm(y)*prec)*np.sqrt(h/(b - a))
		if err < tolerance:
			t0 = t0 + h
			y = yt
			ts.append(t0)
			ys.append(y)
			errors.append(err)
		if err == 0:
			h *= 2
		else:
			h *= ((tolerance/err)**0.25)*0.95
#	print(ys)
	return y, np.array([ts, ys, errors])
