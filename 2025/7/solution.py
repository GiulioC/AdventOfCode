import numpy as np

class Solution:
    
    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input

    def _parse_input(self):
        lines = self.puzzle_input.split("\n")[:-1]

        parsed_lines = [np.array([1 if char == "S" else 0 for char in lines[0]])]
        for line in lines[1:]:
            parsed_lines.append(np.array([1 if char == "^" else 0 for char in line]))

        return parsed_lines

    # solution: 1533
    def part1(self):
        lines = self._parse_input()
        beam = lines[0]

        num_splits = 0
        for line in lines[1:]:
            if np.sum(line) == 0:
                continue

            splits = np.where(beam & line == 1)[0]

            if len(splits) == 0:
                continue

            num_splits += len(splits)

            new_beam = np.copy(beam)
            new_beam[splits] = 0
            new_beam[splits-1] = 1
            new_beam[splits+1] = 1

            beam = new_beam
        return num_splits

    # solution: 10733529153890
    def part2(self):
        lines = self._parse_input()
        beam = lines[0]

        for line in lines[1:]:
            if np.sum(line) == 0:
                continue

            beam_mod = np.array([1 if num >= 1 else 0 for num in beam])
            splits = np.where(beam_mod & line == 1)[0]

            if len(splits) == 0:
                continue

            new_beam = np.copy(beam)
            for el in splits:
                new_beam[el] -= beam[el]
                new_beam[el-1] += beam[el]
                new_beam[el+1] += beam[el]

            beam = new_beam
        return np.sum(beam)
