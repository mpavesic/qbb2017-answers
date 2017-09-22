#!/usr/bin/env python


"""
reads_low_1.fastq
reads_low_2.fastq

velveth/velvetg
$ time velveth velvetoutput 31 -fastq reads_low_1.fastq reads_low_2.fastq -short 

output: 
w_1.fastq reads_low_2.fastq
[0.000000] Reading FastQ file reads_low_1.fastq;
[0.004280] 1000 sequences found
[0.004289] Done
[0.004656] Reading FastQ file reads_low_2.fastq;
[0.007360] 1000 sequences found
[0.007367] Done
[0.008170] Reading read set file velvetoutput/Sequences;
[0.008647] 2000 sequences found
[0.011898] Done
[0.011910] 2000 sequences in total.
[0.012207] Writing into roadmap file velvetoutput/Roadmaps...
[0.014410] Inputting sequences...
[0.014422] Inputting sequence 0 / 2000
[0.082498]  === Sequences loaded in 0.068090 s
[0.082617] Done inputting sequences
[0.082622] Destroying splay table
[0.087440] Splay table destroyed

real	0m0.096s
user	0m0.051s
sys	0m0.037s

$ time velvetg velvetoutput
Final graph has 306 nodes and n50 of 233, max 968, total 47835, using 0/2000 reads

real	0m0.141s
user	0m0.093s
sys	0m0.025s

SPAdes
$ time spades.py --12 reads_low_1.fastq --12 reads_low_2.fastq -o SPAdes
real	0m3.990s
user	0m4.118s
sys	0m1.199s
"""



