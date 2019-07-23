#!/usr/bin/python3

import os

metaf = open("../tables/meta.tsv")
merge = dict()

metaf.readline() # read the header
for i in metaf:
    fields = i.rstrip().split()
    filename = fields[1].split("/")[2]
    if filename not in merge:
        merge[filename] = []
    merge[filename].append(fields[2])
count = 1
for i in merge:
    print("cat "," ".join(merge[i])," >merged" + str(count) + ".fastq")
    count += 1
