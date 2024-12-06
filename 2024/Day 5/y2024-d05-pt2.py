from collections import defaultdict, deque

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

def reorder_update(update, rules):
    """Reorder an update using topological sorting based on the rules."""
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    # Build graph for pages in the update
    applicable_rules = [(x, y) for x, y in rules if x in update and y in update]
    for x, y in applicable_rules:
        graph[x].append(y)
        in_degree[y] += 1
        in_degree.setdefault(x, 0)
    
    # Topological sort
    queue = deque([node for node in update if in_degree[node] == 0])
    ordered_update = []
    while queue:
        node = queue.popleft()
        ordered_update.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return ordered_update

def find_middle_page(update):
    """Find the middle page number in a sorted update."""
    mid_index = len(update) // 2
    return update[mid_index]

def calculate_middle_page_sum_for_incorrect_updates(file_path):
    """Calculate the sum of middle pages from reordered incorrect updates."""
    rules, updates = parse_input(file_path)
    incorrect_updates = []
    
    for update in updates:
        if not is_update_valid(update, rules):
            incorrect_updates.append(update)
    
    # Reorder each incorrect update and find the middle pages
    middle_page_sum = sum(
        find_middle_page(reorder_update(update, rules))
        for update in incorrect_updates
    )
    return middle_page_sum

# Example usage
file_path = r'2024\Day 5\input.txt'  # Replace with your file path
result = calculate_middle_page_sum_for_incorrect_updates(file_path)
print(f"Sum of middle pages from reordered incorrect updates: {result}")
