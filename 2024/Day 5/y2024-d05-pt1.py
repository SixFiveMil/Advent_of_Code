from collections import defaultdict

def parse_input(file_path):
    """Parse the input file to extract ordering rules and updates."""
    with open(file_path, 'r') as file:
        lines = file.read().split("\n")
    
    # Split sections by blank line
    split_index = lines.index("")
    rules_section = lines[:split_index]
    updates_section = lines[split_index + 1:]
    
    # Parse rules and updates
    rules = [tuple(map(int, line.split('|'))) for line in rules_section if line]
    updates = [list(map(int, line.split(','))) for line in updates_section if line]
    
    return rules, updates

def is_update_valid(update, rules):
    """Check if an update respects the given ordering rules."""
    rule_set = {(x, y) for x, y in rules if x in update and y in update}
    positions = {page: i for i, page in enumerate(update)}
    return all(positions[x] < positions[y] for x, y in rule_set)

def find_middle_page(update):
    """Find the middle page number in a sorted update."""
    mid_index = len(update) // 2
    return update[mid_index]

def calculate_middle_page_sum(file_path):
    """Calculate the sum of middle pages from valid updates."""
    rules, updates = parse_input(file_path)
    valid_updates = []
    for update in updates:
        if is_update_valid(update, rules):
            valid_updates.append(update)
    
    # Find the middle page of each valid update and sum them
    middle_page_sum = sum(find_middle_page(update) for update in valid_updates)
    return middle_page_sum

# Example usage
file_path = r'2024\Day 5\input.txt'  # Replace with your file path
result = calculate_middle_page_sum(file_path)
print(f"Sum of middle pages from valid updates: {result}")
