#!/usr/bin/python3

import sys
import re

def whichcateg(ref, alt):
    if ref == 'A' and alt == 'G':
        return 5
    if ref == 'T' and alt == 'C':
        return 5
    if ref == 'A' and alt == 'T':
        return 6
    if ref == 'A' and alt == 'C':
        return 6
    if ref == 'T' and alt == 'A':
        return 6
    if ref == 'T' and alt == 'G':
        return 6
    if ref == 'C' and alt == 'A':
        return 4
    if ref == 'C' and alt == 'G':
        return 4
    if ref == 'G' and alt == 'T':
        return 4
    if ref == 'G' and alt == 'C':
        return 4
    if ref == 'C' and alt == 'T':
        return 3
    if ref == 'G' and alt == 'A':
        return 3
    return 7

def whicheffect(ref, alt, cons):
    # "noncoding/silent/nonsilent/null"
    out =  { "frameshift_variant":            "nonsilent",
             "transcript_ablation":           "nonsilent",
             "splice_acceptor_variant":       "nonsilent",
             "splice_donor_variant":          "nonsilent",
             "frameshift_variant":            "nonsilent",
             "stop_lost":                     "nonsilent",
             "coding_sequence_variant":       "nonsilent",
             "inframe_deletion":              "nonsilent",
             "inframe_insertion":             "nonsilent",
             "missense_variant":              "nonsilent",
             "stop_gained":                   "nonsilent",
             "synonymous_variant":            "silent",
             "splice_region_variant":         "silent",
             "start_lost":                    "nonsilent",
             "start_retained_variant":        "silent",
             "protein_altering_variant":      "nonsilent",
             "3_prime_UTR_variant":           "noncoding",
             "downstream_gene_variant":       "noncoding",
             "5_prime_UTR_variant":           "noncoding",
             "upstream_gene_variant":         "noncoding",
             "intergenic_variant":            "noncoding",
             "intron_variant":                "noncoding",
             "non_coding_transcript_variant": "noncoding",
             "non_coding_transcript_exon_variant": "noncoding",
             "NMD_transcript_variant":        "noncoding",
             "TFBS_ablation":                 "noncoding",
             "TFBS_amplification":            "noncoding",
             "TF_binding_site_variant":       "noncoding",
             "regulatory_region_ablation":    "noncoding",
             "regulatory_region_amplification": "noncoding",
             "feature_elongation":            "noncoding",
             "regulatory_region_variant":     "noncoding",
             "feature_truncation":            "noncoding",
             "mature_miRNA_variant":          "noncoding"
            }

    conslist = list()
    for i in cons.split("&"):
        if i in out:
            conslist.append(out[i])

    # Hierarchy
    if "nonsilent" in conslist:
        return "nonsilent"
    if "silent" in conslist:
        return "silent"
    if "noncoding" in conslist:
        return "noncoding"
    return "null"

reannot = re.compile("CSQ=([^;]+)")

#print("gene\tpatient\teffect\tcateg")
for i in open(sys.argv[1]):
    if i.startswith('#CH'):
        header = i.rstrip().split()[9:]
    if not i.startswith('#'):
        cols = i.rstrip().split('\t')
        if cols[6] != "PASS":
            continue
        alts = cols[4].split(',')
        althash = dict()
        for j in alts:
            althash[j] = list()
        match = reannot.search(cols[7])
        if match:
            annots = match.group(1).split(',')
            for j in annots:
                alt = j.split('|')[0]
                if alt in althash:
                    althash[alt].append(j)
            for altnum in range(len(alts)):
                categ = whichcateg(cols[3], alts[altnum])
                for j in range(len(header)):
                    gt = cols[9+j].split(":")[0]
                    if gt == '0/0' or gt == './.' or gt == '0|0' or gt == '.|.':
                        continue
                    gtindex = int(gt[-1])-1
                    thisannotlist = althash[alts[gtindex]]
                    for thisannot in thisannotlist:
                        thisgene = thisannot.split('|')[3]
                        if thisgene == "":
                            continue
                        thiseff  = whicheffect(cols[3], alts[altnum], thisannot.split('|')[1])
                        print(thisgene, header[j], thiseff, categ, sep="\t")
