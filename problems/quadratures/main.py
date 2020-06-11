import numpy as n
from math import *
from integrater import *
from scipy import integrate

call = 0 

def sqrtfunc(x: float):
	global call
	call += 1
	return sqrt(x)

def invsqrt(x: float):
	global call
	call += 1
	return 1./sqrt(x)

def logsqrt(x: float):
	global call
	call += 1
	return log(x)/sqrt(x)

def pi_int(x: float):
	global call
	call += 1
	return 4*sqrt(1-x**2)

a = 0.
b = 1.
acc = 1e-7
eps = 1e-7

result = integrator(sqrtfunc, a, b, acc, eps)
print("Integrating sqrt(x)", "\nResult should be 2/3\nResult is", result, "\nCalls:", call)

call = 0
result = clen_curt(sqrtfunc, a, b, acc, eps)
print("\nIntegrating sqrt(x) using Clenshaw-Curtis:","\nResult should be 2/3\nResult is", result,"\nCalls:", call)

call = 0
result = integrate.quad(sqrtfunc, a, b, epsabs = acc, epsrel = eps)[0]
print("\nIntegrating sqrt(x) using SciPy:","\nResult should be 2/3\nResult is", result, "\nCalls:", call)

call = 0
result = integrator(pi_int, a, b, acc, eps)
print("\nIntegrating 4*sqrt(1-x**2)", "\nResult should be pi\nResult is", result, "\nCalls:", call)

call = 0
result = clen_curt(pi_int, a, b, acc, eps)
print("\nIntegrating 4*sqrt(1-x**2) using Clenshaw-Curtis:","\nResult should be pi\nResult is", result,"\nCalls:", call)

call = 0
result = integrate.quad(pi_int, a, b, epsabs = acc, epsrel = eps)[0]
print("\nIntegrating 4*sqrt(1-x**2) using SciPy:","\nResult should be pi\nResult is", result, "\nCalls:", call)


