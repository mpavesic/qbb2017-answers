#!/usr/bin/env python

import sys

f = open(sys.argv[1])
#create mapping dictionary from mapping file from exercise 1 ~/day2-exercise1.out
mappingdictionary = {}

for line in f:
    (key, val) = line.split()
    mappingdictionary[key] = val
#print mappingdictionary


g = open(sys.argv[2])
# input from /Users/cmdb/data/genomes/t_data.ctab
## column 9 = gene_name

for line in g:
    fields = line.split('\t')
    fbgn = fields[8]
    if fbgn in mappingdictionary:
        uniprot = mappingdictionary[fbgn]
    else:
        uniprot = "NA"
    fields[8] = uniprot
    #slower method:   
    # for (key, val) in mappingdictionary.iteritems():
    #     if key == fields[8]:
    #         fields[8] = val
    # for key in mappingdictionary:
    #     if key == fields[8]:
    #         fields[8] = mappingdictionary[key]
    #opposite of split. un-ugly the list created by split 
    print "\t".join(fields)
