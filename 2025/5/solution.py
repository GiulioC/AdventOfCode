class Solution:
    
    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input

    def _parse_input(self):
        part1, part2 = self.puzzle_input.split("\n\n")

        ranges = []
        for line in part1.split("\n"):
            ranges.append((int(line.split("-")[0]), int(line.split("-")[1])))

        ids = [int(id) for id in part2.split("\n")[:-1]]

        return ranges, ids
    
    # solution: 758
    def part1(self):
        ranges, ids = self._parse_input()

        fresh_count = 0
        for num in ids:
            for r in ranges:
                if r[0] <= num <= r[1]:
                    fresh_count += 1
                    break
        return fresh_count

    # solution:     343143696885053
    def part2(self):
        ranges, _ = self._parse_input()

        merged_ranges = []
        for r in sorted(ranges):
            if len(merged_ranges) == 0:
                merged_ranges.append(r)
            else:
                last_range = merged_ranges.pop()
                if last_range[1] >= r[0]:
                    merged_ranges.append((last_range[0], max(last_range[1], r[1])))
                else:
                    merged_ranges.append(last_range)
                    merged_ranges.append(r)

        return sum([el[1]-el[0]+1 for el in merged_ranges])