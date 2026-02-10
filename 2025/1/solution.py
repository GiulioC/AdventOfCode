class Solution:
    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input

    def _parse_input(self):
        rotations = []
        for rotation in self.puzzle_input.split("\n")[:-1]:
            direction = rotation[0]
            entity = int(rotation[1:])

            if direction == 'L':
                rotations.append(-entity)
            else:
                rotations.append(entity)
        return rotations

    # solution: 1168
    def part1(self):
        rotations = self._parse_input()
        position = 50
        total = 0
        for rotation in rotations:
            position += rotation
            position = position % 100

            if position == 0:
                total += 1
        return total

    # solution: 7199
    def part2(self):
        rotations = self._parse_input()
        position = 50
        total = 0
        for rotation in rotations:
            new_position = position + rotation
            if new_position < 0:
                total += new_position // -100
                if position != 0:
                    total += 1
            elif new_position == 0:
                total += 1
            elif new_position >= 100:
                total += new_position // 100

            position = new_position % 100
        return total