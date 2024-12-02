def largest_adjacent_distance(nums):
    if len(nums) < 2:
        return 0  # No adjacent elements to compare
    max_distance = 0
    for i in range(len(nums) - 1):
        distance = abs(nums[i] - nums[i + 1])
        if distance > max_distance:
            max_distance = distance
    return max_distance

def is_safe_list(f):
    ld = largest_adjacent_distance(f)
    if (f == sorted(f) or f == sorted(f, reverse=True)) and ld <= 3:
        for i in range(len(f) - 1):
            if f[i] == f[i + 1]:
                return False  # Unsafe due to adjacent equal elements
        return True
    return False

def safe(f):
    if is_safe_list(f):
        ld = largest_adjacent_distance(f)
        return (1, "is Safe distance", ld)
    
    # Test by removing one element at a time
    for i in range(len(f)):
        modified_list = f[:i] + f[i+1:]
        if is_safe_list(modified_list):
            ld = largest_adjacent_distance(modified_list)
            return (1, "is Safe distance after removing element", ld)
    
    ld = largest_adjacent_distance(f)
    return (0, "is unsafe", ld)

def main():
    with open('2024\Day 2\\input.txt', 'r') as f:
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
