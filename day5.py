#!/usr/bin/env python3
# -*-coding: utf-8 -*-
"""
Day 5: If You Give A Seed A Fertilizer

Task:
What is the lowest location number that corresponds to any of the initial seed numbers?

Detailed description:
https://adventofcode.com/2023/day/5

The input file is available there:
https://adventofcode.com/2023/day/5/input

The code below assumes it has been saved locally.

"""
import re

def is_inrange(what, start, length):
    return (start <= what < start+length)

# for Part 1
def mapper(what, where):
    for i in range(len(where)):
        if is_inrange(what, where[i][1], where[i][2]):
            return where[i][0] + what - where[i][1]
    return what


def mapper_chain(item):
    for m in range(7):
        item = mapper(item, mappings[m])
    return item


# for Part 2
def inverse_mapper(what, where):
    for i in range(len(where)):
        if is_inrange(what, where[i][0], where[i][2]):
            return where[i][1] + what - where[i][0]
    return what


def inverse_mapper_chain(item):
    for m in range(7):
         item = inverse_mapper(item, mappings[6-m])
    return item


def is_seed(what):
    for i in range(0, len(seeds), 2):
        if what in range(seeds[i], seeds[i]+seeds[i+1], 1):
            return True
    return False


file = open("day5-input.txt", "r")

blocks = file.read().strip().split("\n\n")
file.close()

# seeds: all the numbers in the first line in a list
# Part 1: individually, Part 2: ranges - see later
seeds = list(map(int, re.findall("\d+", blocks[0])))

# there are 7 mappings, from seed-to-soil to humidity-to-location
mappings = []

for m in range(1, 8):
    mappings.append([list(map(int, re.findall("\d+", inside))) for inside in blocks[m].split("\n")[1:]])


# I just chose a number that seemed large enough to start out from
min_location =	100000000000

for seed in seeds:
    location = mapper_chain(seed)
    min_location = min(location, min_location)

print("Part 1 - The lowest possible location number:", min_location)

# Part 2: 
# The naive strategy of Part 1 would also work in theory, but takes way too long time.
# So, solving this with reverse lookup:
# i.e. starting from lowest location 0 to find the first one that is possible to get to
#   from an existing seed
# Note: it may take several minutes, but still much quicker than naive approach

location = 0
found = False
while not found:
    poss_seed = inverse_mapper_chain(location)
    if is_seed(poss_seed):
        print("Part 2 - the best location:", location)
        found = True
    location += 1

