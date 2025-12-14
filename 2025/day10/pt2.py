import sys
import math

four_dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
diag = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
eight_dir = four_dir + diag

if len(sys.argv) < 2:
    print("Usage: python main.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

if len(sys.argv) < 2:
    print("Usage: python main.py <part_nb> <filename>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "r") as file:
    input = file.read()

class State:
    def __init__(self, indicators, presses):
        self.ind = indicators
        self.pre = presses

# Search algorithm will always be too ineficient
# def legacy_min_presses(jolt, buttons):
#     q = []
#     init = State([0 for _ in jolt], 0)
#     q.append(init)

#     # very simple to avoid repeated states of indicators
#     # to be implemented later
#     registry = set()
#     while q:
#         # if(len(q)%100==0):
#         #     print(len(q))

#         st = q.pop(0)
#         for but in buttons:
#             new_ind = st.ind.copy()
#             new_pre = st.pre + 1

#             cont = False
#             for b in but:
#                 if(new_ind[b] == jolt[b]):
#                     cont = True
#                     break
#                 new_ind[b] += 1
#             if(cont):
#                 continue

#             if( new_ind == jolt ):
#                 return new_pre
#             elif(str(new_ind) not in registry):
#                 q.append(State(new_ind, new_pre))
#                 registry.add(str(new_ind))
#     assert False

# Key to this problem is recognizing this a well-know solved 
# Linear Programming problem and structuring it as such
# 
# Template:
# 
# minmize       x1 + ... + xn
# subject to    x1v1 + ... + xnvn = N
#               x1, ..., xn >= 0
#               xn ∈ N0​
#
#              < = >
#
# minmize       1^T c
# subject to    Ac = N
#               c ∈ N0​

import numpy as np
import pulp
def min_presses(jolt, buttons):

    # Build N
    N = np.array(jolt)          # shape (m,)

    # Build A
    m = len(jolt)               # dimension of vectors
    n = len(buttons)            # number of vectors
    A = np.zeros((m, n))        # m x n

    for i, btn in enumerate(buttons):
        A[btn, i] = 1           # set components in column i

    # Define MILP
    prob = pulp.LpProblem("MinPresses", pulp.LpMinimize)

    # Variables: integers ≥ 0
    x_vars = [pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(n)]

    # Objective: minimize sum of presses
    prob += pulp.lpSum(x_vars)

    # Constraints: A @ x == N
    for row in range(m):
        prob += pulp.lpSum(A[row, j] * x_vars[j] for j in range(n)) == N[row]

    # Solve
    status = prob.solve(pulp.PULP_CBC_CMD(msg=False))

    if pulp.LpStatus[status] != "Optimal":
        raise RuntimeError("No feasible integer solution")

    # Get solution as NumPy array
    x = np.array([x_vars[j].varValue for j in range(n)], dtype=int)
    return x.sum()


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
        press = min_presses(jolt[i], but[i])
        print(i, " - ", press)
        sum += press

    return sum

print(main(input))