#!/bin/bash

FQ=$1
REF=$2
PREFIX=$3

minimap2 -ax map-ont -t 8 $REF $FQ | samtools view -b - >$PREFIX.raw.bam
samtools sort -@ 8 -o $PREFIX.bam $PREFIX.raw.bam
samtools index $PREFIX.bam
rm $PREFIX.raw.bam
