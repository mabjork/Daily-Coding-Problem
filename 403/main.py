import random
import numpy as np

def rand5():
    return random.randint(1, 5)

def rand2():
    None

def rand7():
    None

values = [rand7() for i in range(100000)]
unique, counts = np.unique(values, return_counts=True)
print(counts)
