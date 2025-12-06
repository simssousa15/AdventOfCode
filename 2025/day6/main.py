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

def parser(line):
    vec = []
    tmp = ""
    for c in line:
        if c == " ":
            if tmp:
                vec.append(tmp)
            tmp = ""
        else:
            tmp += c
    if tmp:
        vec.append(tmp)
    return vec

def invert_dim(m):
    return list(map(list, zip(*m)))

def part1(input):
    lines = input.splitlines()
    parsed = [parser(line) for line in lines]
    inverted = invert_dim(parsed)   

    sum = 0
    for col in inverted:
        op = col[-1]
        res = int(col[0])
        for i in range(1, len(col)-1):
            if op == "+":
                res += int(col[i])
            elif op == "-":
                res -= int(col[i])
            elif op == "*":
                res *= int(col[i])
            elif op == "/":
                res //= int(col[i])
        sum += res
            
        
    return sum


def parser2(input):
    lines = input.splitlines()
    ops = []
    ops_idx = []
    for i, c in enumerate(lines[-1]):
        if c != " ":
            ops.append(c)
            ops_idx.append(i)
    
    nums = []
    for l in lines[:-1]:
        l_nums = []
        tmp = ""
        for i, c in enumerate(l):
            if i+1 in ops_idx:
                l_nums.append(tmp)
                tmp = ""
            else:
                tmp += c
        if tmp:
            l_nums.append(tmp)
        nums.append(l_nums)
        
    return (ops, invert_dim(nums))

def get_nums(lst):
    m = [[c for c in num] for num in lst] 
    inv_m = invert_dim(m)
    ints = [int("".join(i)) for i in reversed(inv_m)]
    return ints

def calc(num, op):
    ints = get_nums(num)
    res = ints[0]
    for i in range(1, len(ints)):
        if op == "+":
            res += ints[i]
        elif op == "-":
            res -= ints[i]
        elif op == "*":
            res *= ints[i]
        elif op == "/":
            res //= ints[i]
    return res

def part2(input):
    ops, nums = parser2(input)
    print (ops)
    print (nums)

    sum = 0
    for i, col in enumerate(nums):
        op = ops[i]
        res = calc(col, op)
        print(col,op, "->", res)
        sum += res
        
    return sum

if part == "1":
    print(part1(input))
elif part == "2":
    print(part2(input))