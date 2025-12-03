import sys

if len(sys.argv) < 2:
    print("Usage: python main.py <filename>")
    sys.exit(1)

filename = sys.argv[1]


with open(filename, "r") as file:
    input = file.read()

lines = input.splitlines()

sum = 0
battery_size = 12
for line in lines:
    d = ""
    idx = 0
    while len(d) < battery_size:
        end_idx = min(len(line)-(battery_size - len(d) - 1), len(line))
        sub_line = line[idx:end_idx]
        # print(sub_line, idx, end_idx)
        idx = sub_line.index(max(sub_line)) + idx + 1
        d += max(sub_line)
        # print(d, idx)

        

    print("found ", int(d), len(d)==battery_size)
    sum += int(d)

print(sum)