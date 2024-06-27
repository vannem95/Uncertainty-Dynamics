from scipy.stats import multivariate_normal
import numpy as np
x = np.array([[1,2], [3,4]])
multivariate_normal.pdf(x, mean=[0, 1], cov=[5, 2])