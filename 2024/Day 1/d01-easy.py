with open('2024\Day 1\input.txt', 'r') as f:
    lines = f.readlines()
    l,r=[], []
    #each line is a serries of 2 numbers serpated by white spaces
    #example 50472   55227
    # seperate each set into 2 lists, sort those lists so the smallest number of each list is at the top
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