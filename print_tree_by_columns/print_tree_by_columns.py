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
"""

from collections import OrderedDict

class tree_node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = None
        self.right = None
        self.vline = 0
    def display(self):
        print("value=", self.value) #, "  vertical_level=",self.vertical_level, "  horizontal_level=",self.horizontal_level)
        print(self.left)
        print(self.right)

def tree_construction():
    # building left side of the tree
    root = tree_node(6, None, None)
    root.left = tree_node(3, None, None)
    root.left.left = tree_node(5, None, None)
    root.left.left.right = tree_node(2, None, None)
    root.left.left.right.left = tree_node(9, None, None)
    root.left.left.right.right = tree_node(7, None, None)
    # building right side of the tree
    root.right = tree_node(4, None, None)
    root.right.left = tree_node(1, None, None)
    root.right.right = tree_node(0, None, None)
    root.right.right.left = tree_node(8, None, None)
    return root


def breadth_first_search(treelist):
    #vline = 0
    sorted_list = OrderedDict()
    enqueue = []
    enqueue.append(treelist)
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
root = tree_construction()
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
