
import math

def euqlidian_distance(current_pos, new_pos):
    c_x, c_y = current_pos
    n_x, n_y = new_pos
    return math.sqrt((n_x - c_x)**2 + (n_y - c_y)**2)

move_operations = [
    lambda x,y: (x+1,y),
    lambda x,y: (x-1,y),
    lambda x,y: (x,y+1),
    lambda x,y: (x,y-1),
    lambda x,y: (x-1,y-1),
    lambda x,y: (x+1,y+1),
    lambda x,y: (x-1,y+1),
    lambda x,y: (x+1,y-1) 
]

def find_optimal_move(current_pos, goal_pos):
    lowest_dist = math.inf
    position = None
    for operation in move_operations:
        pos_after_move = operation(current_pos[0], current_pos[1])
        distance = euqlidian_distance(pos_after_move, goal_pos)
        if (distance < lowest_dist):
            lowest_dist = distance
            position = pos_after_move
        if (position == goal_pos):
            break

    return position

def traverse_positions(positions):
    num_moves = 0
    current_position = positions[0]
    for next_position in positions[1:]:
        while True:
            position_after_move = find_optimal_move(current_position, next_position)
            num_moves += 1
            if (position_after_move == next_position):
                current_position = next_position
                break
            else:
                current_position = position_after_move
    return num_moves

positions = [(0, 0), (1, 1), (1, 2), (5, 5)]

print(traverse_positions(positions))