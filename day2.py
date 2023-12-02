#!/usr/bin/env python3
# -*-coding: utf-8 -*-
"""
Day 2: Cube Conundrum

Task:
The Elf would first like to know which games would have been possible 
if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

What is the sum of the IDs of those (i.e. the possible) games?

Detailed description:
https://adventofcode.com/2023/day/2

The input file is available there:
https://adventofcode.com/2023/day/2/input

The code below assumes it has been saved locally.
"""

import re


def colour_checker(colour, colournum, text):
    """Checking whether a game log is possible for a given colour
    """
    res = re.findall(r"(\d+)\s+" + colour, text)
    for c in res:
        if int(c) > colournum:
            return False
    return True


def colour_checker_all(text):
    """Checking for all colours whether a game log is possible.
    Possible: if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes.
    """
    if (colour_checker("red", 12, text) and colour_checker("green", 13, text) 
        and colour_checker("blue", 14, text)):
        return True
    return False


def colour_checker_part2(colour, text):
    """Find the max value in the game log for a given colour.    
    """
    res = re.findall(r"(\d+)\s+" + colour, text)
    resnums = [int(c) for c in res]
    return max(resnums)


game_id_sum = 0

fin = open("day2-input.txt", "r")

for line in fin:
    # if there's a newline EOF and not strip()-ing the line
    # then the "empty line" would include the newline, with 1 as length
    if len(line) > 1:
        game_id, line = line.split(":")
        game_id_no = int(re.findall(r"\d+", game_id)[0])
        if colour_checker_all(line):
            game_id_sum += game_id_no

fin.close()
        
print("Part 1 - the sum of the IDs of the possible games:", game_id_sum)

# Part 2

cube_powers = 0

fin = open("day2-input.txt", "r")

for line in fin:
    if len(line) > 1:
        cube_power = colour_checker_part2("red", line) * colour_checker_part2("green", line) * colour_checker_part2("blue", line)
        cube_powers += cube_power
        
print("Part 2: the sum of cube powers:", cube_powers)

