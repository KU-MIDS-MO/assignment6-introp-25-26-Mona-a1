# Write a function:
# `random_unit_vectors(num_vectors, dim)`
# that:
# a)creates a matrix M of shape (num_vectors, dim)using;

# M = np.random.randn(num_vectors, dim)

# b)normalizes each row so it has Euclidean norm 1,

# and c)returns the resulting matrix as a NumPy array.

import numpy as np

from numpy import array
from numpy.linalg import norm 

num_vectors = 10
dim = 2


def random_unit_vectors(num_vectors, dim):

    M = np.random.randn(num_vectors, dim) 
    print(M)

    
    all_l2_norm_result = []
    for i in range(0, num_vectors):    
        l2_norm_result = M[i,:] /np.linalg.norm(M[i, :], ord=2)
        all_l2_norm_result.append(l2_norm_result)
    

    return np.array(all_l2_norm_result)

    pass
    ### Replace with your own code (end)   ###
print(random_unit_vectors(num_vectors, dim))