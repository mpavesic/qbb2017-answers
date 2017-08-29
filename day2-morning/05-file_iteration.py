#!/usr/bin/env python

import sys

fh = sys.stdin

for line in fh:
    #Start and end are in columns 3 and 4
    if line.startswith("t_id"):
        continue
    fields = line.split("\t")
    #designates tab delimiting in file
    print int(fields[4]) - int(fields[3])
    #converts string fields to integers to calculate differences