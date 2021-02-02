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


def bfs(board, sx, sy, ex, ey):
    if (board[sx][sy]==1):
        return False

    q = [(sx, sy)]
    while len(q) > 0:
        #print("len(q) =", len(q))
        pos = q[0]
        #print("q[0] == ", pos)
        del q[0]

        # Reach the end
        if pos[0] == ex and pos[1] == ey:
            return True
        next_pos = [(x, y) for x, y in [
            (pos[0] + 1, pos[1]),
            (pos[0] - 1, pos[1]),
            (pos[0], pos[1] + 1),
            (pos[0], pos[1] - 1)
            ] if x >= 0 and x < len(board) and y >=0 and y < len(board[0]) and
                board[x][y] == 0]

        print("next_pos", next_pos)
        for n in next_pos:
            #print("n in next_pos",n[0], n[1], "added POS", pos)
            board[n[0]][n[1]] = pos
            q.append(n)
    return False



# Start of the Program
start_x = 0
start_y = 0
end_x = len(maze) - 1
end_y = len(maze[0]) - 1

print(maze)
# DFS solution
path = []
route = dfs(maze, start_x, start_y, end_x, end_y, path)
if (route):
    print("Depth-First Search--> path is", path)
else:
    print("Depth-First Search--> no path")


# BFS solution
maze = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 0]
]
path = []
found = bfs(maze, start_x , start_y, end_x, end_y)
if (found):
    #print(len(maze), len(maze[0]), maze[1][2])
    #print("updated maze", maze)
    pos = (maze[len(maze)-1][len(maze[0])-1]) # backtrack from the exit position
    # start from the destination
    path.insert(0, (end_x, end_y))
    while not (pos[0] == start_x and pos[1] == start_y):
        path.insert(0, pos)
        pos = maze[pos[0]][pos[1]]
    path.insert(0, pos) # (start_x, start_y))
    print("Breadth-First Search--> path is", path)
else:
    print("Breadth-First Search--> no path")
