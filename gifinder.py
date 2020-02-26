#!/usr/bin/python3

blastout  = open("../blastdb/gi.blast.out")
gi_length = dict()
coverage  = dict()
allstrains = set()
for i in blastout:
    if i.startswith("#"):
        continue
    fields = i.rstrip().split("\t")
    gi_id  = fields[0]
    strain = "_".join(fields[1].split("_")[:-1])
    allstrains.add(strain)
    perc   = float(fields[2])
    alnlen = int(fields[3])
    if perc < 0.9: # HSP similarity should be larger than 90%
        continue
    if alnlen < 200: # if the HSP too small, we drop it
        continue
    if gi_id not in gi_length:
        gi_length[gi_id] = alnlen # the first hit will be the same, so the alignment length gives us the length of the GI
        coverage[gi_id] = dict()
    if strain not in coverage[gi_id]:
        coverage[gi_id][strain] = list()
    coverage[gi_id][strain].append([int(fields[6]), int(fields[7]), int(fields[8]), int(fields[9]), fields[1]])
blastout.close()

for gi_id in coverage:
    l = gi_length[gi_id]
    for strain in coverage[gi_id]:
        cov = [0] * l
        straincoord = list() # genomic island coordinates in the specified strain
        for hsp in coverage[gi_id][strain]:
            gi_start = hsp[0] -1
            gi_end   = hsp[1]
            for i in range(gi_start, gi_end):
                cov[i] = 1
        if (l * 0.9) < float(sum(cov)):
            # strain accepted, because the HSPs cover more than 90%
            # some part of the genomic island is covered more than one
            # we select the larger parts
            removeindex = set()
            for i in range(len(coverage[gi_id][strain]) - 1):
                for j in range(i + 1, len(coverage[gi_id][strain])):
                    hsp1 = coverage[gi_id][strain][i]
                    hsp2 = coverage[gi_id][strain][j]
                    if hsp2[0] > hsp1[0] and hsp2[1] < hsp1[1]:
                        # hsp2 is inside hsp1
                        removeindex.add(j)
                    if hsp1[0] > hsp2[0] and hsp1[1] < hsp2[1]:
                        removeindex.add(i)
            removeindex = sorted(removeindex, reverse = True) # deleting from an array will reindex it
            for i in removeindex:
                del coverage[gi_id][strain][i]

allstrains = list(allstrains)
print("\t".join(allstrains))
for gi_id in coverage:
    out = list()
    out.append(gi_id)
    for strain in allstrains:
        if strain in coverage[gi_id]:
            out.append("+")
        else:
            out.append("-")
    print("\t".join(out))
