# Exercises in NumPy

import numpy as np

new1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(new1[2:6])

new2 = np.arange(0,20,2)

print(new2[4:8])

print(new1[:5])

print(new1[6:])

print(new1[:-1])

# Works correctly until here

'''
Slice syntax is i:j:k where i is the starting index (inclusive), j is the stopping index (exclusive) 
and k is the step size.

'''
