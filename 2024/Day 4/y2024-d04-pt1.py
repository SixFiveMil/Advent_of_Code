def count_xmas(grid):
    rows, cols = len(grid), len(grid[0])
    word = "XMAS"
    directions = [
        (0, 1),   # Right
        (1, 0),   # Down
        (0, -1),  # Left
        (-1, 0),  # Up
        (1, 1),   # Down-right diagonal
        (1, -1),  # Down-left diagonal
        (-1, 1),  # Up-right diagonal
        (-1, -1)  # Up-left diagonal
    ]
    
    def is_valid(x, y):
        """Check if the coordinates are within the grid bounds."""
        return 0 <= x < rows and 0 <= y < cols

    def search(x, y, index, dx, dy):
        """Recursive search for the word."""
        if index == len(word):  # Found the complete word
            return 1
        if not is_valid(x, y) or grid[x][y] != word[index]:  # Out of bounds or mismatch
            return 0
        return search(x + dx, y + dy, index + 1, dx, dy)

    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "X":  # Start searching for the word
                for dx, dy in directions:
                    count += search(i, j, 0, dx, dy)

    return count


def main():
    # Open the file in read mode
    with open(r'2024\Day 4\input.txt.', 'r') as file:
        # Read all lines from the file
        lines = file.readlines()

    # Convert each line into a list of characters
    list_of_lists = [list(line.strip()) for line in lines]

    return count_xmas(list_of_lists)


if __name__ == "__main__":
   print(main())