import numpy as np

# read text file into 2 dimensional char array
with open(r'2024\Day 4\input.txt.', 'r') as file:
    lines = file.readlines()
    array = np.array([list(line.rstrip()) for line in lines])


def check_subarray(subarray):
    check = ["MAS", "SAM"]
    s1 = "".join(subarray.ravel()[[0, 4, 8]])
    s2 = "".join(subarray.ravel()[[2, 4, 6]])
    return (s1 in check) and (s2 in check)

x_mas_count = 0
for i in range(1, array.shape[0]-1):
    for j in range(1, array.shape[0]-1):
        subarray = array[i-1:i+2, j-1:j+2]
        x_mas_count += check_subarray(subarray)

print(f"Total X-MAS count: {x_mas_count}")