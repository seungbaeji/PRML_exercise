# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 23:02:57 2017

@author: torsh
"""

import numpy as np

np.random.seed(0)
a = np.random.uniform(low=0, high=10, size=100)

np.random.seed(9)
b = np.random.uniform(low=0, high=10, size=100)

c = a + b
mean_sum = np.mean(a) + np.mean(b)
var_sum = np.var(a) + np.var(b)

print("Mean of the first samples: %.5f" % np.mean(a))
print("Mean of the second samples: %.5f" % np.mean(b))
print("Mean of the joint samples: %.5f" % np.mean(c))
print("Sum of the means of the first and the second samples: %.5f" % mean_sum)

print("Variance of the first samples: %.5f" % np.var(a))
print("Variance of the second samples: %.5f" % np.var(b))
print("Variance of the joint samples: %.5f" % np.var(c))
print("Sum of the variances of the first and the second samples: %.5f" % var_sum)