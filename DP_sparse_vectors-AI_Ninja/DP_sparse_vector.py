#!/usr/local/bin/python3

"""
Description

Dot product of sparse vectors

Please implement an efficient code to perform dot product of
sparse vectors. A sparse vector is a vector with most elements
equal to zero --- imagine a vector with millions of elements but
only ten thousand or so are non-zero.

[0, 2, 0, 0, 7, 0, 15, 0, 0, 10, 0, 0, 5] *
[1, 0, 0, 2, 3, 0, 20, 7, 0,  0, 0, 0, 2]    = 331

"""

# verification
"""
i = 1
j = 2
len(a) = 5
len(b) = 6
a[i][0] = 4
b[j][0] = 4
psum = 7*3 = 21
"""

def dot_product(a, b):
    i = 0
    j = 0
    psum = 0
    while (i < len(a) and j < len(b)):
        if (a[i][0] > b[j][0]):
            j = j + 1
        elif (a[i][0] < b[j][0]):
            i = i + 1
        else:
            psum = psum + a[i][1] * b[j][1]
            i = i + 1
            j = j + 1

    return psum

a = [(1,2), (4,7), (6,15), (9,10), (12,5)]
b = [(0,1), (3,2), (4,3), (6, 20), (7,7), (12,2)]
print(dot_product(a,b))
