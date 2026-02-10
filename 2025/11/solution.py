from collections import defaultdict
from time import time

class Solution:
    
    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input

    def _parse_input(self):
        rack = defaultdict(list)
        for line in self.puzzle_input.split("\n")[:-1]:
            port_in, ports_out = line.split(":")
            rack[port_in.strip()] = [p.strip() for p in ports_out.split(" ") if p != '']
        return rack
    
    # solution: 670
    def part1(self):
        rack = self._parse_input()

        num_paths = self.explore_paths(rack, 'you')
        return num_paths

    def explore_paths(self, rack, port_in):
        if rack[port_in] == ['out']:
            return 1
        sub_paths = 0
        for port_out in rack[port_in]:
            sub_paths += self.explore_paths(rack, port_out)
        return sub_paths

    # solution: 332052564714990
    def part2(self):
        rack = self._parse_input()
        res = self.explore_paths_dac_fft(rack, 'svr', defaultdict(tuple))
        return res['both']

    def explore_paths_dac_fft(self, rack, port_in, explored_paths):
        if rack[port_in] == ['out']:
            if port_in == 'dac':
                return {'dac': 1, 'fft': 0, 'other': 0, 'both': 0}
            elif port_in == 'fft':
                return {'dac': 0, 'fft': 1, 'other': 0, 'both': 0}
            else:
                return {'dac': 0, 'fft': 0, 'other': 1, 'both': 0}

        explored_paths[port_in] = {'dac': 0, 'fft': 0, 'other': 0, 'both': 0}
        for port_out in rack[port_in]:
            if len(explored_paths[port_out]) == 0:
                dac_fft = self.explore_paths_dac_fft(rack, port_out, explored_paths)
                explored_paths[port_out] = dac_fft
            else:
                dac_fft = explored_paths[port_out]

            if port_in == 'dac':
                explored_paths[port_in]['dac'] += dac_fft['dac'] + dac_fft['other']
                explored_paths[port_in]['fft'] += dac_fft['fft']
                explored_paths[port_in]['other'] = 0
                if explored_paths[port_in]['fft'] > 0:
                    explored_paths[port_in]['both'] = explored_paths[port_in]['fft']
            elif port_in == 'fft':
                explored_paths[port_in]['fft'] += dac_fft['fft'] + dac_fft['other']
                explored_paths[port_in]['dac'] += dac_fft['dac']
                explored_paths[port_in]['other'] = 0
                if explored_paths[port_in]['dac'] > 0:
                    explored_paths[port_in]['both'] = explored_paths[port_in]['dac']
            else:
                explored_paths[port_in]['dac'] += dac_fft['dac']
                explored_paths[port_in]['fft'] += dac_fft['fft']
                explored_paths[port_in]['other'] += dac_fft['other']
                explored_paths[port_in]['both'] += dac_fft['both']
        return explored_paths[port_in]
