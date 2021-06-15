#!/usr/bin/python3

import sys

table = open(sys.argv[1])
table.readline()
exphash = dict()
for i in table:
	cols = i.rstrip().split("\t")
	if cols[0] not in exphash:
		exphash[cols[0]] = list()
	exphash[cols[0]].append(cols[1])

print("library(ggplot2)")
for i in exphash:
	print('subset <- read.table("%s.tsv", colClasses = c("factor","factor","double","factor","double"))' % i)
	print('colnames(subset) <- c("expid", "peak", "peakscore", "contains_target_motif", "height")')
	print('pdf("%s.pdf")' % i)
	print('ggplot(subset, aes(x = height, y = (..count..)/sum(..count..))) + geom_histogram(data = subset(subset, contains_target_motif == 0), binwidth = 30, fill = "red", alpha = 0.3) + geom_histogram(data = subset(subset, contains_target_motif == 1), binwidth = 30, fill = "blue", alpha = 0.3) + labs(x = "Bins", y = "Percentage") + ggtitle("Histograms of summit heights")')
	print('dev.off()')
