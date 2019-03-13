#!/usr/bin/python3

# This script reads a headerless ped file and a VCF file
# and try to make in input for trio package

import sys

persons = dict()

ped = open(sys.argv[1])
for i in ped:
    fields = i.rstrip().split()
    pid = fields[1]
    if pid not in persons:
        persons[pid] = list()
    persons[pid].extend(fields)
ped.close()

header = ["famid", "pid", "fatid", "motid", "sex", "affected"]

vcf = open(sys.argv[2])
for i in vcf:
    if i.startswith("#"):
        if i.startswith("#CHR"):
            ids = i.rstrip().split()
        continue
    fields = i.rstrip().split()
    chrom = fields[0]
    pos = fields[1]
    ref = fields[3]
    alt = fields[4]
    if "," in alt:
        # Multi allele site
        continue
    if len(alt) > 1 and len(ref) > 1:
        # not snv
        continue
    snvid = "_".join([chrom, pos, ref, alt])
    header.append(snvid)
    for j in range(9,len(fields)):
        gt = fields[j].split(":")[0]
        if gt == "./." or gt == ".|." or gt == "0/0" or gt == "0|0":
            code = "0"
        elif gt == "0/1" or gt == "0|1":
            code = "1"
        elif gt == "1/1" or gt == "1|1":
            code = "2"
        else:
            sys.err.write("Unknown genotype:" + gt + "\n")
        persons[ids[j]].append(code)
vcf.close()

print("\t".join(header))
for pid in persons:
    print("\t".join(persons[pid]))
