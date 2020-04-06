#!/usr/bin/python3

import sys
import gzip

kmersize = 100

kmer = set()
kmerfile = open(sys.argv[1])
for i in kmerfile:
	kmer.add(i.rstrip())
kmerfile.close()

count = 0
totalcount = 0
foundkmer = set()

for fastq in sys.argv[2:]:
	infile = gzip.open(fastq)
	for i in infile:
		line = i.decode('utf-8').rstrip()
		if count % 4 == 1:
			for startpos in range(0, len(line)-kmersize):
				subseq = line[startpos:startpos+kmersize]
				if subseq in kmer:
					totalcount += 1
					foundkmer.add(subseq)
		count += 1
		if count % 1000000 == 0:
			print("Process:", count, file=sys.stderr)
	infile.close()

print(fastq, len(foundkmer), totalcount, count / 4, sep = "\t")
