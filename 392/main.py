import numpy as np

maze = [
    [0, 1, 1, 0],
    [1, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0]
]

def pad_maze(maze):
    maze_size = len(maze)
    padded_maze = np.zeros((maze_size+2,maze_size+2), dtype=int)
    padded_maze[1:-1,1:-1] = maze
    return padded_maze

def parts_of_land_connected_to_cell(maze, x, y):
    count = 0
    maze_size = maze.shape[0]
    if (x - 1 >= 0):
        count += maze[y,x-1]
    if (x + 1 < maze_size):
        count += maze[y,x+1]
    if (y - 1 >= 0):
        count += maze[y-1,x]
    if (y + 1 < maze_size):
        count += maze[y+1,x]
    return count

def find_circumference(maze):
    circumference = 0
    rows, cols = maze.shape
    for y in range(rows):
        for x in range(cols):
            if (maze[y,x] == 1):
                continue
            cell_value = parts_of_land_connected_to_cell(maze, x, y)
            print("x:",x,"y:",y,"val:",cell_value)
            circumference += cell_value
    return circumference



padded_maze = pad_maze(maze)
print(padded_maze)
print(find_circumference(padded_maze))


