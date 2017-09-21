#!/usr/bin/env python


"""

reads_low_1.fastq
reads_low_2.fastq

velveth/velvetg
$ time velveth reads_low_1_kmer.fastq 29 -short -fastq reads_low_1.fastq 
real	0m0.077s
user	0m0.034s
sys	0m0.035s
$ time velvetg reads_low_1_kmer.fastq 
real	0m0.088s
user	0m0.053s
sys	0m0.023s
output: 
Final graph has 205 nodes and n50 of 122, max 535, total 22819, using 0/1000 reads

$ time velveth reads_low_2_kmer.fastq 33 -short -fastq reads_low_2.fastq 
real	0m0.071s
user	0m0.032s
sys	0m0.033s
$ time velvetg reads_low_2_kmer.fastq
real	0m0.087s
user	0m0.052s
sys	0m0.024s
output: 
Final graph has 194 nodes and n50 of 116, max 683, total 20956, using 0/1000 reads


SPAdes
$ time spades.py -o SPAdes --sc --12 reads_low_1.fastq
real	0m3.715s
user	0m2.801s
sys	0m1.125s
$ time spades.py -o SPAdes --sc --12 reads_low_2.fastq
real	0m3.009s
user	0m2.595s
sys	0m1.057s
"""

"""
Parse a single FASTA record from stdin and prints it.
usage: ./00-parse-one-fasta.py < input.fa > output
"""

