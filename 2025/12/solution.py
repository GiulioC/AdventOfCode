import re


class Solution:
    
    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input

    def _parse_input(self):
        shape_sizes = []
        grids = []

        temp_shape_size = 0
        for group in self.puzzle_input.split("\n\n")[:-1]:
            for line in group.split("\n"):
                if re.match(r"[0-9]:", line) is not None:
                    if temp_shape_size > 0:
                        shape_sizes.append(temp_shape_size)
                    temp_shape_size = 0
                    continue
                temp_shape_size += sum([1 if el == "#" else 0 for el in line])
        shape_sizes.append(temp_shape_size)

        for line in self.puzzle_input.split("\n\n")[-1].split("\n")[:-1]:
            width, length = re.findall(r'([0-9]+)x([0-9]+)', line)[0]
            grid_size = int(width) * int(length)
            nums = [int(n.strip()) for n in line.split(":")[1].split(" ") if n != ""]
            grids.append((grid_size, nums))

        return shape_sizes, grids

    # solution: 422
    def part1(self):
        shapes, grids = self._parse_input()

        valid_grids = 0
        for grid in grids:
            needed_space = sum([n*s for n,s in list(zip(shapes, grid[1]))])
            valid_grids += 1 if grid[0] > needed_space else 0
        return valid_grids

    # solution: -
    def part2(self):
        return "Merry Christmas!"
                