from collections import defaultdict
from itertools import groupby
from functools import reduce
from operator import mul
import numpy as np


class Solution:

    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input

    def _parse_input(self):
        positions = []
        for line in self.puzzle_input.split("\n")[:-1]:
            x, y, z = line.split(",")
            positions.append(np.array([int(x), int(y), int(z)]))
        return positions

    # solution: 63920
    def part1(self):
        positions = self._parse_input()
        distances = []

        for i, position1 in enumerate(positions):
            for j, position2 in enumerate(positions[i + 1:]):
                distances.append((int(np.linalg.norm(position1 - position2)), i, j + i + 1))

        shortest_distances = sorted(distances, key=lambda x: x[0])[:1000]
        uf = UnionFind(len(positions))

        for d in shortest_distances:
            if uf.find(d[1]) == uf.find(d[2]):
                continue
            uf.unite(d[1], d[2])

        parents = defaultdict(list)
        for num in range(len(positions)):
            parent = uf.find(num)
            parents[parent].append(num)

        max_sizes = sorted(map(lambda x: len(x), parents.values()), reverse=True)[:3]
        return reduce(mul, max_sizes, 1)

    # solution: 1026594680
    def part2(self):
        positions = self._parse_input()
        distances = []

        for i, position1 in enumerate(positions):
            for j, position2 in enumerate(positions[i + 1:]):
                distances.append((int(np.linalg.norm(position1 - position2)), i, j + i + 1))

        shortest_distances = sorted(distances, key=lambda x: x[0])
        uf = UnionFind(len(positions))

        connected = set()
        result = None
        for d in shortest_distances:
            if uf.find(d[1]) == uf.find(d[2]):
                continue
            uf.unite(d[1], d[2])

            num_connections = len(connected)
            if num_connections == len(positions) - 1:
                result = positions[d[1]][0] * positions[d[2]][0]
            else:
                connected.add(d[1])
                connected.add(d[2])

        return result


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def unite(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
