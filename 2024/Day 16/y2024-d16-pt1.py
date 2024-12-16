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

    # Priority queue for A* (cost, x, y, direction, path)
    pq = []
    heapq.heappush(pq, (0, *start, 1, []))  # (cost, x, y, direction_index, path)
    visited = set()

    while pq:
        cost, x, y, direction, path = heapq.heappop(pq)

        if (x, y, direction) in visited:
            continue
        visited.add((x, y, direction))

        # If we've reached the end
        if (x, y) == end:
            return cost, path

        # Move forward
        dx, dy = DIRECTIONS[direction]
        nx, ny = x + dx, y + dy
        if 0 <= nx < cols and 0 <= ny < rows and grid[ny][nx] != '#':
            heapq.heappush(pq, (cost + 1, nx, ny, direction, path + [(nx, ny, direction)]))

        # Rotate clockwise
        heapq.heappush(pq, (cost + 1000, x, y, (direction + 1) % 4, path + [(x, y, (direction + 1) % 4)]))

        # Rotate counterclockwise
        heapq.heappush(pq, (cost + 1000, x, y, (direction - 1) % 4, path + [(x, y, (direction - 1) % 4)]))

def main():
    filename = input_file = r'2024\Day 16\input.txt'
    cost, path = a_star(filename)
    print("Lowest cost:", cost)
    print("Path:", path)
    print("Path:", )

# Run the algorithm
if __name__ == "__main__":
    main()