def largest_adjacent_distance(nums):
    if len(nums) < 2:
        return 0  # No adjacent elements to compare
    max_distance = 0
    for i in range(len(nums) - 1):
        distance = abs(nums[i] - nums[i + 1])
        if distance > max_distance:
            max_distance = distance
    return max_distance

def safe(f):
    if f == sorted(f) or f == sorted(f,reverse=True):
        if largest_adjacent_distance(f) <= 3:
            return 1
    return 0


with open(r'2024\Day 1\test.txt', 'r') as f:
    lines = f.readlines()
    s=0
    for line in lines:
        floors = [int(x) for x in line.strip().split()]
        s += safe(floors)

print(s)

