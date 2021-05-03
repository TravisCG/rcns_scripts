#!/usr/bin/python3

"""
   Peakscore and summit score normalizer
"""

import sys
import math

class PeakSummit:
	def __init__(self):
		self.count     = 0.0
		self.avgpeak   = 0.0
		self.avgsummit = 0.0
		self.sdpeak    = 0.0
		self.sdsummit  = 0.0

experiments = dict()

# Calculating sums
f = open(sys.argv[1])
f.readline()
for i in f:
	cols      = i.rstrip().split()
	expid     = cols[4]
	peakscore = float(cols[8])
	summit    = float(cols[7])
	if expid not in experiments:
		experiments[expid] = PeakSummit()
	experiments[expid].avgsummit += summit
	experiments[expid].avgpeak   += peakscore
	experiments[expid].count     += 1.0
f.close()

# Calculating average
for expid in experiments:
	experiments[expid].avgpeak   = experiments[expid].avgpeak   / experiments[expid].count
	experiments[expid].avgsummit = experiments[expid].avgsummit / experiments[expid].count

# Calculating standard deviation
f = open(sys.argv[1])
f.readline()
for i in f:
	cols      = i.rstrip().split()
	expid     = cols[4]
	peakscore = float(cols[8])
	summit    = float(cols[7])
	experiments[expid].sdpeak   += (peakscore - experiments[expid].avgpeak)   * (peakscore - experiments[expid].avgpeak)
	experiments[expid].sdsummit += (summit    - experiments[expid].avgsummit) * (summit    - experiments[expid].avgsummit)
f.close()

for expid in experiments:
	experiments[expid].sdpeak   = math.sqrt(experiments[expid].sdpeak   / experiments[expid].count)
	experiments[expid].sdsummit = math.sqrt(experiments[expid].sdsummit / experiments[expid].count)

# Z-score normalization
f = open(sys.argv[1])
print(f.readline().rstrip())
for i in f:
	cols      = i.rstrip().split()
	expid     = cols[4]
	peakscore = float(cols[8])
	summit    = float(cols[7])
	if experiments[expid].sdpeak != 0.0:
		cols[8] = str(peakscore - experiments[expid].avgpeak   / experiments[expid].sdpeak)
	else:
		cols[0] = "0"
	if experiments[expid].sdsummit != 0.0:
		cols[7] = str(summit    - experiments[expid].avgsummit / experiments[expid].sdsummit)
	else:
		cols[7] = "0"
	print("\t".join(cols))
