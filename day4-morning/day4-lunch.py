#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
Usage: ./day4-lunch.py <ctab1> <ctab2> <outplot>

Use scatter() to plot the FPKM values of SRR072893 vs SRR072915.
~/data/results/stringtie/SRR072893/t_data.ctab
~/data/results/stringtie/SRR072915/t_data.ctab


- Provide plot title and label axes
- Compensate for extreme values by log transforming your values. Be sure not to lose any transcripts.
- Compensate for overlapping points by adjusting transparency
- Fit a curve

"""

df1 = pd.read_csv( sys.argv[1], sep="\t")
df2 = pd.read_csv( sys.argv[2], sep="\t")

x = np.log(df1["FPKM"] + 1)
y = np.log(df2["FPKM"] + 1)

##  NOT WORKING YET
# poly = np.polyfit(x,y,1)
# fit = np.poly1d(poly)

plt.figure()
plt.scatter(x, y, alpha = 0.1)
plt.plot(np.unique(x), np.poly1d(np.polyfit(x,y, deg = 2))(np.unique(x)))
plt.axis([0,10,0,10])
plt.xlabel("SRR072893")
plt.ylabel("SRR072915")
plt.title("RPKM Values")
plt.savefig( sys.argv[3] + ".png" )
plt.close()

