#!/usr/bin/python3

"""
   Simple RFLP program. Takes two input files:
   - maker output gff (after gff3_merge, gff3_merge -d master_datastore_index.log -n -l)
   - restriction output created by remap
   The program has hash for the genes and enzymes
"""

import sys

need = { "STP22_YEAST": {"EcoRV", "PstI"},
         "HIS4_YEAST" : {"HindIII", "EcoRV"},
         "ACT_YEAST"  : {"HinfI", "HaeIII", "MseI", "BglII"},
         "COX2_YEAST" : {"HinfI"},
         "MET2_YEAST" : {"EcoRI", "PstI"},
         "CYAA_YEAST" : {"HaeIII", "HpaII"}}

found = dict()
for i in open(sys.argv[1]):
	cols = i.rstrip().split("\t")
	if len(cols) < 9:
		continue
	if cols[1] != "blastx":
		continue
	if cols[2] != "protein_match":
		continue
	for protname in need:
		if protname in i:
			if protname not in found:
				found[protname] = list()
			found[protname].append([cols[0], int(cols[3]), int(cols[4]), []])

for i in open(sys.argv[2]):
	cols = i.rstrip().split()
	if "Sequence" in i:
		contigname = cols[2]
	if len(cols) < 13:
		continue
	if cols[0] == "Start":
		continue
	start  = int(cols[0])
	end    = int(cols[1])
	enzyme = cols[3]
	for protname in need:
		for region in found[protname]:
			if region[0] == contigname and region[1] < start and region[2] > end and enzyme in need[protname]:
				region[3].append(cols)

for protname in found:
	for enzyme in need[protname]:
		for region in found[protname]:
			fragments = list()
			prevpos = region[1]
			for ressites in region[3]:
				if ressites[3] != enzyme:
					continue
				fragments.append(str(int(ressites[0]) - prevpos))
				prevpos = int(ressites[0])
			fragments.append(str(region[2] - prevpos))
			print(protname, enzyme, region[0], region[1], region[2], "\t".join(fragments), sep = "\t")
