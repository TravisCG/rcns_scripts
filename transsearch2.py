#!/usr/bin/python3

import sys

id2species = dict()

for i in open(sys.argv[1]):
    cols = i.rstrip().split("\t")
    id2species[cols[0]] = " ".join(cols[1].split(" ")[0:2])

scaff = dict()

for i in open(sys.argv[2]):
    if "tp:A:P" in i:
        cols = i.rstrip().split("\t")
        if cols[0] not in scaff:
            scaff[cols[0]] = dict()
        if id2species[cols[5]] not in scaff[cols[0]]:
            scaff[cols[0]][id2species[cols[5]]] = dict()
        if cols[5] not in scaff[cols[0]][id2species[cols[5]]]:
            scaff[cols[0]][id2species[cols[5]]][cols[5]] = list()
        scaff[cols[0]][id2species[cols[5]]][cols[5]].append([int(cols[2]),int(cols[3])])


for name in scaff:
    for species in scaff[name]:
        if len(scaff[name][species]) > 1:
            for chromo in scaff[name][species]:
                for interv in scaff[name][species][chromo]:
                    print(name, species, chromo, interv[0], interv[1])
