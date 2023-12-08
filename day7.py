#!/usr/bin/env python3
# -*-coding: utf-8 -*-
"""
Day 7: Camel Cards

Task:
What are the total winnings?

Detailed description:
https://adventofcode.com/2023/day/7

The input file is available there (login required)
https://adventofcode.com/2023/day/7/input

"""
from collections import Counter
from functools import cmp_to_key

# for Part 1
def find_type(hand):
    counter = Counter(hand)
    if len(counter) == 1:          # five of a kind (counter values: 5)
        return 6
    elif len(counter) == 2:
        if 4 in counter.values():  # four of a kind (4,1)
            return 5
        else:                      # full house (3,2)
            return 4
    elif len(counter) == 3:
        if 3 in counter.values():  # three of a kind (3,1)
            return 3
        else:                      # two pair (2,2,1)
            return 2
    elif len(counter) == 4:        # one pair (2,1,1,1)
        return 1
    else:                          # high card (1,1,1,1,1)
        return 0


# for part 2
def find_type_withjoker(hand):
    origtype = find_type(hand)
    if 'J' not in hand:
        return origtype
    else:
        if origtype == 0:          # J turns one card into pair
            newtype = 1
        elif origtype == 1:        # J turns the one pair into 3 of a kind
            newtype = 3
        elif origtype == 2:
            j_count = Counter(hand)['J']
            if j_count == 1:       # J turns two pair into full house
                newtype = 4
            else:                  # JJ turns two pair into 4 of a kind
                newtype = 5
        elif origtype == 3:        # J (or JJJ) turns 3-of-a-kind into 4 of a kind
            newtype = 5
        else:                      # origtype is 4, 5 or 6 will be 6 (5 of a kind)
            newtype = 6
        return newtype


def getval_card(card, with_joker=False):
    cardvalues = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    if with_joker == True:
        cardvalues['J'] = 1
    if card.isdigit():
        return int(card)
    else:
        return cardvalues[card]


def cmp_cards(card1, card2, with_joker=False):
    val1, val2 = getval_card(card1, with_joker), getval_card(card2, with_joker)
    if val1 < val2:
        return -1
    elif val1 > val2:
        return 1
    else:
        return 0


def cmp_hands(hand1, hand2, with_joker=False):
    if hand1 == hand2:   # exact same hands
        return 0
    elif find_type(hand1) < find_type(hand2):
        return -1
    elif find_type(hand1) > find_type(hand2):
        return 1
    else:    # the types are equals, but the hands are not
        for i in range(5):    # hands are 5-char long string
            cmp = cmp_cards(hand1[i], hand2[i])
            if cmp != 0:
                return cmp


def cmp_hands_withjoker(hand1, hand2):
    if hand1 == hand2:   # exact same hands
        return 0
    elif find_type_withjoker(hand1) < find_type_withjoker(hand2):
        return -1
    elif find_type_withjoker(hand1) > find_type_withjoker(hand2):
        return 1
    else:    # the types are equals, but the hands are not
        for i in range(5):    # hands are 5-char long string
            ###cmp = cmp_cards_withjoker(hand1[i], hand2[i])
            cmp = cmp_cards(hand1[i], hand2[i], with_joker=True)
            if cmp != 0:
                return cmp


cardsdict = {}
file = open("day7-input.txt", "r")

for line in file:
    if len(line) > 1:
        hand, bid = line.strip().split()
        if hand in cardsdict:
            # note: there was none in the input
            print("OHOHOHOOO", hand, bid)
            raise KeyError("duplicate key")
        else:
            cardsdict[hand] = int(bid)

hands_sortedlist = sorted(cardsdict, key=(cmp_to_key(cmp_hands)))

winnings = 0
for index, card in enumerate(hands_sortedlist):
    winnings += (index+1) * cardsdict[card]

print("Part 1 - the total winnings:", winnings)

# Part 2
hands_sortedlist_p2 = sorted(cardsdict, key=(cmp_to_key(cmp_hands_withjoker)))

winnings_p2 = 0
for index, card in enumerate(hands_sortedlist_p2):
    winnings_p2 += (index+1) * cardsdict[card]

print("Part 2 with jokers - the total winnings:", winnings_p2)

