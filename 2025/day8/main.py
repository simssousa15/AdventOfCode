import sys
import math
from functools import singledispatch

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
        return f"x:{self.x} y:{self.y} z:{self.z}"

class Circuit:
    def __init__(self):
        self.boxes = []

    def add_box(self, box: JunctionBox):
        self.boxes.append(box)


###################################
@singledispatch
def dist(a, b) -> int:
    raise NotImplementedError(f"Unsupported type: {type(a)} and {type(b)}")

@dist.register
def dist(a: Coordinates, b: Coordinates) -> int:
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.z - b.z) ** 2)
@dist.register
def dist(a: Circuit, b: JunctionBox) -> int:
    return min(dist(box, b) for box in a.boxes)
@dist.register
def dist(a: JunctionBox, b: Circuit) -> int:
    return dist(b, a)
@dist.register
def dist(a: Circuit, b: Circuit) -> int:
    return min(dist(box_a, box_b) for box_a in a.boxes for box_b in b.boxes)
####################################

def part1(input):
    # Create List of Coordinates from input
    boxes = []
    for line in input.splitlines():
        x, y, z = map(int, line.split(","))
        boxes.append(Coordinates(x, y, z))
    

    return "Part 1 result"

def part2(input):
    
    return "Part 2 result"

if part == "1":
    print(part1(input))
elif part == "2":
    print(part2(input))