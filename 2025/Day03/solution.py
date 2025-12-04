def solve_day3_part1(input_file):
    """
    Day 3 Part 1: Find the maximum joltage by selecting 2 batteries from each bank.
    """
    with open(input_file, 'r') as f:
        lines = f.read().strip().split('\n')
    
    total_joltage = 0
    
    for line in lines:
        # For each bank, find the pair of positions (i, j) where i < j
        # that maximizes the 2-digit number formed by line[i] + line[j]
        max_joltage = 0
        
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                # Form number with digit at position i first, then position j
                joltage = int(line[i] + line[j])
                max_joltage = max(max_joltage, joltage)
        
        total_joltage += max_joltage
    
    return total_joltage


def solve_day3_part2(input_file):
    """
    Day 3 Part 2: Find the maximum joltage by selecting 12 batteries from each bank.
    Uses greedy algorithm: at each step, find the largest digit we can still reach,
    then take it and continue.
    """
    def maximize_k_digits(line, k):
        """Select k digits to form the largest k-digit number in position order."""
        n = len(line)
        if n <= k:
            return line
        
        result = []
        start = 0
        
        for _ in range(k):
            # How many digits do we still need?
            remaining_needed = k - len(result)
            # How many digits can we skip? (must have at least remaining_needed after)
            max_skip = n - start - remaining_needed
            
            # Find the maximum digit in the range [start, start + max_skip + 1)
            max_digit = line[start]
            max_pos = start
            
            for j in range(start, min(start + max_skip + 1, n)):
                if line[j] > max_digit:
                    max_digit = line[j]
                    max_pos = j
            
            result.append(max_digit)
            start = max_pos + 1
        
        return ''.join(result)
    
    with open(input_file, 'r') as f:
        lines = f.read().strip().split('\n')
    
    total_joltage = 0
    
    for line in lines:
        joltage_str = maximize_k_digits(line, 12)
        joltage = int(joltage_str)
        total_joltage += joltage
    
    return total_joltage


if __name__ == "__main__":
    input_file = "input.txt"
    
    part1_result = solve_day3_part1(input_file)
    print(f"Day 3 Part 1 - Total output joltage: {part1_result}")
    
    part2_result = solve_day3_part2(input_file)
    print(f"Day 3 Part 2 - Total output joltage (12 batteries): {part2_result}")

