#!/usr/bin/python3

# replace sample name in VCF file

import gzip
import sys

output = gzip.open(sys.argv[2], "w")

for i in gzip.open(sys.argv[1]):
	txt = i.decode("utf-8")
	if txt.startswith("#CHROM"):
		# replace header
		f    = txt.split("\t")
		f[9] = sys.argv[3]
		txt  = "\t".join(f) + "\n"
		i = txt.encode()
	output.write(i)
