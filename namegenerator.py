#!/usr/bin/python3

"""
   Generate names using Markov Chains
   The transition matrix created from
   a list of existing names read from
   a file.
"""

import sys
import random

transition = dict()
letters = set()

for i in open(sys.argv[1]):
    name = i.rstrip()
    for j in range(1,len(name)):
        pch = name[j-1]
        ch = name[j]
        if pch not in transition:
            transition[pch] = dict()
        if ch not in transition[pch]:
            transition[pch][ch] = 0
        transition[pch][ch] += 1
        letters.add(pch)

# Calculate probabilities

for ch1 in transition:
    s = 0
    for ch2 in transition[ch1]:
        s += transition[ch1][ch2]
    for ch2 in transition[ch1]:
        transition[ch1][ch2] = float(transition[ch1][ch2]) / s

# Generate names
letters = list(letters)
ch1 = letters[random.randint(0, len(letters)-1)]
name = ch1
for i in range(5):
    r = random.random()
    s = 0.0
    if ch1 not in transition:
        break
    for ch2 in transition[ch1]:
        s += transition[ch1][ch2]
        if r < s:
            ch1 = ch2
            name = name + ch2
            break
print(name)
