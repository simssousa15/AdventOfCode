import sys
import math
import shapely

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

def part1(input):
    # Parse input
    points = []
    for line in input.splitlines():
        strs = line.split(",")
        points.append((int(strs[0]),int(strs[1])))
    
    res = -1
    for i in range(len(points)):
        p1 = points[i]
        for j in range(i, len(points)):
            p2 = points[j]
            length = abs(p2[0] - p1[0]) + 1
            width =  abs(p2[1] - p1[1]) + 1
            area = length * width
            res = max(res, area)
    
    return res

def part2(input):
    # Parse input
    points = []
    for line in input.splitlines():
        strs = line.split(",")
        points.append((int(strs[0]),int(strs[1])))
    
    polygon = shapely.Polygon(points)
    shapely.prepare(polygon)

    res = -1
    for i in range(len(points)):
        p1 = points[i]
        for j in range(i, len(points)):
            p2 = points[j]
            length = abs(p2[0] - p1[0]) + 1
            width =  abs(p2[1] - p1[1]) + 1
            area = length * width
            if polygon.covers(shapely.box(p1[0], p1[1], p2[0], p2[1])):
                res = max(res, area)

    return res

if part == "1":
    print(part1(input))
elif part == "2":
    print(part2(input))