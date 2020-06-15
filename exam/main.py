import numpy as np
from math import *
from montecarlo import *

def bigfunc(x): return 1/(pi**3*(1-(cos(x[0])*cos(x[1])*cos(x[2]))))

def sphere(x): return x[0]**2*sin(x[1])

a = [0, 0, 0]
b = [1, pi, 2*pi]

print("Testing the pseudo random Monte Carlo method")
print("\nVolume of sphere with radius = 1:")
result, err = montecarlo_sampler(sphere, a, b, 15000)
print("Result should be 4/3 pi (approximately 4.19)")
print("Result is", result, "p/m", err)

print("\nTesting the quasi random Monte Carlo method")
d = len(a)
print("Volume of sphere with radius = 1:")
result, err = quasi_mc(sphere, a, b, 15000, d)
print("Result should be 4/3 pi (approximately 4.19)")
print("Result is", result, "p/m", err)

print("\n\nTesting convergence on error of sphere:\nSee plot\nThe expected result has been multiplied by a factor of 5")

error = []
convergence = []
iteration = []

for ii in range(10, 1000, 10): 
    result, err = montecarlo_sampler(sphere, a, b, ii)
    error.append(err)
    convergence.append(5/sqrt(ii))
    iteration.append(ii)

q_error = []
q_convergence = []
d = len(a)

for ii in range(10, 1000, 10): 
    q_result, q_err = quasi_mc(sphere, a, b, ii, d)
    q_error.append(q_err)
    q_convergence.append(log(ii)/(ii))


np.savetxt('convergence.txt', list(zip(iteration, error, convergence, q_error, q_convergence)))


