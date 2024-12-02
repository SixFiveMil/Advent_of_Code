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
    ld = 0
    # Check if the list is sorted (ascending or descending)
    if f == sorted(f) or f == sorted(f, reverse=True):
        # Check for adjacent equality
        for i in range(len(f) - 1):
            if f[i] == f[i + 1]:
                return (0, "is unsafe due to adjacent equal elements", ld)
        
        ld = largest_adjacent_distance(f)
        if ld <= 3:
            return (1, "is Safe distance", ld)
        else:
            return (0, "is unsafe distance", ld)
    else:
        return (0, "is unsafe order", ld)

def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        s = 0
        for line in lines:
            floors = [int(x) for x in line.strip().split()]
            sr, msg, ld = safe(floors)
            s += sr
            print("sum:", s, floors, msg, ld)

    print(s)

if __name__ == "__main__":
    main()
