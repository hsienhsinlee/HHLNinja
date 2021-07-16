#!/usr/local/bin/python3

"""
Description

Given a matrix in the form (int *m, int width, int height), determine
if the matrix is Toeplitz (each diagonal has constant elements) or not.

An example of a Toeplitz matrix is:

 4 5 6 7 2
 9 4 5 6 7
 8 9 4 5 6
 3 8 9 4 5

"""

matrix = [
    [4, 5, 6, 7, 2, 9],
    [9, 4, 5, 6, 7, 2],
    [8, 9, 4, 5, 6, 7],
    [3, 8, 9, 4, 5, 6],
    [1, 3, 8, 9, 4, 5]
]

def isToeplitz(matrix, h, w):

    for i in range(0, w-1):
        val = matrix[0][i]
        for j in range(1, h):
            if (i+j) < w:
                print("m(0,",i,")=", matrix[0][i], "  m(", j, "," ,i+j,")=",matrix[j][i+j])
                if (val != matrix[j][i+j]):
                    return False

    for j in range(1, h-1):
        val = matrix[j][0]
        for i in range(1, w):
            if (i+j) < h:
                print("m(0,",j,")=", matrix[j][0], "  m(", i+j, "," ,i,")=",matrix[i+j][i])
                if (val != matrix[i+j][i]):
                    return False

    return True


height = len(matrix)
width = len(matrix[0])
if (isToeplitz(matrix, height, width)):
    print("Is a Toeplitz !")
else:
    print("NOT a Toeplitz")
