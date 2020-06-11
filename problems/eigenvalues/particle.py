from __future__ import print_function
import sys
import string
from matrix import *
import numpy as np
from eigen import *
import math

n = 20
s = 1.0/(n+1)
H = matrix(n,n)
for ii in range(0, n-1):
	H[ii,ii] = -2*(-1)/s/s
	H[ii,ii+1] = 1*(-1)/s/s
	H[ii+1,ii] = 1*(-1)/s/s
H[n-1,n-1] = -2*(-1)/s/s

D, V = jacobi_cycle(H, 1e-6)
print("Testing if energies are correct")
for k in range(0,n-1):
	exact = (math.pi*(k+1))**2
	calc = D[k,k]
	print("k: {}, exact: {}, calc: {}".format(k,exact,calc))


#for j in range(0,6):
#	for i in range(0,n-1):
#		eigenf[j,i] = V[j,i]

eigen0 = matrix.get_col(V, 0)
eigen1 = matrix.get_col(V, 1)
eigen2 = matrix.get_col(V, 2)
eigen3 = matrix.get_col(V, 3)
eigen4 = matrix.get_col(V, 4)

x = np.arange(0, 20, 1)
	
np.savetxt('eigenfunc.txt', list(zip(x, eigen0, eigen1, eigen2, eigen3, eigen4)))

