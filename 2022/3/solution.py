class Solution:

    CONV_FACTOR_LOW = 96
    CONV_FACTOR_UPP = 38

    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input

    def _parse_input(self):
        sacks = []
        for line in self.puzzle_input.split("\n")[:-1]:
            sacks.append(tuple([line[:int(len(line)/2)], line[int(len(line)/2):]]))
        return sacks

    # solution: 7674
    def part1(self):
        sacks = self._parse_input()
        priority_score = 0
        for comp1, comp2 in sacks:
            priority_char = set([*comp1]).intersection(set([*comp2])).pop()
            if priority_char.isupper():
                priority_score += ord(priority_char) - self.CONV_FACTOR_UPP
            else:
                priority_score += ord(priority_char) - self.CONV_FACTOR_LOW
        return priority_score
        
    # solution: 2805
    def part2(self):
        sacks = self._parse_input()
        priority_score = 0
        index = 0
        while index < len(sacks):
            elves = [''.join(elf) for elf in sacks[index:index+3]]
            priority_char = set([*elves[0]]).intersection(set([*elves[1]])).intersection(set([*elves[2]])).pop()
            if priority_char.isupper():
                priority_score += ord(priority_char) - self.CONV_FACTOR_UPP
            else:
                priority_score += ord(priority_char) - self.CONV_FACTOR_LOW
            index += 3
        return priority_score


                