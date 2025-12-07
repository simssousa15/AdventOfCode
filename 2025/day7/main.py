import sys
from collections import deque

class UniqueQueue:
    def __init__(self):
        self.queue = deque()
        self.set = set()

    def push(self, item):
        if item not in self.set:
            self.queue.append(item)
            self.set.add(item)

    def pop(self):
        item = self.queue.popleft()
        self.set.remove(item)
        return item

    def __len__(self):
        return len(self.queue)


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

def find_start(maptrix):
    for i, row in enumerate(maptrix):
        for j, val in enumerate(row):
            if val == "S":
                return (i, j)
    return None

def part1(input):
    maptrix = [list(line) for line in input.splitlines()]
    i_srt, j_strt = find_start(maptrix)
    if i_srt is None:
        return "Start position not found"

    q = UniqueQueue()
    q.push((i_srt, j_strt))
    split_ctr = 0
    while q:
        i, j = q.pop()
        # Process current position (i, j)
        ni, nj = i + 1, j # downwards
        if 0 <= ni < len(maptrix) and 0 <= nj < len(maptrix[0]):
            if maptrix[ni][nj] == '^':  # Split happens
                q.push((ni, nj + 1))  # right
                q.push((ni, nj - 1))  # left
                split_ctr += 1
                # Note: check for bounds will be made when popping
            elif maptrix[ni][nj] == '.':
                q.push((ni, nj))  # continue downwards
            else:
                # Unexpected character, handle accordingly
                print(f"Unexpected character at ({ni}, {nj}): {maptrix[ni][nj]}")
    
    return split_ctr

def part2(input):
    maptrix = [list(line) for line in input.splitlines()]
    i_srt, j_strt = find_start(maptrix)
    if i_srt is None:
        return "Start position not found"

    q = UniqueQueue()
    q.push((i_srt, j_strt))

    tlns = {}
    tlns[(i_srt, j_strt)] = 1

    timeline = 0
    while q:
        # print(len(q))
        i, j = q.pop()
        # Process current position (i, j)
        ni, nj = i + 1, j # downwards
        if 0 <= ni < len(maptrix) and 0 <= nj < len(maptrix[0]):
            if maptrix[ni][nj] == '^':  # Split happens - new timeline
                q.push((ni, nj + 1))  # right
                tlns[(ni, nj + 1)] = tlns.get((ni, nj + 1), 0) + tlns[(i, j)]
                q.push((ni, nj - 1))  # left
                tlns[(ni, nj - 1)] = tlns.get((ni, nj - 1), 0) + tlns[(i, j)]
                # Note: check for bounds will be made when popping
            elif maptrix[ni][nj] == '.':
                q.push((ni, nj))  # continue downwards
                tlns[(ni, nj)] = tlns.get((ni, nj), 0) +  tlns[(i, j)]
            else:
                # Unexpected character, handle accordingly
                print(f"Unexpected character at ({ni}, {nj}): {maptrix[ni][nj]}")
        else:
            # Reached the edges of the map
            timeline += tlns[(i, j)]
    
    return timeline

if part == "1":
    print(part1(input))
elif part == "2":
    print(part2(input))