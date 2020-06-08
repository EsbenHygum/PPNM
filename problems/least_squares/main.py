import numpy as np
from math import *
from vector import *
from matrix import *
from least_squares import *
from lineareq import *

data = np.loadtxt('data.txt')

x = data[:,0]
y = data[:,1]
dy = y/20

print(dy)

def const_func(x): return 1
def lin_func(x): return x

f = [const_func, lin_func]

ln_y = [math.log(y[ii]) for ii in range(len(y))]
ln_dy = [dy[ii]/y[ii] for ii in range(len(dy))]

result, cov = lsfit(x, ln_y, ln_dy, f)

print('Fitted parameters')
print(result)
print('Covariance matrix')
for i in range(cov.size1):
	for j in range(cov.size2):
		print('cov[{:1d},{:1d}] = {:.6f}'.format(i,j,cov[i,j]))
print('Half-life is: {:.1f} pm {:.1f} days'.format(np.log(2)/result[1],np.log(2)/np.power(result[1],2)*np.sqrt(cov[1,1])))
print('According to wikipedia, the half-life of Ra-224 is 3.6 days, so it is not within the uncertainty.')

n = 100
tt = [x[0]+i*x[-1]/n for i in range(n)]
y_f = [np.exp(result[0]+result[1]*tt[i]) for i in range(n)]
y_f_u = [np.exp((result[0]+np.sqrt(cov[0,0])) + (result[1]+np.sqrt(cov[1,1]))*tt[i]) for i in range(n)] 
y_f_l = [np.exp((result[0]-np.sqrt(cov[0,0])) + (result[1]-np.sqrt(cov[1,1]))*tt[i]) for i in range(n)]

np.savetxt('data_exp.txt', list(zip(tt, y_f, y_f_u, y_f_l)))


#x_range = np.linspace(0.1, 15, 1000)
#y_exp = np.zeros(len(x_range))

#for ii in range(len(y_exp)):
#    y_exp[ii] = c[0]*f[0](x_range[ii]) + c[1]*f[1](x_range[ii]) + c[2]*f[2](x_range[ii])


#print("c vector:")
#vector.printing(c)

#print("Error estimate of c:")
#vector.printing(dc)

#print("Covariance matrix:")
#matrix.printing(cov_matrix)
