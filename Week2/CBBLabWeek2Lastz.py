#!/usr/bin/env python


"""
To run Lastz
lastz <target> [<query>] [<options>]
 reference.fasta

Short Read:
Velvet -- 
$ lastz reference.fasta velvetoutput/contigs.fa --chain --step=20 --nogapped --format=general:start1,size2,end1,name2 --output=velvetLowLastz.tsv

$ sort -k 1,1 -n velvetLowLastz.tsv > sorted_velvetLowLastz.tsv

$ ./CBBLabWeek2Lastz.py sorted_velvetLowLastz.tsv Velvet_Low

SPAdes -- 

$ lastz reference.fasta SPAdeslow/contigs.fasta --chain --step=20 --nogapped --format=general:start1,size2,end1,name2 --output=SPAdesLowLastz.tsv

$ sort -k 1,1 -n SPAdesLowLastz.tsv > sorted_SPAdesLowLastz.tsv

$ ./CBBLabWeek2Lastz.py sorted_SPAdesLowLastz.tsv SPAdes_Low

Nanopore SPAdes Long Read
$ lastz reference.fasta SPAdes_long/contigs.fasta --chain --step=20 --nogapped --format=general:start1,size2,end1,name2 --output=SPAdes_Long_Lastz.tsv

$ sort -k 1,1 SPAdes_Long_Lastz.tsv > sorted_SPAdes_Long_Lastz.tsv

$ ./CBBLabWeek2Lastz.py sorted_SPAdes_Long_Lastz.tsv SPAdes_Long

Better Coverage:
Velvet --
$ lastz reference.fasta velvetbc/contigs.fa --chain --step=20 --nogapped --format=general:start1,size2,end1,name2 --output=velvetBCLastz.tsv

$ sort -k 1,1 -n velvetBCLastz.tsv > sorted_velvetBCLastz.tsv

$ ./CBBLabWeek2Lastz.py sorted_velvetBCLastz.tsv Velvet_BetterCoverage

SPAdes --

$ lastz reference.fasta SPAdesBC/contigs.fasta --chain --step=20 --nogapped --format=general:start1,size2,end1,name2 --output=SPAdesBCLastz.tsv

$ sort -k 1,1 -n SPAdesBCLastz.tsv > sorted_SPAdesBCLastz.tsv

$ ./CBBLabWeek2Lastz.py sorted_SPAdesBCLastz.tsv SPAdes_BetterCoverage

"""

"""

USAGE: ./CBBLabWeek2Lastz.py <input_tsv> <outputfile>

"""

import sys
import fasta
import itertools
import matplotlib.pyplot as plt

data = open(sys.argv[1])


plt.figure()

count = 0

#Counter adds each successive contig length so that they stack correctly    
for value in data:
    #start 1 in header line, skip that
    if "start1" in value:
        continue
    else:
        fields = value.split("\t")
        #start field 0, end field 2
        plt.plot([count, count + int(fields[1])], [int(fields[0]), int(fields[2])])
        count += int(fields[1])
        


plt.xlabel("Position")
plt.ylabel("Contig")
plt.title("SPAdes Better Coverage assembly")
plt.xlim(0,200000)
plt.ylim(0,200000)
plt.savefig( sys.argv[2] + ".png")
plt.close()