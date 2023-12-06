#!/usr/bin/env python3
# -*-coding: utf-8 -*-
"""
Task:
Determine the number of ways you could beat the record in each race. 
What do you get if you multiply these numbers together?

Detailed description:
https://adventofcode.com/2023/day/6

The input file is available there:
https://adventofcode.com/2023/day/6/input

The code below assumes it has been saved locally.

There are 2 solutions implemented, runtime differs significantly for Part 2.

Naive approach:
Make the calculation depending on charging time, for each possibility, 
and count whatever is above the desired distance.

Informed approach:
Solve the quadratic inequality:

x (t - x) > d

where t is the time of the given race and d is the (previous record) distance.

and then we'll look for all x where this is true 
(the integer values inbetween the solution of the quadratic equation)

"""
from math import sqrt
import re
import time

# naive approach
def race(racetime, distance):
    goodrace_counter = 0
    for i in range(1, racetime):
        trav_dist = i * (racetime - i)
        if trav_dist > distance:
            goodrace_counter += 1
    return goodrace_counter


# alternatively: solving the problem with a quadratic inequality
def solve_quadr(a, b, c):
    res1 = (-b + sqrt(b*b - 4*a*c)) / (2*a)
    res2 = (-b - sqrt(b*b - 4*a*c)) / (2*a)
    
    # make sure the two results are sorted
    if res1 < res2:
        return res1, res2
    else:
        return res2, res1


def race_alt(racetime, distance):
    r1, r2 = solve_quadr(-1, racetime, -distance)
    # it has to be above the old record, so if the solution happens to be a whole number,
    # start from 1 value above
    if r1 == int(r1):
        r1 = r1 + 1
    return int(r2) - int(r1)


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

# with the same naive approach as for Part 1
start = time.time()
answer = race(racetime, dist_to_beat)
end = time.time()
print("Part 2 answer:", answer)
print("and it took", end-start, "seconds to calculate Part 2")

# with the quadratic formula
start = time.time()
answer = race_alt(racetime, dist_to_beat)
end = time.time()
print("or Part 2 answer:", answer)
print("and it took", end-start, "seconds to calculate with the help of maths (solving a quadratic inequality)")

