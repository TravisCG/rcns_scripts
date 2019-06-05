#!/usr/bin/python3

import sys
import re

def nameprunner(rawname, ecnumbers):
    ecpat     = re.compile("\((EC[ :0-9.-]+)\)")
    ret = rawname[:-2] # remove " from the end
    ret = re.sub("[0-9]+ kDa", "", ret)
    ret = re.sub("FIG[0-9]+:", "", ret)
    ecnumbers.extend(re.findall(ecpat, ret))
    ret = re.sub(ecpat, "", ret)
    return ret

gbk = open(sys.argv[1])
outprefix = sys.argv[2]

fsa = open(outprefix + ".fsa", "w")
tbl = open(outprefix + ".tbl", "w")
writefasta = False
productline = False
noteline = False
for i in gbk:
    fields = i.rstrip().split()
    if i.startswith("LOCUS"):
        seqname = fields[1]
        seqlen  = int(fields[2])
        if seqlen < 200:
            writeout = False
        else:
            writeout = True
            fsa.write(">" + seqname + " [organism=Acinetobacter lwoffii] [strain=M2a]\n")
            tbl.write(">Features " + seqname + "\n")
    if i.startswith("ORIGIN"):
        writefasta = True
        continue
    if i.startswith("//"):
        writefasta = False
    if i.startswith('     CDS') or i.startswith('     tRNA') or i.startswith('     rRNA') or i.startswith('     misc_feature'):
        complement = False
        if "complement" in fields[1]:
            complement = True
        postr = fields[1].replace("complement(", "").replace(")","")
        if complement:
            stop,start = postr.split('..')
        else:
            start,stop = postr.split('..')
        ftype = fields[0]
        if ftype == 'misc_feature':
            ftype = 'repeat_region'
        if writeout:
            tbl.write("%s\t%s\t%s\n" % (start, stop, ftype))
    if i.lstrip().startswith('/product'):
        productline = True
        product = ''
    if i.lstrip().startswith('/note') and "color" not in i:
        noteline = True
        note = ''
    if productline:
        product += i.strip().replace('/product="', '') + " "
        if product.endswith('" '):
            productline = False
            if writeout:
                ecnums = []
                product = nameprunner(product, ecnums)
                tbl.write("\t\t\tproduct\t" + product + '\n')
                for ec in ecnums:
                    tbl.write("\t\t\tEC_number\t" + ec + '\n')
                if len(product.split(' / ')) > 1:
                    tbl.write('\t\t\tnote\tbifunctional\n')
    if noteline:
        note += i.strip().replace('/note="', '') + " "
        if note.endswith('" '):
            noteline = False
            if writeout:
                tbl.write('\t\t\tnote\t' + note[:-2] + '\n')
    if writefasta and writeout:
        outline = "".join(fields[1:])
        fsa.write(outline + "\n")

fsa.close()
tbl.close()
