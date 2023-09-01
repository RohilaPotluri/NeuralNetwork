import numpy as np

# Create random vector of size 20 with floats between 1 and 20
vector = np.random.uniform(1, 20, 20)

# Reshape the vector to 4 by 5
reshape_arr = vector.reshape(4, 5)

# Replace the max in each row by 0
reshape_arr[np.arange(4), reshape_arr.argmax(axis=1)] = 0

print(reshape_arr)