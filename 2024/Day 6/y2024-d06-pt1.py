def read_grid_from_file(file_path):
    """Reads the grid from a text file."""
    with open(file_path, "r") as file:
        grid = [line.strip() for line in file.readlines()]
    return grid

def parse_grid(grid):
    walls = set()
    guard_position = None
    guard_direction = None
    direction_map = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell == "#":
                walls.add((row_idx, col_idx))
            elif cell in direction_map:
                guard_position = (row_idx, col_idx)
                guard_direction = direction_map[cell]
    
    return walls, guard_position, guard_direction

def simulate_guard(grid, guard_position, guard_direction, walls):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    direction_order = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
    
    # Determine the initial direction index
    direction_idx = direction_order.index(guard_direction)
    current_pos = guard_position
    
    while True:
        visited.add(current_pos)
        # Calculate the position in front of the guard
        next_row, next_col = current_pos[0] + direction_order[direction_idx][0], current_pos[1] + direction_order[direction_idx][1]
        
        if (next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or (next_row, next_col) in walls):
            # Turn right 90 degrees
            direction_idx = (direction_idx + 1) % 4
        else:
            # Move forward
            current_pos = (next_row, next_col)
            if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
                break  # Guard steps off the grid
    
    return visited

# Main program
if __name__ == "__main__":
    file_path = r'2024\Day 6\test.txt'  # Replace with your text file's path
    grid = read_grid_from_file(file_path)
    
    # Parse the grid
    walls, guard_position, guard_direction = parse_grid(grid)

    # Simulate guard's movement
    unique_positions = simulate_guard(grid, guard_position, guard_direction, walls)

    # Output results
    print("Walls:", walls)
    print("Guard's initial position:", guard_position)
    print("Unique positions visited by the guard:", unique_positions)
