import argparse
import re
def decode(file_path):
    # Open the file and process it line by line
    with open(file_path, 'r') as file:
        save_data = True  # Control flag to determine whether to save data
        filtered_content = []  # List to store the valid parts

        for line in file:
            i = 0  # Index for line traversal
            while i < len(line):
                if save_data:
                    # Check if "don't()" starts at the current index
                    if line[i:i+7] == "don't()":
                        save_data = False
                        i += 7  # Skip past "don't()"
                    else:
                        filtered_content.append(line[i])
                        i += 1
                else:
                    # Look for "do()" to resume saving
                    if line[i:i+4] == "do()":
                        save_data = True
                        i += 4  # Skip past "do()"
                    else:
                        i += 1

        # Join the filtered content into a single string
        filtered_string = ''.join(filtered_content)

    # Regex to match mul(x, y)
    pattern1 = r"mul\(\d+,\d+\)"
    pattern2 = r"\d+,\d+"

    # Find all mul(x, y) matches in the filtered string
    matches = re.findall(pattern1, filtered_string)

    # Extract numbers from the matches
    all_matches = [re.search(pattern2, m).group() for m in matches]

    return all_matches

def main():
    parser = argparse.ArgumentParser(description="A script with a verbose flag")
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode')
    args = parser.parse_args()

    if args.verbose:
        print("Verbose mode enabled")

    # Your main script logic here
    print("Running script...")
    m = 0
    file_path = '2024\\Day 3\\input.txt'
    output = decode(file_path)
    for mul in output:
        r = mul.split(',')
        m+= int(r[0]) * int(r[1])
    return m



if __name__ == "__main__":
   print(main())