class Solution:
    
    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input

    def _parse_input(self):
        return [(int(r.split("-")[0]), int(r.split("-")[1])) for r in self.puzzle_input[:-1].split(",")]

    # solution: 31839939622
    def part1(self):
        """
        Mia soluzione:
        - scarta tutti i range i cui estremi hanno lunghezza uguale e dispari
        - se gli estremi hanno lunghezze diverse:
            - destra dispari: trasforma destra in 9{n}, con n lunghezza estremo sinistro
            - sinistra dispari: trasforma destra in 10{n}, con n lunghezza estremo destro - 1
        - prendi la prima metà delle cifre degli estremi e calcola gli step (incremento di 1) tra uno e l'altro,
          gestendo i corner case di primo/ultimo step
        """
        ranges = self._parse_input()
        total_sum = 0

        for r in ranges:
            r1 = r[0]
            r2 = r[1]
            l1 = len(str(r1))
            l2 = len(str(r2))

            if l1 % 2 != 0 and l1 == l2:
                continue

            if l2 > l1:
                if l1 % 2 == 0:
                    # check from l1 to 9{l1}
                    r2 = int('9' * l1)
                    l2 = l1
                elif l2 % 2 == 0:
                    # check from 10{l2-1} to l2
                    r1 = int('1' + '0' * (l2 - 1))
                    l1 = l2

            r1 = str(r1)
            r2 = str(r2)
            hl = int(l1/2)

            if r1[:hl] > r1[hl:]:
                start = r1[:hl]
            else:
                start = str(int(r1[:hl]) + 1)

            if r2[:hl] > r2[hl:]:
                end = str(int(r2[:hl]) - 1)
            else:
                end = r2[:hl]

            start = start[:hl]
            end = end[:hl]

            while int(start) <= int(end):
                total_sum += int(f"{start}{start}")
                start = str(int(start) + 1)
        return total_sum

    # solution: 41662374059
    def part2(self):
        ranges = self._parse_input()
        total_sum = 0

        for r in ranges:
            r1 = r[0]
            r2 = r[1]

            range_duplicates = []

            while r1 <= r2:
                r1s = str(r1)

                for sub_length in range(int(len(r1s)/2)):
                    sub_string = r1s[:sub_length+1]

                    if len(r1s) % len(sub_string) != 0:
                        pass

                    if sub_string * int(len(r1s) / len(sub_string)) == r1s:
                        range_duplicates.append(r1)
                r1 += 1

            for num in set(range_duplicates):
                total_sum += int(num)
        return total_sum
