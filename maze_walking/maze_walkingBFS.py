#!/usr/local/bin/python3


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

maze33 = [
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 0]
]

maze23 = [
    [0, 0, 0],
    [1, 0, 0]
]

mazex = [
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

        #print("next_pos", next_pos)
        for n in next_pos:
            #print("n in next_pos",n[0], n[1], "added POS", pos)
            board[n[0]][n[1]] = pos
            q.append(n)
    return False



# Start of the Program
start_x = 0
start_y = 6
end_x = 2 #len(maze) - 1
end_y = 0# len(maze[0]) - 1


for i in range(0, len(maze)):
    print(maze[i])

# BFS solution
path = []
found = bfs(maze, start_x , start_y, end_x, end_y)
if (found):
    #pos = (maze[len(maze)-1][len(maze[0])-1]) # backtrack from the exit position
    pos = (end_x, end_y)
    # start from the destination
    #path.insert(0, (end_x, end_y))
    while not (pos[0] == start_x and pos[1] == start_y):
        path.insert(0, pos)
        pos = maze[pos[0]][pos[1]]
    path.insert(0, (start_x, start_y))
    print("Breadth-First Search--> path is", path)
else:
    print("Breadth-First Search--> no path")
