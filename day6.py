#!/usr/bin/env python3
# -*-coding: utf-8 -*-
"""
Day 6: Wait For It

Task:
Determine the number of ways you could beat the record in each race. 
What do you get if you multiply these numbers together?

Detailed description:
https://adventofcode.com/2023/day/6

The input file is available there:
https://adventofcode.com/2023/day/6/input

The code below assumes it has been saved locally.

"""
import re
import time

def race(racetime, distance):
    goodrace_counter = 0
    for i in range(1, racetime):
        trav_dist = i * (racetime - i)
        if trav_dist > distance:
            goodrace_counter += 1
    return goodrace_counter

file = open("day6-input.txt", "r")

timesline, dists_line = file.read().split("\n")[:2]

racetimes = [int(x) for x in re.findall(r"\d+", timesline)]
dists_to_beat = [int(x) for x in re.findall(r"\d+", dists_line)]

answer = 1
race_zip = zip(racetimes, dists_to_beat)
for item in race_zip:
    answer *= race(item[0],item[1])

print("Part 1 answer:", answer)

# Part 2
# input line is not understood as a list of numbers but 1 number with stray spaces
racetime = int("".join(re.findall(r"\d+", timesline)))
dist_to_beat = int("".join(re.findall(r"\d+", dists_line)))

start = time.time()
answer = race(racetime, dist_to_beat)
end = time.time()
print("Part 2 answer:", answer)
print("and it took", end-start, "seconds to calculate Part 2")

