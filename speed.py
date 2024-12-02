import os
import subprocess
import time

def measure_execution_time(command):
    """
    Measure the execution time of a command.
    """
    start_time = time.time()
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        end_time = time.time()
        execution_time = end_time - start_time
        return execution_time, result.returncode, result.stdout, result.stderr
    except Exception as e:
        return None, -1, "", str(e)

def main():
    directory = os.getcwd()  # Current working directory
    results = []  # Store results for each file

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if file.endswith(".py"):
            print(f"Testing Python script: {file}")
            command = ["python", file_path]
            exec_time, return_code, stdout, stderr = measure_execution_time(command)
            results.append((file, "Python", exec_time, return_code, stderr))
        elif file.endswith(".exe"):
            print(f"Testing C++ executable: {file}")
            command = [file_path]
            exec_time, return_code, stdout, stderr = measure_execution_time(command)
            results.append((file, "C++", exec_time, return_code, stderr))

    # Print results
    print("\nExecution Results:")
    print(f"{'File':<20} {'Type':<10} {'Time (s)':<10} {'Status':<10} {'Error':<30}")
    print("-" * 80)
    for file, lang_type, exec_time, status, error in results:
        status_str = "Success" if status == 0 else "Failed"
        print(f"{file:<20} {lang_type:<10} {exec_time:<10.6f} {status_str:<10} {error[:30]:<30}")

if __name__ == "__main__":
    main()
