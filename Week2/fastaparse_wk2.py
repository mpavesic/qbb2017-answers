#!/usr/bin/env python

"""
Write a python script to compute the number of contigs, minimum/maximum/average contig length, and N50. (Remember, you already have a FASTA parser from Bootcamp).

each entry in contigs.fa has length in header line
eg)
>NODE_8_length_148_cov_1.500000


Parse a single FASTA record from stdin and print it.
usage: ./fastaparse_wk2.py reads_low_1_kmer.fastq/contigs.fa > output
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