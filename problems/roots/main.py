import numpy as np
from matrix import *
from vector import *
from findroot import *
from math import *

def rosen(p, arrays = False):
    x = p[0]
    y = p[1]
    z = vector(2)
    z[0] = -2*(1-x)-400*x*(y-x*x)
    z[1] = 200*(y-x*x)
    if arrays:
        return np.array([z[0], z[1]])
    else:
        return z

def df_rosen(p):
    x = p[0]
    y = p[1]
    J = matrix(2,2)
    J[0,0] = 2-400*y+1200*x*x
    J[1,0] = -400*x
    J[0,1] = -400*x
    J[1,1] = 200
    return J

x0 = vector(2)
x0[0] = 2
x0[1] = 1
x0_list = [2,1]

print("\nTesting solutions to Rosenbrock's valley function:")
deltax = rootfind_analytic(rosen, x0, df_rosen, 1e-6)
print("The analytic function yields a minimum at [%.2f; %.2f]" %(deltax[0], deltax[1]))
deltax = rootfind_numeric(rosen, x0, 1e-6, 1e-6)
print("The numeric function yields a minimum at [%.2f; %.2f]" %(deltax[0], deltax[1]))
print("The starting point was chosen as [%.2f; %.2f]" %(x0[0], x0[1]))

