import numpy as np
import pandas as pd
from advstats import clust

#Tests for population mean and variance from a cluster sample

#data used for tests
cluster1 = [3.08, 2.60, 3.44, 3.04]
cluster2 = [2.36, 3.04, 3.28, 2.68]
cluster3 = [2.00, 2.56, 2.52, 1.88]
cluster4 = [3.00, 2.88, 3.44, 3.64]
cluster5 = [2.68, 1.92, 3.28, 3.20]
grades = cluster1 + cluster2 + cluster3 + cluster4+ cluster5
labels = np.array(["cluster1", "cluster2", "cluster3", "cluster4", "cluster5"])
cluster = np.repeat(labels, [len(cluster1), len(cluster2), len(cluster3), len(cluster4), len(cluster5)], axis=0)

#tests for when user doesn't provide a table but instead supplies cluster means or cluster totals, mean of cluster sample, and mean cluster size for variance
M = {"cluster1": np.mean(cluster1), "cluster2": np.mean(cluster2), "cluster3": np.mean(cluster3), "cluster4": np.mean(cluster4), "cluster5": np.mean(cluster5)}
T = {"cluster1": np.sum(cluster1), "cluster2": np.sum(cluster2), "cluster3": np.sum(cluster3), "cluster4": np.sum(cluster4), "cluster5": np.sum(cluster5)}

#for mean
np.testing.assert_almost_equal(float(clust.mean(M = M)), 2.826)
#for variance
np.testing.assert_almost_equal(float(clust.var(N = 100, T = T, M = float(clust.mean(M = M)), C = 4)), 0.0267862)
print()

#tests for when user provides a table that stores data vertically (all clusters and responses are in one column):
sample0 = pd.DataFrame()
sample0["grades"] = grades
sample0["cluster"] = cluster

#for mean
np.testing.assert_almost_equal(float(clust.mean(data = sample0, x = "cluster")), 2.826)
#for variance
np.testing.assert_almost_equal(float(clust.var(N = 100, data = sample0, x = "cluster")), 0.0267862)


#tests for when user provides a table that stores data vertically (each cluster is a column):
sample1 = pd.DataFrame()
sample1["cluster1"] = cluster1
sample1["cluster2"] = cluster2
sample1["cluster3"] = cluster3
sample1["cluster4"] = cluster4
sample1["cluster5"] = cluster5

#for mean
np.testing.assert_almost_equal(float(clust.mean(data = sample1)), 2.826)
#for variance
np.testing.assert_almost_equal(float(clust.var(N = 100, data = sample1)), 0.0267862)