import numpy as np
from scipy.integrate import quad
import math

def linear_interp(x: list, y: list, u: float):
	n = len(x)
	assert n > 1 and u >= x[0] and u <= x[n-1]
	i = 0
	j = n - 1

	while j-i > 1:
		middle = int((i+j)/2)
		if u > x[middle]:
			i = middle
		else:
			j = middle
	return y[i] + (y[i + 1] - y[i])/(x[i + 1] - x[i]) * (u - x[i])

def linear_integrate(x: list, y: list, u: float):
	f_u = linear_interp(x, y, u)
	int_sum = 0
	sc_int_sum = 0
	for ii in range(len(x)):
		if u == x[0]:
			return int_sum, sc_int_sum
		elif x[ii+1] >= u:
			a = (f_u - y[ii])/(u - x[ii])
			b = y[ii] - a*x[ii]
			int_sum += a/2*(u**2-x[ii]**2) +b*(u - x[ii])
			sc_int_sum += quad(integrand, x[ii], u, args = (a, b))[0]
			return int_sum, sc_int_sum
		else:
			a = (y[ii+1] - y[ii])/(x[ii+1] - x[ii])
			b = y[ii] - a*x[ii]
			int_sum += a/2*(x[ii+1]**2 - x[ii]**2) + b*(x[ii+1]-x[ii])
			sc_int_sum += quad(integrand, x[ii], x[ii+1], args = (a, b))[0]

def integrand(x, a, b):
	return a * x +b

x = np.arange(-5, 6, 0.1)
def func_to_fit(x) : return np.sin(x)
y = [func_to_fit(xi) for xi in x]
u = np.arange(x[0], 5, 0.1)

for ii in range(len(u)):
    print(u[ii], linear_interp(x, y, u[ii]), np.interp(u[ii], x, y), linear_integrate(x, y, u[ii])[0], linear_integrate(x, y, u[ii])[1])
