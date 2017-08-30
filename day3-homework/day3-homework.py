#!/usr/bin/env python

"""
Implement a script that finds matching k-mers between a single query sequence and a database 
of targets. The matcher should take three arguments:

kmer_matcher.py <target.fa> <query.fa> <k>

Where target.fa is the database, potentially multiple sequences, query.fa is the sequence to 
align (assume just one sequnce), and k is the k-mer size (an integer).

The script should find k-mer matches and for each write:

target_sequence_name    target_start    query_start k-mer

For submission: Run the program for k=11 and submit the first 1000 lines, along with your 
script.

"""

import sys
import fasta

target = open(sys.argv[1])
query = open(sys.argv[2])
k = int(sys.argv[3])

# when run, use k = 11
# <target.fa> /Users/cmdb/qbb2017-answers/day3-afternoon/subset.fa
# <query.fa> /Users/cmdb/qbb2017-answers/day3-homework/droYak2_seq.fa

kmer_index = {}

#building library from target file
for ident, sequence in fasta.FASTAReader(target):
    sequence = sequence.upper()
    for i in range (0, len(sequence) - k):
    # need to stop kmer length from end of sequence
        kmer = sequence[i:i+k]
        if kmer not in kmer_index:
            kmer_index[kmer] = [(ident,i)]
        else:
            kmer_index[kmer].append((ident,i))
        #print kmer_index

    
# checking kmers in query file against target library 
ident, sequence_q = fasta.FASTAReader(query).next()
sequence_q = sequence_q.upper()
for j in range (0, len(sequence_q) - k):
    kmer_q = sequence_q[j:j+k]
    if kmer_q in kmer_index:
        result = kmer_index[kmer_q]
        for item in result:
            print item[0], "\t", item[1], "\t", j, "\t", kmer_q
        
