import numpy as np
from matrix import *
from vector import *
from qr_decomp import *

def quasi_newton(f, df, x0, eps, alpha = 1e-4, dx = 1e-6):
	n = x0.size
	x = vector.copy(x0)
	xnew = vector(n)
	c = vector(n)
	y = vector(n)
	s = vector(n)
	u = vector(n)
	step = vector(n)
	neg_g_phi = vector(n)
	B = matrix(n, n)
	dB = mt_copy(B)
	for ll in range(B.size1):
		B[ll, ll] = 1
	grad = df(x)
	fx = f(x)
	while vector.norm(grad) > eps:
		for jj in range(neg_g_phi.size):
			neg_g_phi[jj] = (-1)*grad[jj]
		deltax = mt_vt_mult(B, neg_g_phi)
		for ii in range(s.size):
			s[ii] = 2*deltax[ii]
		while True:
			for jj in range(s.size):
				s[jj] /= 2
			for jj in range(xnew.size):
				xnew[jj] = x[jj] + s[jj]
			fxnew = f(xnew)
			if abs((fxnew)[0]) < abs(fx[0])+0.01*vector.dot_prod(s, grad): break
			if vector.norm(s) < dx:
				for ii in range(B.size1):
					for jj in range(B.size2):
						if ii == jj:
							B[ii, jj] = 1
						else:
							B[ii, jj] = 0
				break
		for jj in range(y.size):
			y[jj] = df(xnew)[jj] - grad[jj]
		for jj in range(u.size):
			u[jj] = s[jj] - mt_vt_mult(B, y)[jj]
		for jj in range(B.size1):
			for ii in range(B.size2):
				B[jj, ii] += outer(u, s)[jj, ii] / vector.dot_prod(y, s)
		for jj in range(xnew.size):
			x[jj] = xnew[jj]
		grad = df(x)
		fx = f(x)
	return x

