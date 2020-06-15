import numpy as np
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

def halton(N, d):
	base = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
	maxd = len(base)
	assert d <= maxd
	x = []
	for ii in range(0, d):
		x.append(corput(N, base[ii]))
	return x

def quasi_random_xsampler(a, b, N, d):
	x_halton = halton(N, d)
	return [a[jj] + x_halton[jj]*(b[jj] - a[jj]) for jj in range(len(a))]

def quasi_mc(f, a, b, N, d):
	V = 1.0
	for jj in range(len(a)):
		V *= b[jj] - a[jj]
	q_montecarlo_sum = 0.0
	q_montecarlo_sum2 = 0.0
	montecarlo_sum = 0.0
	montecarlo_sum2 = 0.0
	for jj in range(0, N):
		fxq = f(quasi_random_xsampler(a, b, N, d))
		q_montecarlo_sum += fxq
		q_montecarlo_sum2 += fxq*fxq
		fx = f(x_sampler(a, b))
		montecarlo_sum += fx
		montecarlo_sum2 += fx*fx
	error = np.abs(V*(montecarlo_sum/N) - V*(q_montecarlo_sum/N))
	return V*(q_montecarlo_sum/N), error


