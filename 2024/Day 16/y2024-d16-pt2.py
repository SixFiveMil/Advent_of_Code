import heapq

# Directions: North, East, South, West
DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def parse_maze_from_file(filename):
    """Parse the maze from a file and find the start and end positions."""
    with open(filename, 'r') as file:
        grid = [line.rstrip() for line in file]
    
    start, end = None, None
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'S':
                start = (x, y)
            elif cell == 'E':
                end = (x, y)
    return grid, start, end

def heuristic(pos, goal):
    """Calculate Manhattan distance heuristic."""
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

def a_star(filename):
    """Run the A* algorithm on a maze read from a file."""
    grid, start, end = parse_maze_from_file(filename)
    rows, cols = len(grid), len(grid[0])

    # Priority queue for A* (cost, x, y, direction, path_tiles)
    pq = []
    heapq.heappush(pq, (0, *start, 1, {(start[0], start[1])}))  # (cost, x, y, direction, visited_tiles)
    visited = {}
    lowest_cost = float('inf')
    optimal_tile_sets = []

    while pq:
        cost, x, y, direction, tiles = heapq.heappop(pq)

        # Skip if this state has been visited with a lower cost
        if (x, y, direction) in visited and visited[(x, y, direction)] <= cost:
            continue
        visited[(x, y, direction)] = cost

        # If we've reached the end
        if (x, y) == end:
            if cost < lowest_cost:
                # Found a new lower-cost path, reset the optimal tile sets
                lowest_cost = cost
                optimal_tile_sets = [tiles]
            elif cost == lowest_cost:
                # Add this set of tiles to the optimal tile sets
                optimal_tile_sets.append(tiles)
            continue

        # Move forward
        dx, dy = DIRECTIONS[direction]
        nx, ny = x + dx, y + dy
        if 0 <= nx < cols and 0 <= ny < rows and grid[ny][nx] != '#':
            heapq.heappush(pq, (cost + 1, nx, ny, direction, tiles | {(nx, ny)}))

        # Rotate clockwise
        heapq.heappush(pq, (cost + 1000, x, y, (direction + 1) % 4, tiles))

        # Rotate counterclockwise
        heapq.heappush(pq, (cost + 1000, x, y, (direction - 1) % 4, tiles))

    # Combine all unique tiles in the lowest-cost paths
    all_optimal_tiles = set()
    for tile_set in optimal_tile_sets:
        all_optimal_tiles.update(tile_set)

    return lowest_cost, len(all_optimal_tiles)


def main():
    filename = input_file = r'2024\Day 16\test2.txt'
    cost, tile_count = a_star(filename)
    print("Lowest cost:", cost)
    print("Number of unique tiles in all lowest-score paths:", tile_count)


# Run the algorithm
if __name__ == "__main__":
    main()
    