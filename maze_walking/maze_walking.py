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

maze = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

mazed = [
    [0, 0, 0],
    [1, 0, 0]
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


def valid_check(x,y):
    print(x, y)
    if ((x>=num_row or x<0) or (y>=num_col or y<0)):
        return False
    else:
        return True

def end_point(x, y):
    if (x==num_row-1 and y==num_col-1):
        if (board[x][y]==0):
            print(queue)
            return True
        else:
            return False

# Bread First Search solution
def bfs_mine(board, x, y, queue):
    if (board[x][y]==1):
        return False

    queue.append([x,y])

    print("QUEUE", queue)
    while (queue):
        temp_queue = []
        node = queue.pop()
        if (valid_check(x, y+1) and board[x][y+1]==0):
            reached = end_point(x, y+1)
            if (reached):
                return (node, (x, y+1))
            else:
                temp_queue.append((node, (x, y+1)))
                print("A", temp_queue)

        if (valid_check(x+1, y) and board[x+1][y]==0):
            reached = end_point(x+1, y)
            if (reached):
                return (node, (x+1, y))
            else:
                temp_queue.append((node, (x+1, y)))
                print("B", temp_queue)

        if (valid_check(x, y-1) and board[x][y-1]==0):
            reached = end_point(x, y-1)
            if (reached):
                return (node, (x, y-1))
            else:
                temp_queue.append((node, (x, y-1)))
                print("C", temp_queue)


        if (valid_check(x-1, y) and board[x-1][y]==0):
            reached = end_point(x-1, y)
            if (reached):
                return (node, (x-1, y))
            else:
                temp_queue.append((node, (x-1, y)))
                print("D", temp_queue)


        queue = temp_queue.copy()
        print("NEW QUEUE", queue)

def bfs(board):
    q = [(0,0)]
    while len(q) > 0:
        print("Q Len =", len(q))
        pos = q[0]
        print("POS", pos)
        del q[0]
        if pos[0] == len(board) - 1 and pos[1] == len(board[0]) - 1:
            return True
        next_pos = [(x, y) for x, y in [
            (pos[0] + 1, pos[1]),
            (pos[0] - 1, pos[1]),
            (pos[0], pos[1] + 1),
            (pos[0], pos[1] - 1)
            ] if x >= 0 and x < len(board) and y >=0 and y < len(board[0]) and
                board[x][y] == 0]

        print("LLL", next_pos)
        for n in next_pos:
            print("N",n[0], n[1], "added POS", pos)
            board[n[0]][n[1]] = pos
            q.append(n)
    return False




# Start of the Program
"""path = []
route = dfs(maze, 0, 0, path)
if (route):
    print("Depth-First Search--> path is", path)
else:
    print("Depth-First Search--> no path")
"""
print("BE", maze[1][2])
path = []
found = bfs(maze)
if (found):
    print(len(maze), len(maze[0]), maze[1][2])
    print("M2", maze)
    pos = (maze[len(maze)-1][len(maze[0])-1]) # the exit position
    print("POSbefore", pos)
    while not (pos[0] == 0 and pos[1] ==0):
        path.insert(0, pos)
        print("POS", pos)
        pos = maze[pos[0]][pos[1]]
    print("WHAT IS THIS", pos)
    path.insert(0, (0,0))
    print("Breadth-First Search--> path is", path)
else:
    print("Breadth-First Search--> no path")
