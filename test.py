from scipy.stats import multivariate_normal
import numpy as np
import math

import matplotlib.pyplot as plt

x = np.arange(-10,10,100)

xx = multivariate_normal.pdf(x, mean=[0], cov=[1])

A = 2

B = 1

yy = A*xx + B

plt.plot(x,yy)
plt.show()
