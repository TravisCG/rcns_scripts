#!/usr/bin/python3

# Correct tesserac OCR read errors
# in my case 0 some times become O,
# but it is systematic

import sys
import re

check = re.compile("[A-Z]{4}[0-9]{8}")

for i in open(sys.argv[1]):
    if len(i.rstrip()) == 12:
        if i[4] == 'O':
            i = i[0:4] + '0' + i[5:]
        match = check.match(i)
        if not match:
            print("problem:" + i)
    print(i.rstrip())
