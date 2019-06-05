#!/usr/bin/python3

import sys

binsize    = int(sys.argv[1])
matrix     = dict()
allsamples = list()
for filename in sys.argv[2:]:
    f = open(filename)
    samplename = filename.split(".")[0]
    allsamples.append(samplename)
    for line in f:
        fields     = line.rstrip().split()
        cnvtype    = fields[0]
        if cnvtype == "deletion":
            cnvtype = "-1"
        else:
            cnvtype = "1"
        pos        = fields[1]
        pices      = pos.split(":")
        chrom      = ":".join(pices[:-1])
        start, end = [int(x) for x in pices[-1].split("-")]
        for segment in range(start, end, binsize):
            newkey = chrom + "," + str(segment) + "," + str(segment+binsize-1)
            if newkey not in matrix:
                matrix[newkey] = dict()
            matrix[newkey][samplename] = cnvtype
    f.close()

print("\t".join(allsamples))
for key in matrix:
    out = list()
    out.append(key)
    for sample in allsamples:
        if sample in matrix[key]:
            out.append(matrix[key][sample])
        else:
            out.append("0")
    print("\t".join(out))
