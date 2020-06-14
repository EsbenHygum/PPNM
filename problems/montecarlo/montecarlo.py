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
