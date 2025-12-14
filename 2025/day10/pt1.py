import sys
import math

four_dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
diag = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
eight_dir = four_dir + diag

if len(sys.argv) < 2:
    print("Usage: python main.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "r") as file:
    input = file.read()

class State:
    def __init__(self, indicators, presses):
        self.ind = indicators
        self.pre = presses

def min_presses(indicators, buttons):

    ind = [ i == '.' for i in indicators]

    q = []
    init = State(ind, 0)
    q.append(init)

    # very simple to avoid repeated states of indicators
    # to be implemented later
    registry = set()
    while q:
        
        st = q.pop(0)
        for but in buttons:
            new_ind = st.ind.copy()
            new_pre = st.pre + 1

            for b in but:
                new_ind[b] = not new_ind[b]

            if(all(new_ind)):
                return new_pre
            elif(str(new_ind) not in registry):
                q.append(State(new_ind, new_pre))
                registry.add(str(new_ind))
    assert False
            


def main(input):
    lines = input.splitlines()
    lines_parsed = [l.split(" ") for l in lines]

    ind = []
    but = []
    jolt = []
    for lin in lines_parsed:
        tmp_but = []
        for block in lin:
            if block[0] == "[": # indicator light
                ind.append(block[1:-1])
            elif block[0] == "(": # button wiring schematics
                tmp_but.append([int(i) for i in block[1:-1].split(",")])
            elif block[0] == "{": # joltage requirements
                jolt.append([int(i) for i in block[1:-1].split(",")])
        but.append(tmp_but)
    
    print(ind)
    print(but)
    print(jolt)
    
    sum = 0
    for i in range(len(ind)):
        press = min_presses(ind[i], but[i])
        print(i, " - ", press)
        sum += press

    return sum

print(main(input))