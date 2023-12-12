#!/usr/bin/env python3
# -*-coding: utf-8 -*-
"""
Day 10: Pipe Maze

Task:
How many steps along the loop does it take to get from the starting position to the point farthest from the starting position?

Detailed description:
https://adventofcode.com/2023/day/10

The input file is available there (login required)
https://adventofcode.com/2023/day/10/input

Notes:
For the AoC challenge you can have a look into the inputfile.

This means, you can look at the the position of the 'S' in the input, 
decide which direction to start to, before launching the path finder.

Currently:
Part 1 is implemented, the answer is complete and correct (tested for my given input).

For Part 2:
As a first step the loop is drawn, and written into an output file.

"""
import numpy as np

def is_tile(row, col, size):
    """Checking the validity of coordinates in the grid, to avoid triggering IndexError, where called.
    """
    return ( 0 <= row < size and 0 <= col < size )


def next_tile(prevrow, prevcol, currrow, currcol):
    """Find the next tile the path is leading to, keeping in mind the previous position,
          to keep moving forward, avoid turning back to where we came from.
    """
    global step_dict
    direction = grid[currrow,currcol]
    nextrow = currrow + step_dict[direction][0][0]
    nextcol = currcol + step_dict[direction][0][1]
    if ((not is_tile(nextrow, nextcol, size)) or (nextrow == prevrow and nextcol == prevcol)):
        nextrow = currrow + step_dict[direction][1][0]
        nextcol = currcol + step_dict[direction][1][1]
    return nextrow, nextcol



step_dict = {'|': [(-1, 0), (1, 0)], '-': [(0, -1), (0, 1)], 
                 'L': [(-1, 0), (0, 1)], 'J': [(0, -1), (-1, 0)], 
                 '7': [(0, -1), (1, 0)], 'F': [(0, 1), (1, 0)]}



with open("day10-input2.txt", "r") as file:
    grid = np.array([*map(list, [*map(str.strip, file.readlines())])])


# could search the grid matrix, or just look at the input file
size = 140
# start at the position of "S"
prevrow, prevcol = 82, 74
# pick which way to start
currrow, currcol = 83, 74  

# this is for Part 2
# or for me to see what the walked loop looks like (for Part 2) 

gridlog = np.full((size, size), "O")

gridlog[prevrow, prevcol] = grid[prevrow, prevcol]
gridlog[currrow, currcol] = grid[currrow, currcol]

# 1 step is already taken. Then we go until we get back to 'S'.
allstepcount = 1
while grid[currrow, currcol] != "S":
    nextrow, nextcol = next_tile(prevrow, prevcol, currrow, currcol)
    gridlog[currrow, currcol] = grid[currrow, currcol]
    allstepcount += 1
    prevrow, prevcol = currrow, currcol
    currrow, currcol = nextrow, nextcol

if allstepcount % 2 == 0:
    result = allstepcount//2
else:
    result = allstepcount//2 + 1

print("Part 1 - the farthest point is", result, "steps away.")

with open("day10-gridlog.txt", "w") as file2:
    for row in range(size):
        file2.write("".join(gridlog[row]) + "\n")

