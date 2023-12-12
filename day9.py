#!/usr/bin/env python3
# -*-coding: utf-8 -*-
"""
Day 9: Mirage Maintenance

Task:
What is the sum of these extrapolated values?

Detailed description:
https://adventofcode.com/2023/day/9

The input file is available there (login required)
https://adventofcode.com/2023/day/9/input

"""
import re

def sum_last_elements(list_of_list):
    """Returns the sum of the last elements of the inside lists, in a list of list.
    
    Input: List of lists, not necessarily a well-formed matrix.
    """
    sum = 0
    for i in range(len(list_of_list)):
        sum += list_of_list[i][-1]
    return sum


def extrapolate(inputlist):
    biglist = list([inputlist])
    row = 0
    while any(x != 0 for x in biglist[row] ):
        biglist.append([biglist[row][i]-biglist[row][i-1] for i in range(1, len(biglist[row]))])
        row += 1
    return sum_last_elements(biglist)


# Part 1

history = []

with open("day9-input.txt", "r") as file: 
    lines = file.readlines()
    for line in lines:
        history.append([int(x) for x in re.findall("[-]?\d+", line)])

histsum = 0            
for line in history:
    histsum += extrapolate(line)

print("Part 1 - the sum of these extrapolated values:", histsum)

# Part 2 : getting the preceding element for each line by:
# reversing each line and use Part 1's extrapolate to get the next element there

history = []
with open("day9-input.txt", "r") as file: 
    lines = file.readlines()
    for line in lines:
        rev_line = [int(x) for x in re.findall("[-]?\d+", line)]
        rev_line.reverse()
        history.append(rev_line)

histsum_p2 = 0            
for line in history:
    histsum_p2 += extrapolate(line)

print("Part 2 - the sum of these extrapolated values:", histsum_p2)

