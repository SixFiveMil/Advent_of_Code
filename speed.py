import os
import subprocess
import time
import argparse

# Function to run a Python script and return the execution time
def run_python_script(file_path, num_runs=5):
    times = []
    for _ in range(num_runs):
        start_time = time.time()
        subprocess.run(['python', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

# Function to run an executable and return the execution time
def run_executable(file_path, num_runs=5):
    times = []
    for _ in range(num_runs):
        start_time = time.time()
        subprocess.run([file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

# Function to process all Python and executable files in the directory
def test_all_files_in_directory(directory, num_runs=5):
    results = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if filename.endswith('.py'):
            print(f"Testing Python script: {filename}")
            times = run_python_script(file_path, num_runs)
        elif filename.endswith('.exe'):
            print(f"Testing Executable: {filename}")
            times = run_executable(file_path, num_runs)
        else:
            continue
        
        # Calculate min, max, and average times
        min_time = min(times)
        max_time = max(times)
        avg_time = sum(times) / len(times)
        
        results.append({
            'filename': filename,
            'min_time': min_time,
            'max_time': max_time,
            'avg_time': avg_time
        })

    return results

# Function to print the results
def print_results(results):
    for result in results:
        print(f"{result['filename']}: Min Time = {result['min_time']:.6f}s, Max Time = {result['max_time']:.6f}s, Avg Time = {result['avg_time']:.6f}s")

# Main function to run the tests
def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Automated testing script for Python and Executable files.")
    parser.add_argument('directory', type=str, help="Path to the directory containing .py and .exe files")
    parser.add_argument('--num_runs', type=int, default=5, help="Number of times to run each file (default: 5)")

    args = parser.parse_args()

    # Get the directory path and number of runs from the command-line arguments
    directory = args.directory
    num_runs = args.num_runs

    # Run tests and print results
    results = test_all_files_in_directory(directory, num_runs)
    print_results(results)

if __name__ == "__main__":
    main()
