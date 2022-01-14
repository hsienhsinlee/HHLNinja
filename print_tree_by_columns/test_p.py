#!/opt/homebrew/bin/python3.7

"""
Description

Given the root of a binary tree containing integers, print each column from left to right,
and within each column print the values from top to bottom.

Input:
      6
     / \
    3   4
   /   / \
  5   1   0
   \     /
    2   8
   / \
  9   7

Output:
5 9 3 2 6 1 7 4 8 0
"""

from binarytree import build


nodes =[3, 6, 8, 2, 11, None, 13]
