import numpy as np
from vector import *
from matrix import *
from minimize import *
from findroot import *

calls = 0

def rosen(p):
    global calls
    calls += 1
    x = p[0]
    y = p[1]
    z = vector(1)
    z[0] = (1-x)**2 + 100*(y-x*x)**2
    return z

def df_rosen(p):
    global calls
    calls += 1
    x = p[0]
    y = p[1]
    z = vector(2)
    z[0] = -2*(1-x)-400*x*(y-x*x)
    z[1] = 200*(y-x*x)
    return z

def dfH_rosen(p):
    global calls
    calls += 1
    x = p[0]
    y = p[1]
    H = matrix(2,2)
    H[0,0] = 2-400*y+1200*x*x
    H[1,0] = -400*x
    H[0,1] = -400*x
    H[1,1] = 200
    return H

def himmelblau(p):
    global calls
    calls += 1
    x = p[0]
    y = p[1]
    z = vector(1)
    z[0] = (x*x+y-11)**2 + (x+y*y-7)**2
    return z

def df_himmelblau(p):
    global calls
    calls += 1
    x = p[0]
    y = p[1]
    z = vector(2)
    z[0] = 4*x*(x*x+y-11) + 2*(x+y*y-7)
    z[1] = 2*(x*x+y-11) + 4*y*(x+y*y-7)
    return z

def dfH_himmelblau(p):
    global calls
    calls += 1
    x = p[0]
    y = p[1]
    H = matrix(2,2)
    H[0,0] = 12*x*x + 4*y - 42
    H[0,1] = 4*x + 4*y
    H[1,0] = 4*x + 4*y
    H[1,1] = 4*x + 12*y*y - 26
    return H

x0 = vector(2)
x0[0] = 2
x0[1] = 1


print("Running minimization method on Rosenbrock's function:")
x = quasi_newton(rosen, df_rosen, x0, 1e-6)
print("Quasi Newton analytical method yields a minimum at [%.2f; %.2f] with %d steps" %(x[0], x[1], calls))

calls = 0
print("\n\nRunning minimization method on Himmelblau's function:")
x = quasi_newton(himmelblau, df_himmelblau, x0, 1e-6)
print("Quasi Newton analytical method yields a minimum at [%.2f; %.2f] with %d steps" %(x[0], x[1], calls))

