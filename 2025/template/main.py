import sys

if len(sys.argv) < 2:
    print("Usage: python main.py <filename>")
    sys.exit(1)

filename = sys.argv[1]


with open(filename, "r") as file:
    input = file.read()
