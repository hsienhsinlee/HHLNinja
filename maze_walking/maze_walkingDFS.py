#!/usr/local/bin/python3


mazeL = [
    [0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 0]
]

maze2 = [
    [0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0]
]

mazeX = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 0]
]

maze33 = [
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 0]
]

maze23 = [
    [0, 0, 0],
    [1, 0, 0]
]

maze = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 0]
]

num_row = len(maze)
num_col = len(maze[0])
#print(num_row)
#print(num_col)

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
def dfs(board, x, y, ex, ey, path):
    path.append((x,y))

    # if it is exit
    if (x==ex and y==ey):
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
    r = dfs(board, x+1,   y,    ex, ey, path)
    if (r):
        return True
    r = dfs(board, x,     y+1,  ex, ey, path)
    if (r):
        return True
    r = dfs(board, x,     y-1,  ex, ey, path)
    if (r):
        return True
    r = dfs(board, x-1,   y,    ex, ey, path)
    if (r):
        return True
    else:
        del path[-1]
        return False



# Start of the Program
start_x = 0
start_y = 3
end_x = 0 #len(maze) - 1
end_y = 0 #len(maze[0]) - 1

print(maze[0])
print(maze[1])
print(maze[2])


# DFS solution

path = []
route = dfs(maze, start_x, start_y, end_x, end_y, path)
if (route):
    print("Depth-First Search--> path is", path)
else:
    print("Depth-First Search--> no path")
