# Luc Boruta, 2011-2012
# This program is free software: you can redistribute it and/or modify it under
# the terms of the Do What The Fuck You Want To Public License, version 2.
# http://tinyurl.com/wtfpl
"""
This module provides a weighted implementation of Ester et al.'s (1996) DBSCAN 
algorithm. The main and only function is wdbscan(), which takes a dissimilarity
matrix and two reachability parameters and returns a density-based clustering of
arbitrary shape. This implementation accomodates instance weights, i.e. a core
object is not defined as an object whose epsilon-neighborhood contains at least
a given number of objects, but as an object whose epsilon-neighborhood weighs
a least a given weight. The weight of a given object's epsilon-neighborhood is
straightforwardly defined as the sum of the pairwise weights between this object
and each of its epsilon-neighbors. This implementation does not require weights
to be positive, so be careful what you wish for, you might just get it.

To use this module, you must have numpy installed.

Version 0.2: Aug. 28, 2012
	First GitHub version.

Version 0.1: Nov. 14, 2011
"""

import numpy

def wdbscan(dmatrix, epsilon, mu, weights=None, noise=True):
	"""
	Generates a density-based clustering of arbitrary shape. Returns a numpy
	array coding cluster membership with noise observations coded as 0.
	
	Positional arguments:
	dmatrix -- square dissimilarity matrix (cf. numpy.matrix, numpy.squareform,
	           and numpy.pdist).
	epsilon -- maximum reachability distance.
	mu      -- minimum reachability weight (cf. minimum number of points in the
	           classical DBSCAN).
	
	Keyword arguments:
	weights -- square weight matrix (if None, weights default to 1).
	noise   -- Boolean indicating whether objects that do not belong to any
	           cluster should be considered as noise (if True) or assigned to
	           clusters of their own (if False).
	"""
	n = len(dmatrix)
	ematrix = dmatrix <= epsilon # Epsilon-reachability matrix
	epsilon_neighborhood = lambda i : [j for j in xrange(n) if ematrix[i, j]]
	if weights is None:
		weights = numpy.ones(n, dtype=numpy.int) # Classical DBSCAN
	status = numpy.zeros(n, dtype=numpy.int) # Unclassified = 0
	cluster_id = 1 # Classified = 1, 2, ...
	for i in xrange(n):
		if status[i] == 0:
			seeds = epsilon_neighborhood(i)
			if weights[seeds].sum() < mu:
				status[i] = -1 # Noise = -1
			else: # Core point
				status[seeds] = cluster_id
				seeds.remove(i)
				while seeds:
					j = seeds[0]
					eneighborhood = epsilon_neighborhood(j)
					if weights[eneighborhood].sum() >= mu:
						for k in eneighborhood:
							if status[k] <= 0: # Unclassified or noise
								if status[k] == 0: # Unclassified
									seeds.append(k)
								status[k] = cluster_id
					seeds.remove(j)
				cluster_id += 1
	if not noise: # Assign cluster ids to noise
		noisy = (status == -1)
		status[noisy] = xrange(cluster_id, cluster_id + noisy.sum())
	return status

