import sys

if len(sys.argv) < 2:
    print("Usage: python main.py <filename>")
    sys.exit(1)

filename = sys.argv[1]


with open(filename, "r") as file:
    input = file.read()

ranges = [ i.split("-") for i in input.replace("\n", "").split(",")]

# print(ranges)

sum = 0

for r in ranges:
    r_start = int(r[0])
    r_end = int(r[1])

    for i in range(r_start, r_end + 1):
        i_str = str(i)
        for repeated_len in range(1, len(i_str)//2 + 1):
            reps = len(i_str) // repeated_len
            sub_str = i_str[:repeated_len]
            if sub_str * reps == i_str:
                print("found ", i)
                sum += i
                break

print(sum)
