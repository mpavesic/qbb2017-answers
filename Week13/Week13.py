#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt

"""
SRR492183.kraken
SRR492186.kraken
SRR492188.kraken
SRR492189.kraken
SRR492190.kraken
SRR492193.kraken
SRR492194.kraken
SRR492197.kraken

Need to create a tab-delimited file that assembles counts of each taxon
"""

"""
trial usage:
./Week13.py week13_data/KRAKEN/SRR492183.kraken > SRR492183_Summary
./Week13.py week13_data/KRAKEN/SRR492186.kraken > SRR492186_Summary
./Week13.py week13_data/KRAKEN/SRR492188.kraken > SRR492188_Summary
./Week13.py week13_data/KRAKEN/SRR492189.kraken > SRR492189_Summary
./Week13.py week13_data/KRAKEN/SRR492190.kraken > SRR492190_Summary
./Week13.py week13_data/KRAKEN/SRR492193.kraken > SRR492193_Summary
./Week13.py week13_data/KRAKEN/SRR492194.kraken > SRR492194_Summary
./Week13.py week13_data/KRAKEN/SRR492197.kraken > SRR492197_Summary

"""

day0 = open(sys.argv[1])
taxoncounts = {}

for entry in day0:
    line = entry.rstrip("\n").split("\t")
    read_id = line[0]
    # taxa = line[1].split(";") - makes taxon designation separate. Keeping in place for easier count.
    # taxa = line[1]
    # print taxa
    if line[1] not in taxoncounts:
        taxoncounts[line[1]] = 1
    else:
        taxoncounts[line[1]] += 1
    # print taxoncounts

for thing in taxoncounts:
    count = taxoncounts[thing]
    taxa = "\t".join(thing.split(";"))
    line = str(count) + "\t" + taxa + "\n"
    print line
    

"""
    To produce KronaTools charts
    
ktImportText SRR492183_Summary -o SRR492183_Summary
ktImportText SRR492186_Summary -o SRR492186_Summary
ktImportText SRR492188_Summary -o SRR492188_Summary
ktImportText SRR492189_Summary -o SRR492189_Summary
ktImportText SRR492190_Summary -o SRR492190_Summary
ktImportText SRR492193_Summary -o SRR492193_Summary
ktImportText SRR492194_Summary -o SRR492194_Summary
ktImportText SRR492197_Summary -o SRR492197_Summary
    
"""