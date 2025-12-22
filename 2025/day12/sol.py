import sys
import math
import copy
from collections import deque

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

class Region:
    def __init__(self, w, h, ctrs):
        self.w = w
        self.h = h
        self.ctrs = ctrs

    def __repr__(self):
        return f"Region({self.w}, {self.h}, {self.ctrs})"

def part1(input):

    lines = input.strip().split("\n")
    shapes = []

    SHAPE_SIZE = 3

    regions = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if "." in line or "#" in line:
            shape = []
            start = i
            while i < len(lines) and ('.' in lines[i] or '#' in lines[i]):
                for j, c in enumerate(lines[i]):
                    if(c == '#'):
                        shape.append( [i - start, j] )
                i+=1
            shapes.append(shape)
        if "x" in line:
            w = int(line.split("x")[0])
            h = int(line.split("x")[1].split(":")[0])
            ctrs = [int(c) for c in line.split(":")[1].strip().split(" ")]
            
            regions.append(Region(w, h, ctrs))

        i += 1

    print(shapes)
    print(regions)

    thresholds = [1.1, 1.25, 1.5, 2.0]
    ctrs = [0 for _ in range(len(thresholds))]

    for region in regions:
        area_reg = region.w * region.h
        area_shapes = 0
        for i, shape in enumerate(shapes):
            area_shapes += len(shape)*region.ctrs[i]
        
        ratio = area_reg / area_shapes
        for j, th in enumerate(thresholds):
            if ratio >= th:
                ctrs[j] += 1
    
    for j, th in enumerate(thresholds):
        print(f"t= {th}: {ctrs[j]}")


    return -1

def part2(input):
    # No part 2
    return "Part 2 result"

if part == "1":
    print(part1(input))
elif part == "2":
    print(part2(input))