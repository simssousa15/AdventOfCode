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
    input_lines = input.splitlines()

    p1 = True
    ctr = 0
    ranges = []
    for line in input_lines:
        if line == "":
            p1 = False
            print("Ranges found, counting fresh...")
            continue
        
        if p1:
            # store ranges
            idx = line.index("-") 
            ranges.append((int(line[:idx]), int(line[idx+1:])))
            print(f"Added range: {ranges[-1]}")
        else:
            # count fresh
            num = int(line.strip())
            print(f"Checking number: {num}")
            for r in ranges:
                if r[0] <= num <= r[1]:
                    ctr += 1
                    break
    return ctr

def part2(input):

    input_lines = input.splitlines()

    ranges = []
    for line in input_lines:
        if line == "":
            print("Finished")
            break
        range_parts = line.split("-")
        start = int(range_parts[0])
        end = int(range_parts[1])
        print(f"Processing range: {start}-{end}")
        for r in ranges:
            if not (end < r[0] or start > r[1]):
                # overlapping ranges, merge
                start = min(start, r[0])
                end = max(end, r[1])
                print(f"Merging with existing range {r} to form {start}-{end}")
                ranges.remove(r)
        ranges.append((start, end))
    
    # Sum size of all ranges
    sum = 0
    for r in ranges:
        sum += (r[1] - r[0] + 1)
        print(f"Range {r} contributes {r[1] - r[0] + 1} to total")
    
    return sum

if part == "1":
    print(part1(input))
elif part == "2":
    print(part2(input))