import numpy as np
import math
from math import *

def montecarlo_sampler(f, a, b, N):
	V = 1.0
	for jj in range(len(a)):
		V *= b[jj] - a[jj]
	montecarlo_sum = 0.0
	montecarlo_sum2 = 0.0
	for jj in range(0, N):
		fx = f(x_sampler(a, b))
		montecarlo_sum += fx
		montecarlo_sum2 += fx*fx
	sigma = sqrt(montecarlo_sum2/N - (montecarlo_sum/N)**2)
	error = V * sigma/sqrt(N)
	return V*(montecarlo_sum/N), error

def x_sampler(a, b):
	return [a[jj] + np.random.random()*(b[jj] - a[jj]) for jj in range(len(a))]

#########

def corput(N, base):
	q = 0
	bk = 1/base
	while N > 0:
		q += (N % base)*bk
		N /= base
		bk /= base
	return q

#def halton(N, d):
#	base = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
#	maxd = len(base)
#	assert d <= maxd
#	x = []
#	for ii in range(0, d):
#		x.append(corput(N, base[ii]))
#	return x

def quasi_mc(f, a, b, N, d, exact):
	V = 1.0
	for jj in range(len(a)):
		V *= b[jj] - a[jj]
	q_montecarlo_sum = 0.0
	for jj in range(0, N):
		fxq = f(halton(jj, d))
		q_montecarlo_sum += fxq
	error = np.absolute(V*(q_montecarlo_sum/N) - exact)
	print(V*(q_montecarlo_sum/N))
	return V*(q_montecarlo_sum/N), error

def halton(dim: int, num: int):
	h = np.full(num*dim, np.nan)
	p = np.full(num, np.nan)
	P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
	logn = math.log(num + 1)
	for ii in range(dim):
		b = P[ii]
		n = int(math.ceil(logn / math.log(b)))
		for t in range(n):
			p[t] = pow(b, -(t+1))
		for jj in range(num):
			d = jj + 1
			sum_ = math.fmod(d, b) * p[0]
			for t in range(1, n):
				d = math.floor(d / b)
				sum_ += math.fmod(d, b) * p[t]
			h[jj * dim + ii] = sum_
	return h.reshape(num, dim)







