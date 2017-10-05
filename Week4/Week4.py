#!/usr/bin/env python

"""
/Users/cmdb/qbb2017-answers/Week4 $ plink2 --pca 2 tabs header --freq --vcf BYxRM_segs_saccer3.bam.simplified.vcf --allow-extra-chr --mind

Usage:
./Week4.py plink.eigenvec PCA1_PCA2
"""
import sys
import pandas as pd
import matplotlib.pyplot as plt

df_pca = pd.read_csv( sys.argv[1], sep="\t")

x = df_pca["PC1"]
y = df_pca["PC2"]

plt.figure()
plt.scatter(x, y, alpha = 0.5)
plt.savefig( sys.argv[2] + ".png" )
plt.xlabel("PCA1")
plt.ylabel("PCA2")
plt.title("PCA_BYxRM")
plt.close()

