#/usr/bin/python3

# The F??king Script
# Formatting illogical tables into "normal" table

import sys

counter = 0
winnum = 1
cols = list()
print("Window_num Window_start Window_ens Num1 Gt_1 Num2 Gt_2 Num_3 Gt_3")
for i in open(sys.argv[1]):
    line = i.rstrip()
    if not line.startswith(" "):
        if counter % 2 == 0:
            if len(cols) == 0:
                continue
            for j in range(len(cols),5):
                cols.append("0 0")
            print(winnum," ".join(cols))
            winnum += 1
            cols = list()
        counter += 1
    else:
        line = line.strip()
    cols.append(line)
