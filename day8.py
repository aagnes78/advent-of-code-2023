#!/usr/bin/env python3
# -*-coding: utf-8 -*-
"""
Day 8: Haunted Wasteland 

Task:
How many steps are required to reach ZZZ?

Detailed description:
https://adventofcode.com/2023/day/8

The input file is available there (login required)
https://adventofcode.com/2023/day/8/input

"""
import re
from numpy import lcm
from functools import reduce

# Part 1

def next_step(wherefrom, how):
    if how == "L":
        return nodes_dict[wherefrom][0]
    else:
        return nodes_dict[wherefrom][1]


def navigate(start, end, instructions, stepcounter):
    for i in range(len(instructions)):
        stepcounter += 1
        next_pos = next_step(start, instructions[i])
        
        if next_pos.endswith(end):
            return stepcounter
        else:
            start = next_pos
    if not next_pos.endswith(end):
        return navigate(next_pos, end, instructions, stepcounter)


file = open("day8-input.txt", "r")

instructions, allnodes = file.read().strip().split("\n\n")
file.close()

# the nodes of the network are listed in lines like:
# AAA = (BBB, CCC)
# GNK = (LBV, QNP)
nodes_dict = {}

nodes_lines = allnodes.split("\n")
for line in nodes_lines:
    # Part 2's small example also included digits
    nodes = re.findall(r"[A-Z0-9]{3}", line)
    nodes_dict[nodes[0]] = (nodes[1], nodes[2])

stepcount = navigate('AAA', 'ZZZ', instructions, 0)
print("Part 1 - number of steps to ZZZ:", stepcount)


# Part 2

# all nodes ending in 'A' will count as starting point, besides 'AAA'

start_list = []
for key in nodes_dict:
    if key.endswith("A"):
          start_list.append(key)
          
# Note: 
# Theoretically, Part 1's solution could be launched for all starting points parallelly,
# and check when they would all get into some 'Z' ending position at the same step.
# That would take too long, and there is really no need for it.

# All paths seem to step on a 'Z' node cyclically, 
# so the solution is to look for the least common multiple (lcm) of the path cycles
# (note to self: lkkt is lcm in English)

list_for_lcm = []

for item in start_list:
    arrives_at_z = navigate(item, 'Z', instructions, 0)
    #print("starting from", item, "arrived at Z after", arrives_at_z, "steps")
    list_for_lcm.append(arrives_at_z)

result = reduce(lcm, list_for_lcm)

print("Part 2 - number of steps until all nodes end on Z:", result)

