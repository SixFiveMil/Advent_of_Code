import argparse

def main():
    parser = argparse.ArgumentParser(description="A script with a verbose flag")
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode')
    args = parser.parse_args()

    if args.verbose:
        print("Verbose mode enabled")

    # Your main script logic here
    print("Running script...")

    with open('input.txt', 'r') as f:
        lines = f.readlines()


if __name__ == "__main__":
    main()