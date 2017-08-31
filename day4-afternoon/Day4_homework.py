#!/usr/bin/env python

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

"""
Usage:  ./00-boxplot.py <samples.csv> <ctab_dir> <replicate.csv>
~/qbb2017/samples.csv
~/data/results/stringtie/
~/qbb2017/replicates.csv

Time Course w/ Replicates
Add a second series of FBtr0331261 abundance to the same plot, this time for male samples.
style it similarly to Lott et al., 2011 PLoS Biology (i.e. x-axis tick labels, color, 
legend, etc.)

add stage 14 replicates to the same plot (~/qbb2017/replicates.csv)

HINT: since there are only replicates for 14A/B/C/D, you will need to "skip" plotting 
10/11/12/13
HINT: plt.plot( x, y, 'o' )
Submit your two Python scripts, with instructions needed to run them in a documentation 
comment, and the plots that they generate.

"""

transcript = "FBtr0331261"

#SERIES 1 - Female samples
df_fsamples = pd.read_csv(sys.argv[1])
fsoi = df_fsamples["sex"] == "female"

f_fpkms = []

for fsample in df_fsamples["sample"][fsoi]:
    fname = os.path.join(sys.argv[2], fsample, "t_data.ctab")
    df = pd.read_csv( fname, sep="\t")
    froi = df["t_name"] == transcript
    f_fpkms.append(df[froi]["FPKM"].values)
# print f_fpkms

#SERIES 2 - Male samples
df_msamples = pd.read_csv(sys.argv[1])
msoi = df_msamples["sex"] == "male"

m_fpkms = []

for msample in df_msamples["sample"][msoi]:
    fname = os.path.join(sys.argv[2], msample, "t_data.ctab")
    df = pd.read_csv( fname, sep="\t")
    mroi = df["t_name"] == transcript
    m_fpkms.append(df[mroi]["FPKM"].values)
# print m_fpkms


#SERIES 3 - REPLICATES

df_RFsamples = pd.read_csv(sys.argv[3])
RFsoi = df_RFsamples["sex"] == "female"

RF_fpkms = []
while len(RF_fpkms) < 4:
    RF_fpkms.append(None)
for RFsample in df_RFsamples["sample"][RFsoi]:
        fname = os.path.join(sys.argv[2], RFsample, "t_data.ctab")
        df = pd.read_csv( fname, sep="\t")
        RFroi = df["t_name"] == transcript
        RF_fpkms.append(df[RFroi]["FPKM"].values)
# print RF_fpkms


df_RMsamples = pd.read_csv(sys.argv[3])
RMsoi = df_RMsamples["sex"] == "male"

RM_fpkms = []
while len(RM_fpkms) < 4:
    RM_fpkms.append(None)
for RMsample in df_RMsamples["sample"][RMsoi]:
    fname = os.path.join(sys.argv[2], RMsample, "t_data.ctab")
    df = pd.read_csv( fname, sep="\t")
    RMroi = df["t_name"] == transcript
    RM_fpkms.append(df[RMroi]["FPKM"].values)
# print RM_fpkms



plt.figure()
plt.plot( f_fpkms, color='r', lw=4)
plt.plot( m_fpkms, color='b', lw=4)
plt.plot( RF_fpkms, 'r^', markersize = 12)
plt.plot( RM_fpkms, 'b^', markersize = 12)
plt.xticks(range(len(f_fpkms)), df_fsamples["stage"], rotation = 90)
plt.xlabel("developmental stage")
plt.ylabel("mRNA abundance FPKM")
plt.title("Sxl")
plt.gca().tick_params(direction='out', top='off', right='off')
art=[]
plt.legend(['females', 'males', 'female replicates', 'male replicates'], loc='center right', bbox_to_anchor =(1.5,0.5), frameon = False, numpoints = 1)
plt.savefig( "Day4.png", additional_artists=art, bbox_inches="tight")
plt.close()