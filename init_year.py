import argparse
import sys
import os

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--year', required=True)
    args = argparser.parse_args()

    if not os.path.isdir(args.year):
        os.mkdir(args.year)

    for i in range(25):
        target_dir = os.path.join(args.year, str(i+1))

        if os.path.isdir(target_dir):
            continue

        os.mkdir(target_dir)
        with open(os.path.join(target_dir, "solution.py"), "w") as f:
            f.write("""\
class Solution:
    
    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input

    def _parse_input(self):
        pass
    
    # solution:
    def part1(self):
        raise(NotImplementedError)

    # solution:
    def part2(self):
        raise(NotImplementedError)
                """)
    