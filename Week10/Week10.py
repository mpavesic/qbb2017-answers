#!/usr/bin/env python

"""


Usage: ./Week10.py hema_data.txt

"""


"""
The only thing you need to make sure is that you convert your data into a matrix X with n samples and m features, so that X.shape == (n, m).

"""

import sys
import math
import itertools
import numpy as np
import pandas as pd
import scipy.cluster.hierarchy as hac
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from sklearn import datasets
from sklearn.cluster import KMeans


infile = open(sys.argv[1],'r')

colHeaders = infile.next().strip().split()[1:]
rowHeaders = []
dataMatrix = []

for line in infile:
	data = line.strip().split('\t')
	rowHeaders.append(data[0])
	dataMatrix.append([float(x) for x in data[1:]])

#convert native data array into a numpy array
dataMatrixnp = np.array(dataMatrix) 

linkageMatrix = hac.linkage(dataMatrixnp, method = "average")
heatmapOrder = hac.leaves_list(linkageMatrix)

linkageMatrix_transposed = hac.linkage(dataMatrixnp.T, method = "average")
heatmapOrder_transposed = hac.leaves_list(linkageMatrix_transposed)

orderedDataMatrix = dataMatrixnp[heatmapOrder,:][:, heatmapOrder_transposed]
# rowHeaders = np.array(rowHeaders)
# orderedRowHeaders = rowHeaders[heatmapOrder,:]
labels = np.array(['CFU', 'poly', 'unk', 'int', 'mys', 'mid'])
labels_t = labels[ heatmapOrder_transposed]
plt.figure()
plt.imshow(orderedDataMatrix, aspect='auto', interpolation='nearest')
plt.grid( False )
plt.title("Heatmap of Iris characteristics")
plt.colorbar()
plt.xticks( [ x for x in range(6) ], labels_t) 
plt.savefig("week10_heatmap.png") # Save the image
plt.close()


plt.figure()
hac.dendrogram(linkageMatrix_transposed, labels=labels )
plt.savefig( 'dendrogram10.png' )
plt.close()


kmeans = KMeans( n_clusters=5, random_state=0 )
kmeans.fit( dataMatrixnp )
labels = kmeans.predict( dataMatrixnp )
dataMatrix_df = pd.merge( pd.DataFrame(dataMatrixnp, columns = ['CFU', 'poly', 'unk', 'int', 'mys', 'mid']), pd.DataFrame( labels, columns=['cluster'] ), left_index=True, right_index=True )
k_clustered = dataMatrix_df.sort_values('cluster')[['CFU', 'poly', 'unk', 'int', 'mys', 'mid']].values

plt.figure()
plt.imshow(k_clustered, aspect='auto', interpolation='nearest')
plt.grid( False )
plt.title("Heatmap of Iris characteristics")
plt.colorbar()
plt.xticks( [ x for x in range(6) ], labels_t) 
plt.savefig("week10_k_clustered.png") # Save the image
plt.close()


