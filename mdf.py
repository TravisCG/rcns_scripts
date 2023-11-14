#!/usr/bin/python3

"""
  Metadata formatter for the Metagenomic data
"""

import sys

for i in open(sys.argv[1]):
    if "ITS" in i:
        tech = "its"
    else:
        tech = "16s"
    fields = i.rstrip().split("_")
    lastchunk = fields[-2]
    name = i.rstrip().split("/")[-1]
    if lastchunk.endswith("5"):
        depth = "5"
    else:
        depth = "20"
    if name.startswith("TA"):
        place = "badacsony"
    elif name.startswith("E1"):
        place = "eger_terasz"
    elif name.startswith("E2"):
        place = "eger_kutato"
    elif name.startswith("E3"):
        place = "eger_thummerer"
    elif name.startswith("KE1"):
        place = "kecskemeti_uj_telek"
    elif name.startswith("KE2"):
        place = "kecskemeti_kutato"
    elif name.startswith("SZE1"):
        place = "szekszard_leanyvar"
    elif name.startswith("SZE2"):
        place = "szekszard_kisbodo"
    elif name.startswith("TO"):
        place = "tokaj_tarcali_kutato"
    else:
        place = "unknown"
    print("%s\t%s\t%s\t%s" % (name, tech, depth, place))
