#!/usr/bin/python3

import sys

# consmotif       chr     start   end     expID   antibody        summitpos       hight   peakscore       motifstart      motifend

class Peak:
	def __init__(self, summitpos, hight, peakscore):
		self.summit = dict()
		self.summit[summitpos] = float(hight)
		self.peakscore = peakscore
		self.motifs = set()
	def maxsh(self):
		m = 0
		for s in self.summit:
			if self.summit[s] > m:
				m = self.summit[s]
		return m

targetexp = sys.argv[2]
motifs = sys.argv[3:]

peak = dict()

for i in open(sys.argv[1]):
	cols = i.rstrip().split()
	expid = cols[4]
	if expid == targetexp:
		k = cols[1] + ":" + cols[2] + "-" + cols[3]
		if k not in peak:
			peak[k] = Peak(cols[6], cols[7], cols[8])
		peak[k].motifs.add(cols[0])
		peak[k].summit[cols[6]] = float(cols[7])

for k in peak:
	target = "0"
	for m in motifs:
		if m in peak[k].motifs:
			target = "1"
	print(targetexp, k, peak[k].peakscore, target, peak[k].maxsh())
