import re
from functools import reduce
from operator import mul

class Solution:
    
    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input

    def _parse_input(self):
        rows = {}
        for line in self.puzzle_input.split("\n")[:-1]:
            for pos, num in enumerate([n for n in re.split("\s", line) if n != ""]):
                try:
                    value = int(num)
                except ValueError:
                    value = num
                try:
                    rows[pos].append(value)
                except KeyError:
                    rows[pos] = [value]
        return rows

    def _parse_input_part2(self):
        columns = {num: '' for num in range(len(self.puzzle_input.split("\n")[0]))}
        for line in self.puzzle_input.split("\n")[:-1]:
            for pos, char in enumerate(line):
                if char not in ('+', '*', ' '):
                    columns[pos] = f"{columns[pos]}{char}"
        return columns
    
    # solution: 5060053676136
    def part1(self):
        rows = self._parse_input()
        total = 0
        for col in rows.values():
            if col[-1] == "*":
                total += reduce(mul, col[:-1], 1)
            else:
                total += sum(col[:-1])
        return total

    # solution: 9695042567249
    def part2(self):
        numbers = self._parse_input_part2()
        operations = [(ind, char) for ind, char in enumerate(self.puzzle_input.split("\n")[-2]) if char != ' ']
        total = 0

        for pos,operation in enumerate(operations):
            if pos == len(operations) - 1:
                range_max = len(numbers.keys())
            else:
                range_max = operations[pos+1][0]-1
            nums = [int(numbers[ind].strip()) for ind in range(operation[0], range_max)]
            if operation[1] == "*":
                total += reduce(mul, nums, 1)
            else:
                total += sum(nums)
        return total
