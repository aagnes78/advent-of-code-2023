#!/usr/bin/env python3
# -*-coding: utf-8 -*-
"""
Task:
Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

Detailed description:
https://adventofcode.com/2023/day/1

The input file is available there:
https://adventofcode.com/2023/day/1/input

The code below assumes it has been saved locally.

Note that the Python re methods are designed for non-overlapping strings.

Note also for Part 2: there is no need to convert all number words to digits.

"""
import re

digitdict = {'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5',
             'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}

def convert_to_digit(text):
    """Converts written-out words for the corresponding digit, leaves digit input unchanged.
    Returns the digit as string.
    """
    if text in digitdict:
        text = digitdict[text]
    return text
    

def convert_to_num(s1, s2):
    """Converts two digits (input as either written-out word or digit) into 2-digit int.
    """
    return int(convert_to_digit(s1) + convert_to_digit(s2))


# Part 1

sum = 0

file = open("day1-input.txt", "r")
for line in file:
    line = line.strip()
    if re.search(r'\d', line):
        digits = re.findall(r"\d", line)
        sum += convert_to_num(digits[0], digits[-1])

file.close()

print("Part 1 - the sum of all calibration values:", sum)

# Part 2

sum = 0

# re matches non-overlapping substrings left-to-right
# twone -> two
regex_nums = "(\d|one|two|three|four|five|six|seven|eight|nine)"

# twone -> one
regex_nums_end = ".*(\d|one|two|three|four|five|six|seven|eight|nine).*$"

file = open("day1-input.txt", "r")
for line in file:
    line = line.strip()

    if re.search(regex_nums, line):
        # find the first and last number (word or digit) in the line
        firstdigit = re.findall(regex_nums, line)[0]
        lastdigit = re.findall(regex_nums_end, line)[-1]
        sum += convert_to_num(firstdigit, lastdigit)

print("Part 2 - the sum of all calibration values:", sum)

