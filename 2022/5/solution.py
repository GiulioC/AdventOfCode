import re

class Solution:

    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input

    def _parse_input(self):
        start_config, operations = self.puzzle_input.split("\n\n")

        start_config = start_config.split("\n")[::-1]

        stacks = {int(s):[] for s in start_config[0].split()}
        for cranes in start_config[1:]:
            for idx, crane in enumerate([m if m.strip() != '' else None for m in re.findall("(... )", cranes+" ")]):
                if crane is None:
                    continue
                stacks[idx+1].append(re.search('\[(.)\]', crane)[1])
        
        parsed_ops = []
        for op in operations.split("\n")[:-1]:
            num, start, dest = re.search("move (.+) from (.) to (.)", op).groups()
            parsed_ops.append((int(start), int(dest), int(num)))

        return stacks, parsed_ops
    
    def _move_crane(self, start, dest):
        crane = self.stacks[start].pop()
        self.stacks[dest].append(crane)

    def _move_crane_v2(self, start, dest, num):
        cranes = self.stacks[start][-num:]
        for _ in range(num):
            self.stacks[start].pop()
        self.stacks[dest].extend(cranes)

    # solution: JRVNHHCSJ
    def part1(self):
        stacks, operations = self._parse_input()
        self.stacks = stacks

        for op in operations:
            for _ in range(op[2]):
                self._move_crane(op[0], op[1])

        message = ""
        for cranes in self.stacks.values():
            message = f"{message}{cranes[-1]}"
        return message
        
    # solution: GNFBSBJLH
    def part2(self):
        stacks, operations = self._parse_input()
        self.stacks = stacks

        for op in operations:
                self._move_crane_v2(op[0], op[1], op[2])

        message = ""
        for cranes in self.stacks.values():
            message = f"{message}{cranes[-1]}"
        return message             
                