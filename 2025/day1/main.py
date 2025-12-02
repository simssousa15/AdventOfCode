import sys

if len(sys.argv) < 2:
    print("Usage: python main.py <filename>")
    sys.exit(1)

filename = sys.argv[1]


with open(filename, "r") as file:
    input = file.read()

lines = input.strip().split("\n")

pos = 50
ctr = 0
for line in lines:
    dir = 1 if line[0] == "R" else -1
    steps = int(line[1:])

    for i in range(steps):
        pos += dir

        if pos == 0:
            ctr+=1

        if pos == 100:
            pos = 0
            ctr += 1
        elif pos < 0:
            pos = 99

        
    
print(ctr)