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


Input:
          1
        /   \
       2     3
      / \   /
     4   5 6

Acceptable Outputs:
4 2 1 5 6 3
4 2 1 6 5 3
"""

from collections import OrderedDict

class tree_node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = None
        self.right = None
        self.vline = 0  # to identify the node depth in x-direction

def tree_construction(input_val):
    root = tree_node(input_val.pop(0), None, None)
    enqueue = []
    enqueue.append(root)
    dummy_node = tree_node(None, None, None)
    while (len(input_val)!=0 and enqueue):
        node = enqueue.pop(0)
        if (node == dummy_node):
            next
        val_left = input_val.pop(0)
        val_right = input_val.pop(0)
        if (val_left != None):
            node.left  = tree_node(val_left, None, None)
            enqueue.append(node.left)
        else:
            enqueue.append(dummy_node)
        if (val_right != None):
            node.right = tree_node(val_right, None, None)
            enqueue.append(node.right)
        else:
            enqueue.append(dummy_node)

    return root

def BFS_leveling(root):
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
        if (node.left):
            node.left.vline = vline - 1
            enqueue.append(node.left)
        if (node.right):
            node.right.vline = vline + 1
            enqueue.append(node.right)
    return sorted_list

def print_tree_by_column(tree):
    bucket_list = BFS_leveling(tree)
    final_index = sorted(bucket_list)
    for i in final_index:
        for j in bucket_list[i]:
            print(j, end=' ')
    print("")

# main program
tree1 = [6,
        3, 4,
        5, None, 1, 0,
        None, 2, None, None, None, None, 8, None,
        None, None, 9, 7, None, None, None, None, None, None, None, None, None, None, None, None]

tree2 = [1,
        2, 6,
        3, None, 7, None,
        None, 4, None, None, None, None, None, None,
        None, None, None, 5, None, None, None, None, None, None, None, None, None, None, None, None]

tree3 = [1,
        2, 3,
        4, 5, 6, None]

input_tree = tree_construction(tree1)
print_tree_by_column(input_tree)



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
