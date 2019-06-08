# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 10:16:46 2019

@author: Aaron Edwards
"""

#KMeans Clustering 
import numpy as np
from numpy import random, array 
from numpy import random, float 
import matplotlib.pyplot  as plt
from sklearn import cluster 
from sklearn.cluster import KMeans 
from sklearn.preprocessing import scale 



def createClusteredData(N, k):
    random.seed(10)
    pointsPerCluster = float(N)/k
    X = []
    for i in range (k):
        incomeCentroid = random.unform(20000.0, 200000.0)
        ageCentroid = random.uniform(20.0, 70.0)
        
    for j in range (int(pointsPerCluster)):
        X.append([np.random.normal(incomeCentroid, 10000.0), 
        np.random.normal(ageCentroid, 2.0)])
    
    data = createClusteredData(100, 5)
    model = KMeans(n_cluster= 5 )
    
    print(model.labels_)
    plt.figure(figsize=(8,6))
    plt.scatter(data[:0], data[:1], c=model.labels_.astype(float))
    plt.show()
                   