
import numpy as np
numbers = [3, 5, 8, 0, 8]

def partition(numbers):
    num_buckets = 3
    buckets = [[],[],[]]
    numbers_sum = np.sum(numbers)
    max_bucket_value = numbers_sum / 3
    current_bucket = 0
    while len(numbers) > 0:
        number = numbers[0]
        bucket_sum = np.sum(buckets[current_bucket])
        if (bucket_sum + number <= max_bucket_value):
            numbers.pop(0)
            buckets[current_bucket].append(number)
        else:
            current_bucket = current_bucket + 1
            if (current_bucket + 1 > num_buckets):
                return None

    return buckets        

    

partitions = partition(numbers)
print(partitions)