from __future__ import annotations

import sys
import math

four_dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
diag = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
eight_dir = four_dir + diag

if len(sys.argv) < 3:
    print("Usage: python main.py <part_nb> <filename>")
    sys.exit(1)

part = sys.argv[1]
filename = sys.argv[2]

with open(filename, "r") as file:
    input = file.read()

class JunctionBox:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"{self.x}, {self.y}, {self.z}"

    def to_string(self):
        return f"{self.x}.{self.y}.{self.z}"

def dist(b1: JunctionBox, b2: JunctionBox):
    return math.sqrt((b1.x - b2.x) ** 2 + (b1.y - b2.y) ** 2 + (b1.z - b2.z) ** 2)


def part1(input):
    # Create List of Coordinates from input
    circ_lst = []
    for line in input.splitlines():
        x, y, z = map(int, line.split(","))
        circ_lst.append(JunctionBox(x, y, z))
    
    dist_matrix = [[0 for _ in range(len(circ_lst))] for _ in range(len(circ_lst))]
    for i in range(len(circ_lst)):
        for j in range(i+1, len(circ_lst)):
            dist_matrix[i][j] = dist(circ_lst[i], circ_lst[j])
            dist_matrix[j][i] = dist_matrix[i][j]
    
    MAX_CONNECTIONS = 10 if filename == "example.txt" else 1000
    print(f"Max connections: {MAX_CONNECTIONS}")
    
    circuit_mapping = [i for i in range(len(circ_lst))]
    # circuit_ctr = {i: 1 for i in range(len(circ))}

    for _ in range(MAX_CONNECTIONS):
        #find closest boxes
        min_dist = float('inf')
        i_min, j_min = -1, -1
        for i in range(len(circ_lst)):
            for j in range(i+1, len(circ_lst)):
                if dist_matrix[i][j] < min_dist and dist_matrix[i][j] != 0:
                    min_dist = dist_matrix[i][j]
                    i_min, j_min = i, j

        assert i_min!=-1 and j_min!=-1 and min_dist!=float('inf')

        i, j = i_min, j_min
        # print(f"{i} <-> {j} : {dist_matrix[i][j]}")
        dist_matrix[i][j] = 0
        dist_matrix[j][i] = 0
        
        # merge circuits
        circuit_to_keep = circuit_mapping[i]
        circuit_to_replace = circuit_mapping[j]
        # might be the case they were already merged
        if(circuit_to_keep == circuit_to_replace):
            _ -= 1
            continue
        else:
            for idx in range(len(circuit_mapping)):
                if circuit_mapping[idx] == circuit_to_replace:
                    circuit_mapping[idx] = circuit_to_keep
    
    circuit_ctr = {}
    for circ_nb in circuit_mapping:
        if circ_nb not in circuit_ctr:
            circuit_ctr[circ_nb] = 1
        else:
            circuit_ctr[circ_nb] += 1
    
    NB_CIRCUITS = 3
    # find largest circuits
    largest_circuits = sorted(circuit_ctr.values(), reverse=True)[:NB_CIRCUITS]
    print(f"Largest {NB_CIRCUITS} circuits: {largest_circuits}")
    # multiply their sizes
    result = 1
    for size in largest_circuits:
        result *= size

    return result

def part2(input):
    
    return "Part 2 result"

if part == "1":
    print(part1(input))
elif part == "2":
    print(part2(input))