class Solution:

    WIN_MAP = {
        'A': 'Y',
        'B': 'Z',
        'C': 'X'
    }

    OUTCOME_SCORE = {
        'X': 0,
        'Y': 3,
        'Z': 6
    }

    HAND_SCORE = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input

    def _parse_input(self):
        rounds = []
        for line in self.puzzle_input.split("\n")[:-1]:
            rounds.append(tuple(line.split(" ")))
        return rounds

    # solution: 12772
    def part1(self):
        rounds = self._parse_input()
        total_score = 0
        for opponent, mine in rounds:
            if self.WIN_MAP[opponent] == mine:
                outcome = 'Z'
            elif ord(opponent) == ord(mine) - 23:
                outcome = 'Y'
            else:
                outcome = 'X'

            round_score = self.OUTCOME_SCORE[outcome] + self.HAND_SCORE[mine]
            total_score += round_score
        return total_score
        
    # solution: 11618
    def part2(self):
        rounds = self._parse_input()
        total_score = 0
        for opponent, outcome in rounds:
            if outcome == 'X':
                mine = next(filter(lambda x: x != self.WIN_MAP[opponent] and x != chr(ord(opponent) + 23), self.WIN_MAP.values()))
            elif outcome == 'Y':
                mine = chr(ord(opponent) + 23)
            else:
                mine = self.WIN_MAP[opponent]

            round_score = self.OUTCOME_SCORE[outcome] + self.HAND_SCORE[mine]
            total_score += round_score
        return total_score
                