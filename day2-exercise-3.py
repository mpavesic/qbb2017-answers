#!/usr/bin/env python
import sys

#NH:i:1 means hit

count = 0

sam = sys.stdin

for line in sam:
    if line.startswith("@"):
        n = 0
    elif "NH:i:1" in line:
        n = 1
    else:
        n = 0
    count = count + n

print count
