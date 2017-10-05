#!/usr/bin/env python

"""
first, adjust phenotype file BYxRM_PhenoData.txt to replace categorical underscore with a tab

$ awk 'NR>1''{gsub ("_","\t")}{print}' BYxRM_PhenoData.txt > phenotype.txt

Output linear association files:
$ plink2 --vcf BYxRM_segs_saccer3.bam.simplified.vcf --pheno phenotype.txt --allow-no-sex --linear --allow-extra-chr --all-pheno

Usage: ./Week4B.py <plink.P___.assoc.linear>

"""

import sys
import math
import matplotlib.pyplot as plt
import numpy as np


sig = []
nonsig = []

plink_lin = open(sys.argv[1])

#determine the length of the assoc.linear files
# line_count = 0

line_count = 5
for entry in plink_lin:
    line_count +=1
    
for c in range(line_count):
    sig.append(None)
    nonsig.append(None)

# print len(sig)
# print len(nonsig)

counter = 0
plink_lin.seek(0)
for item in plink_lin:
    a = item.split()
    if "CHR" in a:
        continue
    elif "NA" in a:
        continue
    # line_count += 1
    elif float(a[8]) <= 10e-5 :
        sig[counter] = -np.log10(float(a[8]))
        counter += 1
    elif float(a[8]) > 10e-5 :
        nonsig[counter] = -np.log10(float(a[8]))
        counter += 1




plt.figure()
plt.scatter(range(len(sig)), nonsig, alpha = 0.5, s=7,  c="grey")
plt.scatter(range(len(sig)), sig, alpha = 0.5, s=7, c="red")
plt.xlabel("Location on Genome")
plt.ylabel("-log10(p-Value)")
plt.title(sys.argv[2])
plt.savefig(sys.argv[2] + "_manhattan_plot.png")
plt.close()

