pipes = {
    'plant': {'A': 1, 'B': 5, 'C': 20},
    'A': {'C': 15},
    'B': {'C': 10},
    'C': {}
}

def get_all_possible_pipes_sorted(pipes):
    possible_pipes = []
    for from_key, to_map in pipes.items():
        for to_key, cost in to_map.items():
            possible_pipes.append((from_key, to_key, cost))
    return sorted(possible_pipes, key=lambda x: x[2])

def find_optimal_configuration(pipes):
    possible_pipes = get_all_possible_pipes_sorted(pipes)
    connected_houses = ()
    final_pipe_config = []
    for from_house, to_house, cost in possible_pipes:
        if (from_house not in connected_houses or to_house not in connected_houses):
            final_pipe_config.append((from_house, to_house, cost))
            connected_houses += (to_house, from_house)
    return final_pipe_config

print(find_optimal_configuration(pipes))
