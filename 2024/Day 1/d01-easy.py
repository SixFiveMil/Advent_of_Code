with open('input.txt', 'r') as f:
    lines = f.readlines()
    l,r=[], []
    for line in lines:
        nums = line.strip().split()
        if len(nums) == 2:  # Ensure there are exactly two numbers
            l.append(int(nums[0]))
            r.append(int(nums[1]))

l.sort()
r.sort()
d=0
for i in range(0, len(l)):
    d += abs(l[i] - r[i])
print(d)