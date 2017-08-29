#!/usr/bin/env python
import sys

count = 0

sam = sys.stdin

for line in sam:
    if line.startswith("@"):
        n = 0
    else:
        if "NM:" in line:
            n = 1   
        else:
            n = 0
    count = count + n

print count
