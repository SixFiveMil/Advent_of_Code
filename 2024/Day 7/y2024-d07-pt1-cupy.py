from collections import defaultdict

def parse_input(lines):
    """
    Parse the input to extract antenna positions and their frequencies.
    """
    antennas = defaultdict(list)
    rows = len(lines)
    cols = len(lines[0].strip())

    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            if char.isalnum():  # Any lowercase, uppercase letter, or digit
                antennas[char].append((x, y))

    return antennas, rows, cols

def calculate_antinode_positions(antennas, rows, cols):
    """
    Calculate all unique antinode positions within the bounds of the map.
    """
    antinodes = set()

    for freq, positions in antennas.items():
        n = len(positions)
        if n < 2:
            continue  # Need at least two antennas for antinodes

        # Compare all pairs of antennas with the same frequency
        for i in range(n):
            for j in range(i + 1, n):  # Ensure no duplicate comparisons
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                # Calculate midpoint
                mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2

                # Check if the midpoint is an integer
                if mid_x.is_integer() and mid_y.is_integer():
                    # Convert midpoint to integer tuple
                    mid_x, mid_y = int(mid_x), int(mid_y)

                    # Calculate potential antinode positions
                    dx, dy = x2 - x1, y2 - y1
                    antinode_1 = (x1 - dx, y1 - dy)
                    antinode_2 = (x2 + dx, y2 + dy)

                    # Add antinodes if within bounds
                    if 0 <= antinode_1[0] < cols and 0 <= antinode_1[1] < rows:
                        antinodes.add(antinode_1)
                    if 0 <= antinode_2[0] < cols and 0 <= antinode_2[1] < rows:
                        antinodes.add(antinode_2)

    return antinodes

def solve(lines):
    """
    Solve the puzzle by parsing input, calculating antinodes, and counting unique locations.
    """
    # Parse the input to find antenna positions
    antennas, rows, cols = parse_input(lines)

    # Get all antenna positions as a set
    all_antenna_positions = set(pos for positions in antennas.values() for pos in positions)

    # Calculate antinode positions
    antinodes = calculate_antinode_positions(antennas, rows, cols)

    # Merge antinodes and antenna positions
    unique_positions = antinodes | all_antenna_positions

    # Return the count of unique positions
    return len(unique_positions)

def main():
    input_data = [
        "............",
        "........0...",
        ".....0......",
        ".......0....",
        "....0.......",
        "......A.....",
        "............",
        "............",
        "........A...",
        ".........A..",
        "............",
        "............"
    ]

    # Solve the puzzle
    total = solve(input_data)
    
    # Print the result
    print(f"Total unique antinode locations: {total}")

if __name__ == "__main__":
    main()
