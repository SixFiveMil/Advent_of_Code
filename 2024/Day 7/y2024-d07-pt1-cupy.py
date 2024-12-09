import itertools
import cupy as cp  # CuPy for GPU acceleration
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm  # Install via `pip install tqdm`

def evaluate_left_to_right(numbers, operators):
    """Evaluate the expression strictly left-to-right."""
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            result += numbers[i + 1]
        elif operators[i] == "*":
            result *= numbers[i + 1]
    return result

def math_test(test_value, tests):
    print(f"Running math_test for {test_value} with {tests}")
    n = len(tests)

    # Generate all combinations of "+" and "*" for `n - 1` positions
    operator_combinations = itertools.product(["+", "*"], repeat=n - 1)

    for operators in operator_combinations:
        # Evaluate the numbers and operators strictly left-to-right
        result = evaluate_left_to_right(tests, operators)
        print(f"Evaluating {tests} with {operators} = {result}")
        if result == test_value:
            return True

    return False

def process_line(line):
    print(f"Processing line: {line.strip()}")
    v, t = line.split(':')
    z = [int(i) for i in t.strip().split(' ')]
    if math_test(int(v), z):
        return int(v)
    return 0

def main():
    total = 0
    input_file = r'2024\Day 7\input.txt.'

    # Read all lines from the file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Use ThreadPoolExecutor for parallel processing
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(process_line, line): line for line in lines}

        # Use tqdm to show progress
        with tqdm(total=len(futures), desc="Processing Lines") as pbar:
            for future in as_completed(futures):
                try:
                    result = future.result()
                    print(f"Future result: {result}")
                    total += result
                    pbar.update(1)
                except Exception as e:
                    print(f"Exception in future: {e}")

    print(f"Total: {total}")
    return total

if __name__ == "__main__":
    main()
