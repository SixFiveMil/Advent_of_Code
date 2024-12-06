def parse_input(input_map):
    """Parse the input map to extract the grid, guard position, and direction."""
    directions = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}
    grid = []
    guard_pos = None
    guard_dir = None
    
    for y, row in enumerate(line for line in input_map.splitlines() if line.strip()):
        grid_row = []
        for x, char in enumerate(row):
            if char in directions:
                guard_pos = (x, y)
                guard_dir = directions[char]
                grid_row.append('.')  # Replace the guard's starting position with an empty space
            else:
                grid_row.append(char)
        grid.append(grid_row)
    
    if guard_pos is None or guard_dir is None:
        raise ValueError("Guard position or direction not found in the input map.")
    
    return grid, guard_pos, guard_dir

def turn_right(direction):
    """Turn right from the current direction."""
    dx, dy = direction
    return (dy, -dx)

def is_in_bounds(pos, grid):
    """Check if the position is within the grid bounds."""
    x, y = pos
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])

def move_guard(grid, guard_pos, guard_dir):
    """Simulate the guard's patrol and return the number of distinct positions visited."""
    visited = set()
    visited.add(guard_pos)
    
    current_pos = guard_pos
    current_dir = guard_dir
    
    while True:
        # Calculate the position directly in front of the guard
        front_pos = (current_pos[0] + current_dir[0], current_pos[1] + current_dir[1])
        
        if is_in_bounds(front_pos, grid) and grid[front_pos[1]][front_pos[0]] != '#':
            # Move forward
            current_pos = front_pos
            visited.add(current_pos)
        else:
            # Turn right
            current_dir = turn_right(current_dir)
        
        # Check if the guard is out of bounds
        next_pos = (current_pos[0] + current_dir[0], current_pos[1] + current_dir[1])
        if not is_in_bounds(next_pos, grid):
            break
    
    return len(visited)

def guard_patrol(input_map):
    """Main function to calculate the distinct positions visited by the guard."""
    grid, guard_pos, guard_dir = parse_input(input_map)
    return move_guard(grid, guard_pos, guard_dir)

# Read input from file
def main():
    input_file = r'2024\Day 6\test.txt'  # Replace with your input file name
    with open(input_file, "r") as file:
        input_map = file.read()
    
    result = guard_patrol(input_map)
    print(f"Distinct positions visited: {result}")

if __name__ == "__main__":
    main()
