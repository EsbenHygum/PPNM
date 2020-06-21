import numpy as np
import math
from math import *
from montecarlo import *

def bigfunc(x): return 1/(pi**3*(1-(cos(x[0])*cos(x[1])*cos(x[2]))))

def sphere(x): return x[0]**2*sin(x[1])

a = [0, 0, 0]
b = [1, pi, 2*pi]
exact = 4/3*pi

print("Testing the pseudo random Monte Carlo method")
print("\nVolume of sphere with radius = 1:")
result, err = montecarlo_sampler(sphere, a, b, 15000)
print("Result should be 4/3 pi (approximately 4.19)")
print("Result is", result, "p/m", err)

#print("\nTesting the quasi random Monte Carlo method")
#d = len(a)
#print("Volume of sphere with radius = 1:")
#result, err = quasi_mc(sphere, a, b, 15000, d, exact)
#print("Result should be 4/3 pi (approximately 4.19)")
#print("Result is", result, "p/m", err)


print("\n\nTesting convergence on error of sphere:\nSee plot")

error = []
convergence = []
iteration = []

for ii in range(10, 10000, 10): 
    result, err = montecarlo_sampler(sphere, a, b, ii)
    error.append(err)
    convergence.append(5/sqrt(ii))
    iteration.append(ii)

q_error = []
q_convergence = []
d = len(a)


for ii in range(10, 10000, 10): 
	seq = halton(2, ii)
	accumu = 0
	for jj in range(ii):
		x = 1 + seq[jj][0]*(5 - 1)
		y = 1 + seq[jj][1]*(5**2 - 1**2)
		accumu += x**2
	volume = 5 - 1
	result = volume*accumu/ii
	q_error.append(np.abs(result - 41.333333))
	q_convergence.append(22*log(ii)/(ii))
#	q_result, q_err = quasi_mc(sphere, a, b, ii, d, exact)

np.savetxt('convergence.txt', list(zip(iteration, error, convergence, q_error, q_convergence)))


