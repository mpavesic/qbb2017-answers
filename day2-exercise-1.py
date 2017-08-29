#!/usr/bin/env python
import sys

count = 0

sam = sys.stdin

for line in sam:
    if line.startswith("@"):
        n = 0
    else:
        n = 1
    count = count + n

print count
