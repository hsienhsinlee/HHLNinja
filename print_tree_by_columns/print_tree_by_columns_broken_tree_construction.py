#!/usr/local/bin/python3

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


Input:
      1
     / \
    2   6
   /   /
  3   7
   \
    4
     \
      5

Output:
3 2 4 1 7 5 6
"""

from collections import OrderedDict


class tree_node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = None
        self.right = None
        self.vline = 0  # to identify the node depth in x-direction
    def display(self):
        print(self.value)
        print(self.left)
        print(self.right)

def tree_construction(input_val):
    print(input_val, len(input_val))
    root = tree_node(input_val.pop(0), None, None)
    enqueue = []
    enqueue.append(root)
    dummy = tree_node(None, None, None)
    while (len(input_val)!=0 and enqueue):
        node = enqueue.pop(0)
        if (node == dummy):
            next
        val1 = input_val.pop(0)
        val2 = input_val.pop(0)
        print("v1=",val1," v2=",val2)
        if (val1 != None):
            node.left  = tree_node(val1, None, None)
            enqueue.append(node.left)
        else:
            enqueue.append(dummy)
        if (val2 != None):
            node.right = tree_node(val2, None, None)
            enqueue.append(node.right)
        else:
            enqueue.append(dummy)
    return root

def breadth_first_search(root):
    sorted_list = OrderedDict()
    enqueue = []
    enqueue.append(root)
    while (enqueue):
        node = enqueue.pop(0)
        vline = node.vline
        val = node.value
        if (vline in sorted_list):
            sorted_list[vline] += [val]
        else:
            sorted_list[vline] = [val]
        ## print(sorted_list)
        if (node.left):
            node.left.vline = vline - 1
            enqueue.append(node.left)
        if (node.right):
            node.right.vline = vline + 1
            enqueue.append(node.right)
    return sorted_list


# main program
aaa = [6,
     3, 4,
     5, None, 1, 0,
     None, 2, None, None, None, None, 8, None,
     None, None, 9, 7, None, None, None, None, None, None, None, None, None, None, None, None]

a = [1,
     2, 3,
     4, 5, 6, 7]
#     8, 9, 10, 11, 12, 13, 14, 15]

a1 = [1,
     2, 6,
     3, None, 7, None,
     None, 4, None, None, None, None, None, None,
     None, None, None, 5, None, None, None, None, None, None, None, None, None, None, None, None,]
root = tree_construction(a)


final_list = breadth_first_search(root)
final_index = sorted(final_list)
for i in final_index:
    for j in final_list[i]:
        print(j, end=' ')

print("")
"""


root.display()
root.left.display()
root.left.left.display()
root.left.left.right.display()
root.left.left.right.left.display()
root.left.left.right.right.display()

root.right.display()
root.right.left.display()
root.right.right.display()
root.right.right.left.display()
"""
