#!/usr/bin/python

import numpy as np

def bernoulli(p):
	num =  np.random.rand()
	print(num)
	if (num < p):
		return 1
	else:
		return 0
