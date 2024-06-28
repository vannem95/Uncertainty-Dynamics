from scipy.stats import multivariate_normal
import numpy as np
import math

x = 0.1
x2 = multivariate_normal.pdf(x, mean=[0], cov=[1])

print(x2)

# test gaussian
mu = 0
sig = 1
x3 = (1/(sig*(2*np.pi)**0.5))*math.exp(-0.5* ((x - mu)/(sig))**2 )
print(x3)