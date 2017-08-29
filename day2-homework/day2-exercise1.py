#!/usr/bin/env python
import sys

flydb = sys.stdin
#line 52 is the beginning of data
#columns of interest AC and Flybase_gene 

for line in flydb:
    if "DROME" in line:
        fields = line.rstrip("\r\n").split()
        if len(fields) < 4:
            continue
        else:
            #fields[2] AC
            #fields[3] flybase
            print fields[3] + "\t" + fields[2] 
        

