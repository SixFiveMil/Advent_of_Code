import argparse
import re
def decode(lines):
    combined_lines = "".join(lines)
    pattern1 = r"mul\(\d*,\d*\)"
    pattern2 = r"\d*,\d*"
    all_matches = []
    matches=re.findall(pattern1, combined_lines)
    for m in matches:
        all_matches.extend(re.findall(pattern2, m))
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
    with open('2024\\Day 3\\input.txt', 'r') as f:
        muls = decode(f.readlines())
    for mul in muls:
        r = mul.split(',')
        m+= int(r[0]) * int(r[1])
    return m



if __name__ == "__main__":
   print(main())