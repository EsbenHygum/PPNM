from __future__ import print_function
import sys
import string
from matrix import *
import numpy as np
from eigen import *
import math

if len(sys.argv)>1 : 
    n = int(sys.argv[1])

else:
    n = 4


print("Testing cyclic eigenvalue decomposition")

A = matrix(n, n)


for ii in range(0, n):
    A[ii,ii] = np.random.random()
    for jj in range(ii, n):
         const = np.random.random()
         A[ii, jj] = const
         A[jj, ii] = const



print("Original matrix, A:")
matrix.printing(A)

D, V = jacobi_cycle(A, 1e-6)


print('V: ')
matrix.printing(V)

print("Diagonalized eigenvalue matrix, D:")
matrix.printing(D)
print("Testing V^{T}AV = D:")
matrix.printing(matrix_mult(trans(V), matrix_mult(A, V)))
#"""
#eigen_by_eigen(A, 1, 1e-6)
#"""


