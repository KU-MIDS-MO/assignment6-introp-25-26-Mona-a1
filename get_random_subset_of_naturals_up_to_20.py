import numpy as numpy

from numpy import array
from numpy.linalg import norm 




def get_random_subset_of_naturals_up_to_20():

    

    x =  numpy.random.randint(0,2**20)

    a = []
   
    for i in range(20): 
        if x % 2 == 0:
            x = x//2
        else:
            a.append(i+1)
            x = x//2


    return numpy.array(a)
    pass
    ### Replace with your own code (end)   ###


print(get_random_subset_of_naturals_up_to_20())