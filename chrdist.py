#!/usr/bin/python3

import sys

def removeoverlap(regions):
	while True:
		for i in range(1,len(regions)):
			if regions[i - 1][1] > regions[i][0]:
				regions[i - 1][1] = max(regions[i - 1][1], regions[i][1])
				del regions[i]
				break
		else:
			break

def calclen(regions):
	s = 0
	for i in regions:
		s += i[1] - i[0]
	return s

def nocoverage(regions):
	s = regions[0][0]
	for i in range(1, len(regions)):
		s += regions[i][0] - regions[i - 1][1]
	return s

scaffolds = dict()
scafflen  = dict()
chromosomes = set()

for i in open(sys.argv[1]):
	fields = i.rstrip().split("\t")
	src    = fields[0]
	target = fields[5]
	length = int(fields[1])
	start  = int(fields[2])
	end    = int(fields[3])

	scafflen[src] = length
	chromosomes.add(target)

	if src not in scaffolds:
		scaffolds[src] = dict()
	if target not in scaffolds[src]:
		scaffolds[src][target] = list()
	scaffolds[src][target].append([start, end])

chromosomes = list(chromosomes)
print("\t".join(chromosomes) + "\tmissing")

for i in scaffolds:
	out = list()
	out.append(i)
	allregions = list()
	for chrom in chromosomes:
		if chrom in scaffolds[i]:
			regions = sorted(scaffolds[i][chrom], key = lambda x: x[0])
			removeoverlap(regions)
			allregions.extend(regions)
			coverage = calclen(regions)
			out.append(str(coverage / scafflen[i]))
		else:
			out.append("0.0")
	allregions = sorted(allregions, key = lambda x:x[0])
	removeoverlap(allregions)
	nocover = nocoverage(allregions)
	out.append(str(nocover / scafflen[i]))
	print("\t".join(out))
