#!/usr/bin/env python

"""
Write a python script to compute the number of contigs, minimum/maximum/average contig length, and N50. (Remember, you already have a FASTA parser from Bootcamp).


Parse a single FASTA record from stdin and print it.
usage: ./fastaparse_wk2.py <contiginput>

Short Read:
velvetoutput/contigs.fa
Minimum contig length: 61 Maximum contig length: 998 Average contig length: 186
The N50 is 248

SPAdeslow/contigs.fasta
Minimum contig length: 207 Maximum contig length: 1409 Average contig length: 379
The N50 is 372

SPAdes_long/contigs.fasta - long read
Minimum contig length: 207 Maximum contig length: 6731 Average contig length: 1096
The N50 is 2673

Better coverage:
velvetbc/contigs/fa
Minimum contig length: 61 Maximum contig length: 33235 Average contig length: 9096
The N50 is 19911

SPAdesBC/contigs.fasta
Minimum contig length: 111 Maximum contig length: 99915 Average contig length: 50013
The N50 is 99915
"""

import sys
import fasta
import os
from itertools import groupby
import numpy

contigs = fasta.FASTAReader(open(sys.argv[1]))

#for item in contigs:
#    print item

sorted_lengths = []

for (name, sequence) in contigs:
    seq_length = len(sequence)
    sorted_lengths.append(seq_length)

sorted_lengths = sorted(sorted_lengths, reverse=True)

print sorted_lengths

total = 0
contig_count = 0
for length in sorted_lengths:
    total = total + length
    contig_count += 1

average_contig = total / contig_count

print "Minimum contig length:", min(sorted_lengths), "Maximum contig length:", max(sorted_lengths), "Average contig length:", average_contig
# or 
# print "Minimum contig length = %; Maximum contig length = %f; Average contig length = %f"

#Calculate N50 which is the length of the contig that straddles the midpoint
n50 = 0
n50_contigs = []

for x in sorted_lengths:
    n50 = n50 + x
    n50_contigs.append(x)
    if n50 < total/2:
        continue
    else:
        break

print "The N50 is %d" % n50_contigs[-1]