def read_input_file(file_path):
    """Reads the input file and returns its content as a string."""
    with open(file_path, 'r') as file:
        return file.read().strip()

def parse_disk_map(disk_map):
    """Parses the disk map into a list of file IDs and free space blocks."""
    parsed_map = []
    for i in range(0, len(disk_map), 2):
        file_length = int(disk_map[i])
        free_space_length = int(disk_map[i + 1]) if i + 1 < len(disk_map) else 0
        parsed_map.extend([i // 2] * file_length + ['.'] * free_space_length)
    return parsed_map

def compact_files(disk_map):
    """Compacts the files in the disk map by moving file blocks to the leftmost free space."""
    compacted_map = [block for block in disk_map if block != '.'] + ['.'] * disk_map.count('.')
    return compacted_map

def calculate_checksum(disk_map):
    """Calculates the checksum of the compacted disk map."""
    return sum(pos * block for pos, block in enumerate(disk_map) if block != '.')

def main():
    input_file = r'2024\Day 9\input.txt'
    raw_disk_map = read_input_file(input_file)
    
    # Parse the disk map into a detailed representation
    parsed_disk_map = parse_disk_map(raw_disk_map)
    
    # Compact the disk map
    compacted_disk_map = compact_files(parsed_disk_map)
    
    # Calculate the checksum
    checksum = calculate_checksum(compacted_disk_map)
    
    print(f"Resulting filesystem checksum: {checksum}")

if __name__ == "__main__":
    main()
