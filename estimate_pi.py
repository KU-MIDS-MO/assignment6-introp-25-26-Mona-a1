import numpy as np

from numpy import array
from numpy.linalg import norm 

num_samples = 100000

def estimate_pi(num_samples):
    
    x = []
    y = []
    z = 0
    
    
    pi = np.pi
    
    for i in range(num_samples):
        x.append(np.random.rand())
        y.append(np.random.rand())
        
    for i in range(num_samples):
        if x[i]**2+y[i]**2 <= 1:
            z = z + 1
    
    a = (4*(z/num_samples))
    

    return a


print(estimate_pi(num_samples))