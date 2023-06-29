class Solution:

    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input

    def _parse_input(self):
        pairs = []
        for line in self.puzzle_input.split("\n")[:-1]:
            pair1, pair2 = line.split(",")
            pairs.append((tuple([int(n) for n in pair1.split("-")]), tuple([int(n) for n in pair2.split("-")])))
        return pairs
    
    def _is_contained(self, pair1, pair2):
        return pair1[0] <= pair2[0] and pair1[1] >= pair2[1]
    
    def _overlaps(self, pair1, pair2):
        return pair2[0] >= pair1[0] and pair2[0] <= pair1[1] 

    # solution: 496
    def part1(self):
        pairs = self._parse_input()
        total = 0
        for p1, p2 in pairs:
            if self._is_contained(p1, p2) or self._is_contained(p2, p1):
                total += 1
        return total

        
    # solution: 847
    def part2(self):
        pairs = self._parse_input()
        total = 0
        for p1, p2 in pairs:
            if self._overlaps(p1, p2) or self._overlaps(p2, p1):
                total += 1
        return total               
                