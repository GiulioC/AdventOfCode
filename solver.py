import argparse
import sys

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--year', required=True)
    argparser.add_argument('--day', required=True)
    argparser.add_argument('--part', required=True)
    args = argparser.parse_args()

    # import part1 and part2 solutions
    sys.path.append(f"{args.year}/{args.day}/")
    from solution import Solution

    try:
        with open(f"{args.year}/{args.day}/input", "r") as f:
            puzzle_input = f.read()
    except FileNotFoundError:
        print("Unable to find puzzle input for the selected day!")
        sys.exit(1)

    s = Solution(puzzle_input)
    try:
        if args.part == '1':
            result = s.part1()
        else:
            result = s.part2()
    except NotImplementedError:
        print("This solution has not been implemented yet!")
        sys.exit(1)

    print(f"The solution for part {args.part} is: {result}")
    