class Solution:
    
    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input

    def _parse_input(self):
        m = []
        for line in self.puzzle_input.split("\n")[:-1]:
            m.append([1 if el == "@" else 0 for el in line])
        return m

    # solution: 1433
    def part1(self):
        grid = self._parse_input()
        total, _ = self.identify_rolls(grid)
        return total

    # solution: 8616
    def part2(self):
        grid = self._parse_input()
        total, removed_rolls = self.identify_rolls(grid)
        grid = self.remove_rolls(grid, removed_rolls)

        while len(removed_rolls) > 0:
            new_total, removed_rolls = self.identify_rolls(grid)
            grid = self.remove_rolls(grid, removed_rolls)
            total += new_total

        return total

    def get_sub_grid(self, grid, i, j):
        width = len(grid[0])
        height = len(grid)
        return [line[max(0, j-1):min(width, j+2)] for line in grid[max(0, i-1):min(height, i+2)]]

    def identify_rolls(self, grid):
        total = 0
        removed_rolls = []
        for pos_i, line in enumerate(grid):
            for pos_j, elem in enumerate(line):

                sub_grid = self.get_sub_grid(grid, pos_i, pos_j)

                if grid[pos_i][pos_j] == 0:
                    continue

                if sum([sum(l) for l in sub_grid]) < 5:
                    removed_rolls.append((pos_i, pos_j))
                    total += 1
        return total, removed_rolls

    def remove_rolls(self, grid, positions):
        for pos in positions:
            grid[pos[0]][pos[1]] = 0
        return grid