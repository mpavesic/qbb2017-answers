#!/usr/bin/env python

import sys

totalspan = 0
genecnt = 0

for line in sys.stdin:
    #stdin means $ cat file | python command
    # $ cat lens | ./Day3-afternoon.py
    line = line.rstrip()
    #strips excess whitespace from right side of the data column
    mylen = int(line)
    #converts data to integers
    totalspan += mylen
    genecnt += 1

print "there are %d genes, with a total span of %d, average gene length is %f" % (genecnt, totalspan, float(totalspan/genecnt))
