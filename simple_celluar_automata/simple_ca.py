#!/usr/local/bin/python3 

import random

mutation = 1
bound = 370
ca_shape = [0] * bound
new_shape = [0] * bound
len_ca = len(ca_shape)
ca_shape[1] = 1
ca_shape[bound//2] = 0
iterations = 0

while (iterations < 10000000):
    for i in range(len_ca):
        if (ca_shape[i]):
            print("o", end="")
        else:
            print(" ", end="")
    print("")        
    # evoluation code
    
    new_shape[0] = ca_shape[1] % 2
    new_shape[len_ca-1] = ca_shape[len_ca-2] % 2
    for i in range(1, len_ca-1):
        new_shape[i] =(ca_shape[i-1] + ca_shape[i+1]) % 2
    ca_shape = new_shape.copy()
    mutation = random.randint(0,1) and ((iterations % 1000000) ==0)
    if (mutation==1):
        ca_shape = [0] * bound
        random_num = random.randint(1, bound-1)
        ca_shape[random_num] = 1
        #if (ca_shape[random_num]):
        #    ca_shape[random_num] = 0
        #else:
        #    ca_shape[random_num] = 1
        
    iterations += 1

"""
for i in range(len_ca):
    print("*", end="")
print("")        
"""
