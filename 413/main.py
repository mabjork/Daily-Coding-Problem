
def find_combinations(num_steps, possible_steps):
    if(num_steps == 0 or all(step > num_steps for step in possible_steps)):
        return [[]]

    all_combinations = []
    for step in possible_steps:
        if (step > num_steps):
            continue
        combinations_after_step = find_combinations(num_steps - step, possible_steps)
        for combination in combinations_after_step:
            combination.insert(0, step)
        all_combinations.extend(combinations_after_step)
    
    return all_combinations

print(find_combinations(5, [1, 3, 4, 5]))