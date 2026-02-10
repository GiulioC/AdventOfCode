from collections import defaultdict
import numpy as np

class Solution:
    
    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input

    def _parse_input(self):
        return [(int(line.split(",")[1]), int(line.split(",")[0])) for line in self.puzzle_input.split("\n")[:-1]]
    
    # solution: 4754955192
    def part1(self):
        points = self._parse_input()
        sorted_points = sorted(points, key=lambda x: (x[0], x[1]))

        sizes = []
        for pos, point in enumerate(sorted_points):
            for pp in sorted_points[pos+1:]:
                if point[1] > pp[1]:
                    new_point1 = pp[1]
                    pp = (pp[0], point[1])
                    step_point = (point[0], new_point1)
                else:
                    step_point = point

                size = (pp[0] - step_point[0] + 1) * (pp[1] - step_point[1] + 1)
                sizes.append((size, step_point, pp))

        return sorted(sizes, reverse=True)[0][0]

    # solution: 1568849600
    def part2(self):
        points = self._parse_input()
        sorted_points = sorted(points, key=lambda x: (x[0], x[1]))

        max_row = max([p[0] for p in sorted_points])
        matrix = [[] for _ in range(max_row+1)]

        # compute edges and fill them as 1s in the matrix
        for pos, point in enumerate(sorted_points):
            matrix[point[0]].append(point[1])
            for pp in sorted_points[(pos+1):]:
                if point[0] == pp[0]:
                    # horizontal edge
                    for i in range(point[1], pp[1] + 1):
                        matrix[point[0]].append(i)
                if point[1] == pp[1]:
                    # vertical edge
                    for i in range(point[0], pp[0] + 1):
                        matrix[i].append(point[1])

        matrix_idx = {}
        # only store the first and last occurrence of 1s in each line
        for line_num, line in enumerate(matrix):
            if len(line) == 0:
                continue
            matrix_idx[line_num] = (min(line), max(line))

        sizes = []
        for pos, point in enumerate(sorted_points):
            for pp in sorted_points[pos+1:]:

                top_left = (min(point[0], pp[0]), min(point[1], pp[1]))
                top_right = (min(point[0], pp[0]), max(point[1], pp[1]))
                bottom_left = (max(point[0], pp[0]), min(point[1], pp[1]))
                bottom_right = (max(point[0], pp[0]), max(point[1], pp[1]))

                # if any of the edges is outside the area, skip this rectangle
                if not matrix_idx[top_left[0]][0] <= top_left[1] <= matrix_idx[top_left[0]][1]:
                    continue
                if not matrix_idx[top_left[0]][0] <= top_right[1] <= matrix_idx[top_left[0]][1]:
                    continue
                if not matrix_idx[bottom_left[0]][0] <= bottom_left[1] <= matrix_idx[bottom_left[0]][1]:
                    continue
                if not matrix_idx[bottom_left[0]][0] <= bottom_right[1] <= matrix_idx[bottom_left[0]][1]:
                    continue

                # also check each point of both vertical sides of the rectangle
                # to avoid situations like the one below
                #
                #   #XXXXXXXXXXXXXXXXXXX#
                #   X    +---------+    X
                #   X    |         |    X
                #   X    |         |    X
                #   #XXXXXXX#      |    X
                #        |  X      |    X
                #        |  X      |    X
                #   #XXXXXXX#      |    X
                #   X    |         |    X
                #   X    +---------+    X
                #   X                   X
                #   #XXXXXXXXXXXXXXXXXXX#
                #
                invalid = False
                for i in range(top_left[0], bottom_left[0]):
                    if not matrix_idx[i][0] <= top_left[1] <= matrix_idx[i][1]:
                        invalid = True
                        break
                if invalid:
                    continue

                for i in range(top_right[0], bottom_right[0]):
                    if not matrix_idx[i][0] <= top_right[1] <= matrix_idx[i][1]:
                        invalid = True
                        break
                if invalid:
                    continue

                size = (top_right[1] - top_left[1] + 1) * (bottom_left[0] - top_left[0] + 1)
                sizes.append((size, top_left, bottom_right))
        return sorted(sizes, reverse=True)[0][0]