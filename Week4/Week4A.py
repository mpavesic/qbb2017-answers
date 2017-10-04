#!/usr/bin/env python


"""
/Users/cmdb/qbb2017-answers/Week4 $ plink2 --pca 2 tabs header --freq --vcf BYxRM_segs_saccer3.bam.simplified.vcf --allow-extra-chr --mind

./Week4A.py BYxRM_segs_saccer3.bam.simplified.vcf AlleleFreqHistogram

"""

import sys
import itertools
import matplotlib.pyplot as plt

vcf_file =  open(sys.argv[1])

allele_frequency = []

plt.figure()
for i in vcf_file:
   if i.startswith('#'):
       pass
   else:
       i = i.split('\t')[7]  
       i = i.lstrip("AF=")
       if "," in i:
           i = i.split(",")[0]
       allele_frequency.append(float(i))

           
plt.hist(allele_frequency, bins=[0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0])
plt.xlabel("Allele Frequency")
plt.ylabel("Counts")
plt.title("Histogram_BYxRM")
plt.savefig("Allele_frequency" + ".png")
plt.close()