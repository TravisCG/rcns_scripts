#!/bin/bash

# poor man's docker
# this little scripts configure 
# a worker node in the cloud

SAMPLE=$1

# Install necessary software components
sudo yum -y install python3-pip
sudo yum -y install java-1.8.0-openjdk
sudo yum -y install gcc
sudo yum -y install python3-devel
sudo pip3 install snakemake

# copy necessary files
cd /mnt/resource
sudo mkdir rabbit
sudo chown centos:centos rabbit
cd rabbit
mkdir fastq
mkdir bam
mkdir gvcf
mkdir log
scp -o "StrictHostKeyChecking no" -r dev-genom-master01:/data/rabbit/progs ./
scp -r dev-genom-master01:/data/rabbit/genomes ./
scp dev-genom-master01:/data/rabbit/fastq/${SAMPLE}* ./fastq
ssh -o "StrictHostKeyChecking no" dev-genom-master01 'rm -f /data/rabbit/fastq/'${SAMPLE}*
scp -r dev-genom-master01:/data/rabbit/Snakefile.tmp ./
sed 's/XXXX/'$SAMPLE'/g' Snakefile.tmp >Snakefile

# Run GATK using Snakemake
snakemake -j 20

# copy results back to master
scp gvcf/* dev-genom-master01:/data/rabbit/gvcf
scp bam/* dev-genom-master01:/data/rabbit/bam
scp log/* dev-genom-master01:/data/rabbit/log
scp ~/log.txt dev-genom-master01:/data/rabbit/log/${SAMPLE}.log
scp ~/err.txt dev-genom-master01:/data/rabbit/log/${SAMPLE}.err

sudo poweroff
