#!/usr/bin/env python
"""
TSV file obtained with:
$ ./blastn -db nr -query /Users/cmdb/Downloads/week1_query.fa -out blast_alignment.tsv -evalue 0.0001 -ungapped -outfmt "6 sseqid sseq" -max_target_seqs 1000 -remote

FASTA converted with:
/Users/cmdb/qbb2017/CBB_Lab $ less blast_alignment.tsv | awk -F '\t' '{gsub(/-/, ""); print ">"$1 "\n" $2}' > 1000_homologs.fa

/Users/cmdb/qbb2017/CBB_Lab $ brew install emboss

/Users/cmdb/qbb2017/CBB_Lab $ transeq 1000_homologs.fa 1000_h_prot.fa

/Users/cmdb/qbb2017/CBB_Lab $ mafft 1000_h_prot.fa > alignment_prot.fa

Usage: ./CBBLab01.py 1000_homologs.fa alignment_prot.fa
"""


import sys
import fasta 

nucleo = open(sys.argv[1])
# 1000_homologs.fa
amino = open(sys.argv[2])
# alignment_prot.fa

# list to hold the peptide sequences:
amino_sequence = []
# place-holder for the FASTA identifier:
p_fast_ident = []

# bring two pieces of info from <alignment_prot.fa> into established libraries
for ident, sequence in fasta.FASTAReader(amino):
    amino_sequence.append(sequence)
    p_fast_ident.append(ident)

nucleotide_sequence = []

# bring in sequence data from <1000_homologs.fa>
for ident, sequence in fasta.FASTAReader(nucleo):
    nucleotide_sequence.append(sequence)
print "asdf"
# output FASTA file with corrected sequences
for i in range(len(amino_sequence)):
    codon_position = 0
    new_sequence = ""
    print ">" + p_fast_ident[i]
    for a in amino_sequence[i]:
        if a == "-":
            new_sequence += "---"
        else:
            new_sequence += nucleotide_sequence[i][codon_position:codon_position+3]
            codon_position += 3
    print new_sequence


