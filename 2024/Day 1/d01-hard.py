with open('input.txt', 'r') as f:
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

s=0

#This time, you'll need to figure out exactly how often each number from the left list appears in the right list. Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.
for i in l:
    s+= i * r.count(i)
print(s)