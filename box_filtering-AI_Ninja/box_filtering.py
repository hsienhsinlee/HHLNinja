#!/usr/local/bin/python3

"""
Description

Box filtering (averaging filtering)

Implement a box filter which blur the image / average the neighborhood.
The input contains an image and a box size. For each pixel, its value
in the output image should be the average of its neighorhood in the
input image. The neighborhood is defined by the box size.

boundary condition: 0 padding
box size: odd (e.g., 3x3 or 5x5)


"""

# verification
"""

"""
from copy import copy, deepcopy
from math import floor
###import numpy as np

# Brute-force approach
def box_filter_BS(img, sbox):
    #duplicate a new destination image
    new_img = deepcopy(img)
    denominator = sbox * sbox
    stride = floor(sbox / 2)
    print("stide=", stride)
    for i in range(0, len(img)):
        for j in range(0, len(img[0])):
            #print("i=",i," j=",j, " mat=", img[i][j])
            psum = 0
            #print("i=", i, " j=", j, "psum=", psum)
            for ii in range(i-stride, i+stride+1):
                for jj in range(j-stride, j+stride+1):
                    if (ii <0 or jj<0 or ii>=len(img) or jj>=len(img[0])):
                       continue
                    else:
                        #print("  ii=", ii, " jj=", jj, " img=", img[ii][jj])
                        psum = psum + img[ii][jj]
            #print("    i=", i, " j=", j, "psum=", psum)
            new_img[i][j] = psum / denominator

    return new_img

image2 = [
            [9, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [9, 9, 9, 9, 9, 9],
            [9, 9, 9, 9, 9, 9],
            [0, 0, 0, 0, 0, 0]
]

image = [
            [25, 0,  0,  0,  0,  0,  0],
            [0,  0,  0,  0,  25, 25, 25],
            [25, 25, 0,  0,  25, 25, 25],
            [25, 25, 25, 0,  0,  25, 25],
            [0,  0,  0,  0,  0,  25, 25],
            [25, 0,  0,  0,  0,  0,  25],
            [0,  0,  0,  0,  0,  0,  25]
]


image1 = [
            [1, -1, -2, -4, -8, 0],
            [1, -1,  0,  0,  8, 0],
            [1, -1,  0,  0,  0, 0],
            [1,  1,  0,  0,  0, 0],
            [1,  1,  0,  0,  0, 0]
]

size_of_box = 5
filtered_image = box_filter_BS(image, size_of_box)
#print(image)
for i in range(len(filtered_image)):
    print(filtered_image[i])
