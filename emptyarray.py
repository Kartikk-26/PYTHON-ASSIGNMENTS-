# python program to create
# Empty and Full Numpy arrays

import numpy as np


# Create an empty array
empa = np.empty((3, 4), dtype=int)
print("Empty Array")
print(empa)

# Create a full array
flla = np.full([3, 3], 55, dtype=int)
print("\n Full Array")
print(flla)
