#!/usr/bin/python3

# Quick trio checker
# Nothing fancy, just a quiclky implemented logic

import sys
import re

def same(A, B):
    if A[0] == B[0] and A[1] == B[1]:
        return True
    return False

tab = open(sys.argv[1])
header = tab.readline().rstrip().split("\t")
delim = re.compile("[/|]")

for i in tab:
    fields = i.rstrip().split("\t")
    gt = list()
    for j in range(2,len(fields)):
        gt.append(delim.split(fields[j]))
    if same(gt[2], gt[3]) and gt[2][1] != '0' and gt[2][1] != '.': # there is a mutation same in the two sick
        if gt[4][1] == '0' or gt[4][1] == '.': # grandma should contain some mutation
            continue
        for j in [0,1,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20]:
            if same(gt[2], gt[j]):
                break
        else:
            print(i.rstrip())
