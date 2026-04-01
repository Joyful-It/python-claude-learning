import numpy as np

data=np.array([12,21,32,23,34,544,23,21])
print(data[0:3])
new_data=data.reshape(4,2)
print(new_data)

print(new_data[1:3,0:1])

table = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print(table[1:3,1:3])
