import sys
import math
import copy
from collections import deque

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

class Region:
    def __init__(self, w, h, ctrs):
        self.w = w
        self.h = h
        self.ctrs = ctrs

    def __repr__(self):
        return f"Region({self.w}, {self.h}, {self.ctrs})"

class queueItem:
    def __init__(self, reg_map, updated_ctrs):
        self.reg_map = reg_map
        self.updated_ctrs = updated_ctrs

def part1(input):
    lines = input.strip().split("\n")
    shapes = []

    SHAPE_SIZE = 3

    regions = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if "." in line or "#" in line:
            shape = []
            start = i
            while i < len(lines) and ('.' in lines[i] or '#' in lines[i]):
                for j, c in enumerate(lines[i]):
                    if(c == '#'):
                        shape.append( [i - start, j] )
                i+=1
            shapes.append(shape)
        if "x" in line:
            w = int(line.split("x")[0])
            h = int(line.split("x")[1].split(":")[0])
            ctrs = [int(c) for c in line.split(":")[1].strip().split(" ")]
            
            regions.append(Region(w, h, ctrs))

        i += 1

    print(shapes)
    print(regions)

    directions = [
        (1,1), # normal direction
        (1,-1), # inverted x axis
        (-1,1), # inverted y axis
        (-1,-1) # inverted xy axis
    ]

    valid_region_ctr = 0
    for reg_nb, reg in enumerate(regions): # R
        print(f"[START] Region {reg_nb+1}/{len(regions)} - {reg}")
        dq = deque()
        reg_map = [['.' for i in range(reg.w)] for j in range(reg.h)]
        it = queueItem(reg_map, reg.ctrs)
        dq.append(it)

        sol_found = False
        itr_ctr = 0
        while(len(dq)):
            itr_ctr += 1

            if(itr_ctr%1000 == 0):
                print("itr_nb=", itr_ctr)

            it = dq.pop()
            
            curr_idx = -1
            for j, ctr in enumerate(it.updated_ctrs):
                if ctr!=0:
                    curr_idx = j
                    break

            if(curr_idx==-1):
                sol_found = True
                break

            shape = shapes[curr_idx]

            it.updated_ctrs[curr_idx] -=1

            for is_rotated in [False, True]:
                for dir in directions: # 4 directions
                    # Get the shape into the desired direction
                    dir_shape = shape.copy()
                    if(dir[0] == -1):
                        for u in dir_shape:
                            u[0] = SHAPE_SIZE - u[0]
                    if(dir[1] == -1):
                        for u in dir_shape:
                            u[1] = SHAPE_SIZE -u[1]
                    if(is_rotated):
                        for u in dir_shape:
                            u[0], u[1] = u[1], u[0]

                    assert reg.h == len(it.reg_map)
                    assert reg.w == len(it.reg_map[0])

                    for start_x in range(reg.w): # W
                        valid = True
                        for u in dir_shape:
                            if(start_x+u[0] >= reg.w):
                                valid= False
                                break
                        if(not valid):
                            break

                        for start_y in range(reg.h):# H
                            for u in dir_shape:
                                if(start_y+u[1] >= reg.h):
                                    valid= False
                                    break
                            if(not valid):
                                break

                            # both valid. Place present and put in queue
                            tmp_map = copy.deepcopy(it.reg_map)
                            for u in dir_shape:
                                if(tmp_map[start_y+u[1]][start_x+u[0]] != "."):
                                    #already occupied
                                    valid = False
                                    break
                                tmp_map[start_y+u[1]][start_x+u[0]] = "#"
                            
                            if(valid):
                                # print("New map :O", tmp_map)
                                dq.append(queueItem(tmp_map, copy.copy(it.updated_ctrs)))
            
        region_valid = sol_found
        if(region_valid):
            print("Region is valid")
            valid_region_ctr += 1
        else:
            print("Region is NOT valid")

        print(f"[END] Region {reg_nb+1}/{len(regions)} - {reg}")







    # BFS - clearly not a good idea
    # we want to find ANY solution has soon as possible
    # for reg_nb, reg in enumerate(regions): # R
    #     print(f"[START] Region {reg_nb+1}/{len(regions)} - {reg}")
    #     q = []
    #     reg_map = [['.' for i in range(reg.w)] for j in range(reg.h)]
    #     q.append(reg_map)


    #     for j, ctr in enumerate(reg.ctrs): # 5 shapes
    #         if(ctr == 0):
    #             print(f"Shape: {j}, Ctr:{0}/{ctr} -> QueueSize: {len(q)}")

    #         shape = shapes[j]
    #         for i in range(ctr): # N
    #             new_q = []

    #             while(len(q)):
    #                 itr_map = q[0]
    #                 q.pop(0)

    #                 for dir in directions: # 4 directions
    #                     # Get the shape into the desired direction
    #                     dir_shape = shape.copy()
    #                     if(dir[0] == -1):
    #                         for u in dir_shape:
    #                             u[0] = SHAPE_SIZE - u[0]
    #                     if(dir[1] == -1):
    #                         for u in dir_shape:
    #                             u[1] = SHAPE_SIZE -u[1]

    #                     assert reg.h == len(itr_map)
    #                     assert reg.w == len(itr_map[0])

    #                     for start_x in range(reg.w): # W
    #                         valid = True
    #                         for u in dir_shape:
    #                             if(start_x+u[0] >= reg.w):
    #                                 valid= False
    #                                 break
    #                         if(not valid):
    #                             break

    #                         for start_y in range(reg.h):# H
    #                             for u in dir_shape:
    #                                 if(start_y+u[1] >= reg.h):
    #                                     valid= False
    #                                     break
    #                             if(not valid):
    #                                 break

    #                             # both valid. Place present and put in queue
    #                             tmp_map = copy.deepcopy(itr_map)
    #                             for u in dir_shape:
    #                                 if(tmp_map[start_y+u[1]][start_x+u[0]] != "."):
    #                                     #already occupied
    #                                     valid = False
    #                                     break
    #                                 tmp_map[start_y+u[1]][start_x+u[0]] = "#"
                                
    #                             if(valid):
    #                                 # print("New map :O", tmp_map)
    #                                 new_q.append(tmp_map)

    #             q = new_q
    #             new_q = []
    #             print(f"Shape: {j}, Ctr:{i+1}/{ctr} -> QueueSize: {len(q)}")
    #             if(len(q) == 0):
    #                 break
    #         if(len(q) == 0):
    #                 print("Impossible. len(q) == 0.")
    #                 break
        
    #     region_valid = len(q) > 0
    #     if(region_valid):
    #         print("Region is valid")
    #         valid_region_ctr += 1
    #     else:
    #         print("Region is NOT valid")

    #     print(f"[END] Region {reg_nb+1}/{len(regions)} - {reg}")

    return valid_region_ctr

def part2(input):
    
    return "Part 2 result"

if part == "1":
    print(part1(input))
elif part == "2":
    print(part2(input))