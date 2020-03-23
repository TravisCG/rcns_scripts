#!/usr/bin/python3

import sys
import gzip
import glob

kmersize = 100

kmer = set()
kmerfile = open(sys.argv[1])
for i in kmerfile:
	kmer.add(i.rstrip())
kmerfile.close()

allfastq = glob.glob(sys.argv[2] + "/*q.gz") # fastq.gz fq.gz

for fastq in allfastq:
	infile = gzip.open(fastq)
	count = 0
	totalcount = 0
	foundkmer = set()
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
	print("Done:", fastq, file=sys.stderr)
	print(fastq, len(foundkmer), totalcount, sep = "\t")
