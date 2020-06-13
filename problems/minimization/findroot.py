import numpy as np
from vector import *
from matrix import *
from qr_decomp import *

def rootfind_analytic(f, x0: vector, jacobian, eps: float):
	x = vector.copy(x0)
	neg_fx = vector(x.size)
	fx = f(x)
	while vector.norm(fx) > eps:
		J = jacobian(x)
		for jj in range(neg_fx.size):
			neg_fx[jj] = -1*fx[jj]
		deltax = qr_gs_solve(J, neg_fx)
		lambd = 2
		while True:
			lambd /= 2
			for ii in range(x.size):
				x[ii] = x[ii] + lambd*deltax[ii]
			fx2 = f(x)
			if vector.norm(fx2) < (1 - lambd/2)*vector.norm(fx) or lambd < 0.02: break
		fx = fx2
	return x

def rootfind_numeric(f, x0: vector, eps: float, dx: float):
	x = vector.copy(x0)
	df = vector(x.size)
	J = matrix(x.size, x.size)
	neg_fx = vector(x.size)
	fx = f(x)
	while vector.norm(fx) > eps:
		fx = f(x)
		for jj in range(x.size):
			x[jj] += dx
			for ii in range(df.size):
				df[ii] = f(x)[ii] - fx[ii]
				J[ii, jj] = df[ii]/dx
			x[jj] -= dx
		for ll in range(neg_fx.size):
			neg_fx[ll] = -1*fx[ll]
		deltax = qr_gs_solve(J, neg_fx)
		lambd = 2
		while True:
			lambd /= 2
			for jj in range(x.size):
				x[jj] = x[jj] + lambd*deltax[jj]
			fx2 = f(x)
			if vector.norm(fx2) < (1-lambd/2)*vector.norm(fx) or lambd < 0.02: break
		if vector.norm(deltax) < dx: break
	return x
