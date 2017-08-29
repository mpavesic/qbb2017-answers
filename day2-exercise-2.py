#!/usr/bin/env python
import sys

#NM:i:0 means perfect match

count = 0

sam = sys.stdin

for line in sam:
    if line.startswith("@"):
        n = 0
    elif "NM:i:0" in line:
        n = 1
    else:
        n = 0
    count = count + n

print count
