#!/usr/bin/env python3
# -*-coding: utf-8 -*-
"""
Day 4: Scratchcards

Task:
How many points are they worth in total?

Part 2:
How many total scratchcards do you end up with?

Detailed description:
https://adventofcode.com/2023/day/4

The input file is available there:
https://adventofcode.com/2023/day/4/input

The code below assumes it has been saved locally.

"""
import re
from collections import defaultdict

# for part 1
winsum = 0
# for part 2
scratchdict = defaultdict(int)

fin = open("day4-input.txt", "r")
for line in fin:
    card_has_wins = 0
    if len(line) > 1:
        # for part 2
        card_no = int(re.findall("Card\s+(\d+)", line)[0])
        scratchdict[card_no] += 1

        # for both parts
        line = line.split(":")[1]
        winning_part, my_part = line.split("|")
        winning_numbers = re.findall("\d+", winning_part)
        my_numbers = re.findall("\d+", my_part)
        
        for num in winning_numbers:
            if num in my_numbers:
                card_has_wins += 1
    if card_has_wins > 0:
        # part 1
        winsum += 2 ** (card_has_wins-1)
        
        # part 2
        for i in range(card_has_wins):
            scratchdict[card_no+i+1] += scratchdict[card_no]

print("Part 1 - The scratchcards bring", winsum, "points.")

total_cards = 0
for k, v in scratchdict.items():
    total_cards += v

print("Part 2 - The number of total scratchcards you end up with:", total_cards)

