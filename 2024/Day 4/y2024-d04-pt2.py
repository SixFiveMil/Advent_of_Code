def count_xshape_mas(grid):
    rows, cols = len(grid), len(grid[0])

    def is_valid(x, y):
        """Check if coordinates are within grid bounds."""
        return 0 <= x < rows and 0 <= y < cols

    def check_xshape(x, y):
        """Check if the X-shape pattern exists with A in the center."""
        if not is_valid(x, y) or grid[x][y] != 'A':  # Center must be 'A'
            return 0

        count = 0

        # Define the two possible X-shapes
        patterns = [
            ((x - 1, y - 1), (x + 1, y + 1)),  # Top-left to bottom-right
            ((x - 1, y + 1), (x + 1, y - 1))   # Top-right to bottom-left
        ]

        for m_pos, s_pos in patterns:
            # Check "MAS"
            if (is_valid(*m_pos) and grid[m_pos[0]][m_pos[1]] == 'M' and
                is_valid(*s_pos) and grid[s_pos[0]][s_pos[1]] == 'S'):
                count += 1

            # Check "SAM"
            if (is_valid(*m_pos) and grid[m_pos[0]][m_pos[1]] == 'S' and
                is_valid(*s_pos) and grid[s_pos[0]][s_pos[1]] == 'M'):
                count += 1

        return count

    # Count occurrences of the X-shape pattern
    total_count = 0
    for i in range(rows):
        for j in range(cols):
            total_count += check_xshape(i, j)
    
    return total_count


def main():
    # Open the file in read mode
    with open(r'2024\Day 4\test.txt.', 'r') as file:
        # Read all lines from the file
        lines = file.readlines()

    # Convert each line into a list of characters
    list_of_lists = [list(line.strip()) for line in lines]

    return count_xshape_mas(list_of_lists)


if __name__ == "__main__":
   print(main())