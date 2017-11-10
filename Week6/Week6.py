

$ gunzip http://jamestaylor.org/outgoing/g1e.tar.xz
$ tar -xzf g1e.tar.xz
v = verbose
x = compressed
z = compression in addition to tar
f = folder output

Reads:
Experimental
CTCF_ER4.fastq (after differentiation)
CTCF_G1E.fastq (before differentiation)
Control
input_ER4.fastq
input_G1E.fastq

Mus chromosome 19 from http://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr19.fa.gz
fa file is both upper and lower case, with many N at beginning and end of file

first step is always to index when using a genome:
bowtie2-build [options]* <reference_in> <bt2_base>
$ bowtie2-build -f chr19.fa chr19

Map reads to index:
bowtie2
USAGE: bowtie2 -x <inputindex> -U <input> -S <output>

$ bowtie2 -q -x chr19 -U CTCF_ER4.fastq -S CTCF_ER4.sam
$ bowtie2 -q -x chr19 -U CTCF_G1E.fastq -S CTCF_G1E.sam
$ bowtie2 -q -x chr19 -U input_ER4.fastq -S input_ER4.sam
$ bowtie2 -q -x chr19 -U input_G1E.fastq -S input_G1E.sam

Call peaks:
macs2 callpeak -t <input file> -c <control file> -g 61000000 -f BED
-t input file
-c control file
-f BED

$ macs2 callpeak -t CTCF_ER4.sam -g 61000000 --outdir "/Users/cmdb/qbb2017-answers/Week6/Peaks_CTCF_ER4_nocontrol"
$ macs2 callpeak -t CTCF_ER4.sam -c input_ER4.sam -g 61000000 --outdir "/Users/cmdb/qbb2017-answers/Week6/Peaks_CTCF_ER4"
$ macs2 callpeak -t CTCF_G1E.sam -g 61000000 --outdir "/Users/cmdb/qbb2017-answers/Week6/Peaks_CTCF_G1E_nocontrol"
$ macs2 callpeak -t CTCF_G1E.sam -c input_G1E.sam -g 61000000 --outdir "/Users/cmdb/qbb2017-answers/Week6/Peaks_CTCF_G1E"

Output directories: multiple files, especially one with ".narrowPeak" suffix
---not done yet---
bedtools combinations on the narrowPeak file
$ bedtools intersect -v -a ~/qbb2017-answers/Week6/Peaks_CTCF_ER4/NA_peaks.narrowPeak -b ~/qbb2017-answers/Week6/Peaks_CTCF_G1E/NA_peaks.narrowPeak > diff_bands_ER4vsG1E.txt

$ bedtools intersect -v -header -a ~/qbb2017-answers/Week6/Peaks_CTCF_G1E/NA_peaks.narrowPeak -b ~/qbb2017-answers/Week6/Peaks_CTCF_ER4/NA_peaks.narrowPeak > diff_bands_G1EvsER4.txt

$ bedtools intersect -v -header -a ~/qbb2017-answers/Week6/Peaks_CTCF_ER4_nocontrol/NA_peaks.narrowPeak -b ~/qbb2017-answers/Week6/Peaks_CTCF_G1E_nocontrol/NA_peaks.narrowPeak > diff_bands_ER4vsG1E_nocont.txt

$ bedtools intersect -v -header -a ~/qbb2017-answers/Week6/Peaks_CTCF_G1E_nocontrol/NA_peaks.narrowPeak -b ~/qbb2017-answers/Week6/Peaks_CTCF_ER4_nocontrol/NA_peaks.narrowPeak > diff_bands_G1EvsER4_nocont.txt

=======
Get the top 100 to upload for homework
$ head -100 diff_bands_ER4vsG1E.txt > diff_bands_G1EvsER4_100.txt
$ head -100 diff_bands_ER4vsG1E_nocont.txt > diff_bands_G1EvsER4_nocont_100.txt
$ head -100 diff_bands_G1EvsER4.txt > diff_bands_ER4vsG1E_100.txt
$ head -100 diff_bands_G1EvsER4_nocont.txt > diff_bands_ER4vsG1E_nocont_100.txt

sort the 100 hits out before running the meme-chip

$ sort -k 9 -r -n ~/qbb2017-answers/Week-6/ER4_No_Control/NA_peaks.narrowPeak | head -100 > ER4_nocontrol_meme_100
$ sort -k 9 -r -n ~/qbb2017-answers/Week-6/ER4_Control/NA_peaks.narrowPeak | head -100 > ER4_control_meme_100
$ sort -k 9 -r -n ~/qbb2017-answers/Week-6/G1E_No_Control/NA_peaks.narrowPeak | head -100 > G1E_nocontrol_meme_100
$ sort -k 9 -r -n ~/qbb2017-answers/Week-6/G1E_Control/NA_peaks.narrowPeak | head -100 > G1E_control_meme_100

make these fasta files
$ bedtools getfasta -fi ~/qbb2017-answers/Week6/chr19.fa -bed ER4_control_meme_100 > ER4_control_meme.fa
$ bedtools getfasta -fi ~/qbb2017-answers/Week6/chr19.fa -bed ER4_nocontrol_meme_100 > ER4_nocontrol_meme.fa

get meme-chip to run
/usr/local/opt/meme/bin/meme-chip -meme-maxw 20 -db motif_databases/JASPAR/JASPAR_CORE_2016_vertebrates.meme ER4_control_meme.fa
/usr/local/opt/meme/bin/meme-chip -meme-maxw 20 -db motif_databases/JASPAR/JASPAR_CORE_2016_vertebrates.meme ER4_nocontrol_meme.fa

