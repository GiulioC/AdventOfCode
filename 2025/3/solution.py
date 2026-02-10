class Solution:
    
    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input

    def _parse_input(self):
        return [line for line in self.puzzle_input.split("\n")[:-1]]

    # solution: 17535
    def part1(self):
        banks = self._parse_input()
        total = 0
        for bank in banks:
            zz = zip(list(bank), range(len(bank)))
            ss = sorted(list(zz), key=lambda x: (x[0], -x[1]), reverse=True)

            highest = ss[0]
            trailing_bank = list(filter(lambda x: x[1] > highest[1], ss))
            if len(trailing_bank) > 0:
                second_highest = trailing_bank[0]
                joltage = f"{highest[0]}{second_highest[0]}"
            else:
                second_highest = ss[1]
                joltage = f"{second_highest[0]}{highest[0]}"

            total += int(joltage)
        return total

    # solution: 173577199527257
    def part2(self):
        banks = self._parse_input()
        total = 0
        for bank in banks:
            zz = zip(list(bank), range(len(bank)))
            ss = sorted(list(zz), key=lambda x: (x[0], -x[1]), reverse=True)

            joltage = self.find_highest_substr(ss, 13, "")
            total += int(joltage)
        return total

    def check_bank_length(self, high, size):
        return high[1] + size <= 100

    def find_highest_substr(self, sorted_list, size=12, joltage=""):
        highest = sorted_list[0]
        ii = 0
        while not self.check_bank_length(highest, size - 1):
            ii += 1
            highest = sorted_list[ii]

        joltage = f"{joltage}{highest[0]}"
        if size == 2:
            return joltage
        else:
            new_list = list(filter(lambda x: x[1] > highest[1], sorted_list))
            return self.find_highest_substr(new_list, size - 1, joltage)