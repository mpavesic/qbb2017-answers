#!/usr/bin/env python




"""
$ tar xvf BYxRM_subset.tar.xv

$ twoBitToFa -udcDir=. http://hgdownload.cse.ucsc.edu/goldenPath/sacCer3/bigZips/sacCer3.2bit stdout > sacCer3.fa

$ bwa index sacCer3.fa
ouput - multiple files

$ bwa mem -R '@RG\tID:09\tSM:09' -o A01_09.sam sacCer3.fa A01_09.fastq 
bwa mem -R '@RG\tID:11\tSM:11' -o A01_11.sam sacCer3.fa A01_11.fastq 
bwa mem -R '@RG\tID:23\tSM:23' -o A01_23.sam sacCer3.fa A01_23.fastq 
bwa mem -R '@RG\tID:24\tSM:24' -o A01_24.sam sacCer3.fa A01_24.fastq 
bwa mem -R '@RG\tID:27\tSM:27' -o A01_27.sam sacCer3.fa A01_27.fastq 
bwa mem -R '@RG\tID:31\tSM:31' -o A01_31.sam sacCer3.fa A01_31.fastq 
bwa mem -R '@RG\tID:35\tSM:35' -o A01_35.sam sacCer3.fa A01_35.fastq 
bwa mem -R '@RG\tID:39\tSM:39' -o A01_39.sam sacCer3.fa A01_39.fastq 
bwa mem -R '@RG\tID:62\tSM:62' -o A01_62.sam sacCer3.fa A01_62.fastq 
bwa mem -R '@RG\tID:63\tSM:63' -o A01_63.sam sacCer3.fa A01_63.fastq 


$ samtools view A01_09.sam -b -o A01_09.bam -@ 4
samtools sort A01_09.bam -o A01_09_sorted.bam
samtools index -b A01_09_sorted.bam 
samtools view A01_11.sam -b -o A01_11.bam -@ 4
samtools sort A01_11.bam -o A01_11_sorted.bam
samtools index -b A01_11_sorted.bam
samtools view A01_23.sam -b -o A01_23.bam -@ 4
samtools sort A01_23.bam -o A01_23_sorted.bam
samtools index -b A01_23_sorted.bam
samtools view A01_24.sam -b -o A01_24.bam -@ 4
samtools sort A01_24.bam -o A01_24_sorted.bam
samtools index -b A01_24_sorted.bam
samtools view A01_27.sam -b -o A01_27.bam -@ 4
samtools sort A01_27.bam -o A01_27_sorted.bam
samtools index -b A01_27_sorted.bam 
samtools view A01_31.sam -b -o A01_31.bam -@ 4
samtools sort A01_31.bam -o A01_31_sorted.bam
samtools index -b A01_31_sorted.bam 
samtools view A01_35.sam -b -o A01_35.bam -@ 4
samtools sort A01_35.bam -o A01_35_sorted.bam
samtools index -b A01_35_sorted.bam 
samtools view A01_39.sam -b -o A01_39.bam -@ 4
samtools sort A01_39.bam -o A01_39_sorted.bam
samtools index -b A01_39_sorted.bam 
samtools view A01_62.sam -b -o A01_62.bam -@ 4
samtools sort A01_62.bam -o A01_62_sorted.bam
samtools index -b A01_62_sorted.bam 
samtools view A01_63.sam -b -o A01_63.bam -@ 4
samtools sort A01_63.bam -o A01_63_sorted.bam
samtools index -b A01_63_sorted.bam 


freebayes -f sacCer3.fa A01_09_sorted.bam A01_11_sorted.bam A01_23_sorted.bam A01_24_sorted.bam A01_27_sorted.bam A01_31_sorted.bam A01_35_sorted.bam A01_39_sorted.bam A01_62_sorted.bam A01_63_sorted.bam > output.vcf

vcffilter -f "QUAL > 20" output.vcf > results.vcf

Usage: ./CBBWeek3a.py results.vcf AlleleFrequencyHistogram

$ snpEff download R64-1-1.86
 Usage: snpEff [eff] [options] genome_version [input_file]
$ snpEff results.vcf
$ tail -n+83 results.vcf > headless_results.vcf
$ sort -k 6 -r -n headless_results.vcf > tophits.vcf
$ less -S tophits.vcf | head -5 > topfivehits.vcf

"""
import sys
import numpy as np
import matplotlib.pyplot as plt

vcf = open(sys.argv[1])

allele_frequency = []

for value in vcf:
    if value.startswith("#"):
        continue
    line = value.rstrip("\t\n").split()
    af_value = line[7].split(";")
    af_real = af_value[3][3:]
    af_end = af_real.split(",")
    for value in af_end:
        allele_frequency.append(float(value))
    # else:
#         fields = value.split(";")
#         # print fields[3]
#         freq = fields[3].split("=")
#         # print freq[1]
#         alleles = ()
#         for alleles in freq[1]:
#             alleles.append(int(freq[1])

plt.figure()
plt.hist(allele_frequency, bins=30)
plt.xlabel("Allele Frequency")
plt.ylabel("Occurences")
plt.title("Allele Frequency")
plt.savefig( sys.argv[2] + ".png")
plt.close()

"""
matplotlib.pyplot.hist(x, bins=None, range=None, normed=False, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, hold=None, data=None, **kwargs)
"""
