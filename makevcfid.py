#!/usr/bin/python3

# This script reads a VEP annotated VCF file
# and put snpdbid into the 5th VCF field.
# If there is no such id, create one from
# the chromosome, position, ref and alt id
# great for plink :-)

import gzip
import sys

output = gzip.open(sys.argv[2], "w")
rsid = -1

for i in gzip.open(sys.argv[1]):
    fields = i.decode("utf-8").rstrip().split("\t")
    if fields[0].startswith("#"):
        if "ID=CSQ" in fields[0]:
            vepfields = fields[0].split("|")
            for j in range(1,len(vepfields)):
                if vepfields[j] == "Existing_variation":
                    rsid = j
                    break
    else:
        chrom  = fields[0]
        pos    = fields[1]
        ref    = fields[3]
        alt    = fields[4]
        info   = fields[7]
        infofields = info.split(";")
        for inf in infofields:
            if inf.startswith("CSQ="):
                vepfields = inf.split("|")
                if rsid == -1 or vepfields[rsid] == "":
                    varid = "%s_%s_%s_%s" % (chrom, pos, ref, alt)
                else:
                    varid = vepfields[rsid]
                break
        fields[2] = varid
    out = "\t".join(fields) + "\n"
    output.write(out.encode())
output.close()
