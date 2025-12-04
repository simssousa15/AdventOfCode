import sys

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
    input = input.strip().splitlines()

    ctr = 0
    for i in range(len(input)):
        for j in range(len(input)):
            if input[i][j] == "@":
                near = 0
                for d in eight_dir:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < len(input) and 0 <= nj < len(input):
                        if input[ni][nj] == "@":
                            near += 1
                    if near >= 4:
                        break
                if near < 4:
                    ctr += 1

    return ctr

def part2(input):
    input = input.strip().splitlines()

    total_ctr = 0
    ctr = -1
    while ctr != 0:
        ctr = 0
        for i in range(len(input)):
            for j in range(len(input)):
                if input[i][j] == "@":
                    near = 0
                    for d in eight_dir:
                        ni, nj = i + d[0], j + d[1]
                        if 0 <= ni < len(input) and 0 <= nj < len(input):
                            if input[ni][nj] == "@":
                                near += 1
                        if near >= 4:
                            break
                    if near < 4:
                        ctr += 1
                        input[i] = input[i][:j] + "x" + input[i][j+1:]
        total_ctr += ctr
        print(f"Round complete, {ctr} changes")
    
    return total_ctr

if part == "1":
    print(part1(input))
elif part == "2":
    print(part2(input))
