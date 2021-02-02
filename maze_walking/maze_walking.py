#!/usr/local/bin/python3

"""
*** Description ***

You are given a game board represented as a 2D array of zeroes and ones.
Zero stands for passable positions and one stands for impassable positions.
Design an algorithm to find a path from top left corner to bottom right corner.
For example, for the following board:

entrance -> 0 0 0 0 0 0 0
            0 0 1 0 0 1 0
            0 0 1 0 1 1 0
            0 0 1 0 1 0 1
            1 1 1 0 0 0 0 -> exit

A possible path is:

entrance -> + + + + 0 0 0
            0 0 1 + 0 1 0
            0 0 1 + 1 1 0
            0 0 1 + 1 0 1
            1 1 1 + + + + -> exit

Assuming a zero-indexed grid of rows and columns, we'd return:

(0, 0) -> (0, 1) -> (0, 2) -> (0, 3) -> (1, 3) -> (2, 3) ->
(3, 3) -> (4, 3) -> (4, 4) -> (4, 5) -> (4, 6)

"""

maze = [
    [0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 0]
]

maze = [
    [0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 0]
]

maze3 = [
    [0, 0, 1],
    [1, 0, 0],
    [0, 1, 0]
]

maze2 = [
    [0, 0, 0],
    [0, 0, 1]
]

num_row = len(maze)
num_col = len(maze[0])
print(num_row)
print(num_col)

# iterating thru maze
"""
for row in maze2:
    for col in row:
        print(col)


for row in range(0, num_row):
    for col in range(0, num_col):
        print(maze[row][col])
"""


# Depth-First Search
def dfs(board, x, y, path):
    path.append((x,y))

    # if it is exit
    if (x==num_row-1 and y==num_col-1):
        if (board[x][y]==0):
            return True
        else:
            return False

    # outside the board
    if ((x>=num_row or x<0) or (y>=num_col or y<0)):
        del path[-1]
        return False

    # backtrack needed as the node is an impasse or has been visited
    if (board[x][y] != 0):
        del path[-1]
        return False

    board[x][y] = 2 # visited entry
    r = dfs(board, x+1,   y,    path)
    if (r):
        return True
    r = dfs(board, x,     y+1,  path)
    if (r):
        return True
    r = dfs(board, x,     y-1,  path)
    if (r):
        return True
    r = dfs(board, x-1,   y,    path)
    if (r):
        return True
    else:
        del path[-1]
        return False


path = []
route = dfs(maze, 0, 0, path)
if (route):
    print("path is", path)
else:
    print("no path", path)
