import sys
import math
from dataclasses import dataclass
from typing import Set
import copy

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

@dataclass
class State:
    pos: str
    visited: Set[str]

    
def part1(input):
    connections = {}
    
    for line in input.splitlines():
        devices = line.split(" ")
        source = devices[0][:-1]
        connections[source] = [d for d in devices[1:]]
    print(connections)


    q = []
    tmp = set()
    tmp.add("you")
    q.append(State("you", tmp))
    print(q[0])

    ctr = 0
    while(q):
        st = q.pop(0)
        p = st.pos
        vis = st.visited
        
        assert p in connections
        for new_p in connections[p]:
            if(new_p == "out"):
                ctr+=1
            elif(new_p not in vis):
                tmp = vis.copy()
                tmp.add(new_p)
                q.append(State(new_p, tmp))
    

    return ctr






# Idea:
# Search from every starting point one step at a time
# When a starting point is finised register, none_ctr | dac_ctr | fft_ctr
# When a search reaches a finished starting point, finish it also 
# (could possible also check if the new end point in the visited)
def part2(input):
    
    connections = {}
    
    for line in input.splitlines():
        devices = line.split(" ")
        source = devices[0][:-1]
        connections[source] = [d for d in devices[1:]]
    # print(connections)

    class State2:
        def __init__(self, init_pos="svr"):
            self.pos = init_pos
            self.visited = set()
            self.dac = False
            self.fft = False
            self.visit(init_pos)
        
        def visit(self, pos):
            self.pos = pos
            self.visited.add(pos)
            self.dac = pos == "dac" or self.dac
            self.fft = pos == "fft" or self.fft
        
        def __repr__(self):
            return (f"State2(pos='{self.pos}', "
                    f"visited={self.visited}, "
                    f"dac={self.dac}, "
                    f"fft={self.fft})")

    class Search:
        def __init__(self, init_pos="svr"):
            self.q = [State2(init_pos)]
            self.both_ctr = 0
            self.dac_ctr = 0
            self.fft_ctr = 0
            self.none_ctr = 0
        
        def iter(self, done_map):
            new_q = []

            for st in self.q:
                p = st.pos
                vis = st.visited
                
                assert p in connections
                for new_p in connections[p]:
                    if(new_p in done_map):
                        res = done_map[new_p]

                        if(st.dac and st.fft):
                            self.both_ctr += res.none_ctr + res.both_ctr + res.dac_ctr + res.fft_ctr
                        elif(st.dac):
                            self.both_ctr += res.both_ctr + res.fft_ctr
                            self.dac_ctr += res.none_ctr
                        elif(st.fft):
                            self.both_ctr += res.both_ctr + res.dac_ctr
                            self.fft_ctr += res.none_ctr
                        elif(not st.dac and not st.fft):
                            self.both_ctr += res.both_ctr
                            self.dac_ctr += res.dac_ctr
                            self.fft_ctr += res.fft_ctr
                            self.none_ctr += res.none_ctr

                    elif(new_p == "out"):
                        if(st.dac and st.fft):
                            self.both_ctr +=1
                        elif(st.dac):
                            self.dac_ctr += 1
                        elif(st.fft):
                            self.fft_ctr += 1
                        elif(not st.dac and not st.fft):
                            self.none_ctr += 1

                    elif(new_p not in vis):
                        new_st = copy.deepcopy(st)
                        new_st.visit(new_p)
                        new_q.append(new_st)
            
            done = len(new_q) == 0
            self.q = new_q
            return done

    @dataclass
    class SearchRes:
        both_ctr: int
        dac_ctr: int
        fft_ctr: int
        none_ctr: int



    queues = {}
    for dev in connections.keys():
        queues[dev] = Search(init_pos=dev)
    
    done_map ={}


    while("svr" not in done_map):
        new_queues = {}
        for d, s in queues.items():
            if(s.iter(done_map)):
                res = SearchRes(s.both_ctr, s.dac_ctr, s.fft_ctr, s.none_ctr)
                done_map[d] = res
                print("Done with ", d, s.both_ctr, s.dac_ctr, s.fft_ctr, s.none_ctr)
            else:
                new_queues[d] = s
        queues = new_queues
        
    
    return done_map["svr"].both_ctr

if part == "1":
    print(part1(input))
elif part == "2":
    print(part2(input))