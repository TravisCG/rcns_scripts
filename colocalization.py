#!/usr/bin/python3

import sys

def countpeaks(exp):
    num = 0
    for chrx in exp:
        num += len(exp[chrx])
    return num

def overlap(regio, array, lowindex, hiindex):
    if regio[1] < array[lowindex][0] or regio[0] > array[hiindex][1]:
        return False
    if hiindex - lowindex < 2:
        if regio[1] > array[lowindex][0] and regio[0] < array[lowindex][1]:
            return True
        if regio[1] > array[hiindex][0] and regio[0] < array[hiindex][1]:
            return True
        return False
    mid = lowindex + int((hiindex - lowindex) / 2)
    if regio[1] > array[lowindex][0] and regio[0] < array[mid][1]:
        return overlap(regio, array, lowindex, mid)
    if regio[1] > array[mid][0] and regio[0] < array[hiindex][1]:
        return overlap(regio, array, mid, hiindex)

table = open(sys.argv[1])
table.readline()

experiment = dict()
allexp = set()

for i in table:
    fields = i.rstrip().split("\t")
    chrx   = fields[0]
    start  = int(fields[1])
    end    = int(fields[2])
    expid  = fields[3]
    allexp.add(expid)
    if expid not in experiment:
        experiment[expid] = dict()
    if chrx not in experiment[expid]:
        experiment[expid][chrx] = list()
    experiment[expid][chrx].append( [start, end] )

allexp = list(allexp)

for i in range(len(allexp) - 1):
    exp1 = allexp[i]
    exp1peaks = countpeaks(experiment[exp1])
    exp1chrs = set(experiment[exp1])
    for j in range(i + 1, len(allexp)):
        exp2 = allexp[j]
        exp2peaks = countpeaks(experiment[exp2])
        exp2chrs = set(experiment[exp2])
        overlapc = 0
        for chrx in exp1chrs & exp2chrs:
            peak1 = sorted(experiment[exp1][chrx], key = lambda x: x[0])
            peak2 = sorted(experiment[exp2][chrx], key = lambda x: x[0])
            for p in peak1:
                o = overlap(p, peak2, 0, len(peak2)-1)
                if o:
                    overlapc += 1
        print(exp1, exp2, exp1peaks, exp2peaks, overlapc)
