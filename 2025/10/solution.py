from itertools import combinations
from z3 import *

class Solution:

    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input

    def _parse_input(self):
        machines = []
        for parts in [line.strip().split() for line in self.puzzle_input.split("\n")[:-1]]:
            solution = [c == "#" for c in parts[0][1:-1]]
            buttons = [[int(b) for b in button[1:-1].split(",")] for button in parts[1:-1]]
            voltages = [int(v) for v in parts[-1][1:-1].split(",")]
            machines.append([solution, buttons, voltages])
        return machines

    # solution: 432
    def part1(self):
        machines = self._parse_input()
        total = 0
        for solution, buttons, _ in machines:
            presses = 0
            lights = [False] * len(solution)
            while lights != solution:
                presses += 1
                for combo in combinations(range(len(buttons)), presses):
                    lights = [False] * len(solution)
                    for button in combo:
                        for b in buttons[button]:
                            lights[b] = not lights[b]
                    if lights == solution:
                        break
            total += presses
        return total

    # solution: 18011
    def part2(self):
        machines = self._parse_input()
        total = 0
        for _, buttons, voltages in machines:
            solver = Solver()

            bvars = [Int(f"a{n}") for n in range(len(buttons))]
            for b in bvars:
                solver.add(b >= 0)

            for i, v in enumerate(voltages):
                vvars = [bvars[j] for j, button in enumerate(buttons) if i in button]
                solver.add(Sum(vvars) == v)

            while solver.check() == sat:
                model = solver.model()
                n = sum([model[d].as_long() for d in model])
                solver.add(Sum(bvars) < n)

            total += n
        return total
