#/usr/bin/python3

import scipy.stats as stats
import sys

contigs = dict()
counts = dict()
totalcount = list()

for i in open(sys.argv[1]):
	cols = i.rstrip().split()
	if cols[0] not in contigs:
		print("Next contig:",cols[0], file=sys.stderr)
		contigs[cols[0]] = [0] * (len(cols) - 2)
		counts[cols[0]] = 0.0
		if len(totalcount) == 0:
			print("Total count initialized", file=sys.stderr)
			totalcount = [0] * (len(cols) - 2)
	for j in range(2,len(cols)):
		contigs[cols[0]][j-2] += float(cols[j])
		totalcount[j-2] += float(cols[j])
	counts[cols[0]] += 1.0

for i in contigs:
	for j in range(len(contigs[i])):
		contigs[i][j] = contigs[i][j] / totalcount[j] / counts[i]
	res = stats.ttest_ind(contigs[i][0:4], contigs[i][5:9], equal_var=False)
	if res.pvalue < 0.05:
		print(i,res.statistic, res.pvalue, contigs[i], sep="\t")
