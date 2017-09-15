#!/usr/bin/env python

"""
./CBBLab01a.py <nucleotidesequence.fa>

Thanks to Justin for huge amounts of help getting this far.
"""

import sys
import fasta
import itertools
import matplotlib.pyplot as plt
import numpy as np
import math

codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

nucleotide = open(sys.argv[1])

dN = []

dS = []

#4871 represents the length of the protein sequence
# this is building lists that can be indexed later 
for i in range(0,4871):
    dN.append(0)
    dS.append(0)

# imports query and target sequences
nucleotide_seq = []
for ident, sequences in fasta.FASTAReader( nucleotide ):
    nucleotide_seq.append(sequences)

# list containing query sequence
query_seq = nucleotide_seq[:1]

# list of target sequences
target_seq = nucleotide_seq[1:]



#goes through and gets rid of 
for n in range(len(target_seq)):
    count = 0
    prot_count = 0
    while count < 14614:
        target = target_seq[n][count:count+3]
        query = query_seq[0][count:count+3]
        if "-" in target_seq[n][count:count+3]:
            count += 3
            prot_count += 1
        elif "-" in query_seq[0][count:count+3]:
            count += 3
            prot_count += 1
        elif target_seq[n][count:count+3] == query_seq[0][count:count+3]:
            count += 3
            prot_count += 1
        elif target not in codontable:
            count += 3
        elif codontable[target] != codontable[query]:
            dN[prot_count] = dN[prot_count] + 1
            count += 3
            prot_count += 1
        elif codontable[target] == codontable[query]:
            dS[prot_count] = dS[prot_count] + 1
            count += 3
            prot_count += 1
        else:
            print "Error in code"

dN_dS = [int(n) - int(s) for n,s in zip (dN, dS)]


mean_dN_dS = np.mean(dN_dS)
std_dev_dN_dS = np.std(dN_dS)
SE_dN_dS = std_dev_dN_dS / np.sqrt(len(dN_dS))
zscore_dN_dS = mean_dN_dS / std_dev_dN_dS


print std_dev_dN_dS
print mean_dN_dS
print SE_dN_dS
print zscore_dN_dS


non_zero_dN = []
non_zero_dS = []


for i in range(len(dN)):
    non_zero_dN.append(dN[i] + 1)
    non_zero_dS.append(dS[i] + 1)
#just testing to see if making everything non-zero might help

non_zero_dN_dS = [float(n)/float(s) for n,s in zip(non_zero_dN, non_zero_dS)]

mean_non_zero_dN_dS = np.mean(non_zero_dN_dS)
std_dev_non_zero_dN_dS = np.std(non_zero_dN_dS)
SE_non_zero_dN_dS = std_dev_non_zero_dN_dS / np.sqrt(len(non_zero_dN_dS))
zscore_non_zero_dN_dS = (mean_non_zero_dN_dS)-1 / SE_non_zero_dN_dS


zscore_list = []
for i in dN_dS:
    mean = i - mean_dN_dS
    zscore_list.append(mean / std_dev_dN_dS)
    

print zscore_list







log_non_zero_dN_dS = [np.log2(float(n)/float(s)) for n,s in zip(non_zero_dN, non_zero_dS)]
non_zero_dN_dS = [float(n)/float(s) for n,s in zip(non_zero_dN, non_zero_dS)]

mean_non_zero_dN_dS = np.mean(non_zero_dN_dS)
std_dev_non_zero_dN_dS = np.std(non_zero_dN_dS)
SE_non_zero_dN_dS = std_dev_non_zero_dN_dS / np.sqrt(len(non_zero_dN_dS))
zscore_non_zero_dN_dS = (mean_non_zero_dN_dS)-1 / SE_non_zero_dN_dS





print mean_non_zero_dN_dS
print std_dev_non_zero_dN_dS
print SE_non_zero_dN_dS
print zscore_non_zero_dN_dS
print max(non_zero_dN_dS)

plt.figure()
plt.scatter(range(len(log_non_zero_dN_dS)), log_non_zero_dN_dS)
plt.xlabel("Gene Locations")
plt.ylabel("dN/dS")
plt.savefig( "scatter_dN_dS" + ".png")
plt.close()
    
plt.figure()
plt.scatter(range(len(zscore_list)), zscore_list)
plt.xlabel("Gene Locations")
plt.ylabel("zscore")
plt.savefig( "zscore" + ".png")
plt.close()
    
