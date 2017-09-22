#!/usr/bin/env python


"""
To run Lastz
lastz <target> [<query>] [<options>]
 reference.fasta

$ lastz reference.fasta velvetoutput/contigs.fa --chain --step=20 --nogapped --format=general:start1,size2,end1,name2 --output=velvetLastz.tsv

$ lastz reference.fasta SPAdes/contigs.fasta --chain --step=20 --nogapped --format=general:start1,size2,end1,name2 --output=SPAdesLastz.tsv

"""

"""
needs:
open data

need to iterate through plotting of reference vs contigs
start plotting "for loop"

USAGE: ./CBBLabWeekLastz.py SPAdesLastz_sorted.tsv

 ./CBBLabWeeks2Lastz.py velvetLastz_sorted.tsv

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
        plt.plot([int(fields[0]), int(fields[2])], [count, count + int(fields[1])])
        
        count += int(fields[1])
        


plt.xlabel("Position")
plt.ylabel("Contig")
plt.title("SPAdes short read assembly")
plt.xlim(0,100000)
plt.ylim(0, 100000)
plt.savefig( "SPAdes_plot1" + ".png")
plt.close()