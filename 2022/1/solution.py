class Solution:

    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input

    def _parse_input(self):
        sums = []
        for elf in self.puzzle_input.split("\n\n")[:-1]:
            sums.append(sum([int(cal) for cal in elf.split("\n")]))
        return sums

    # solution: 70698
    def part1(self):
        sums = self._parse_input()
        return max(sums)
        
    # solution: 206643
    def part2(self):
        sums = self._parse_input()
        top3 = 0
        top3 += max(sums)
        del sums[sums.index(max(sums))]
        top3 += max(sums)
        del sums[sums.index(max(sums))]
        top3 += max(sums)
        return top3              
                