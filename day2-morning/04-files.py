#!/usr/bin/env python

# opening file with open
##f = open( "/Users/cmdb/data/genomes/BDGP6.fa")

# or
## import sys
## f = open ( sys.argv[1])
## first_line = f.readline()
## print first_line

import sys
if len (sys.argv) > 1:
    f = open(sys.argv[1])
    first_line = f.readline()
else:    
    first_line = sys.stdin.readline()

## first_line = f.readline()
print first_line
