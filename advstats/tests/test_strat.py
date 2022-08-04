import numpy as np
import pandas as pd
from advstats import strat

#Tests for population mean and variance from a stratified sample

#data used for tests
TownA = [35, 43, 36, 39, 28, 28, 29, 25, 38, 27, 26, 32, 29, 40, 35, 41, 37, 31, 45, 34]
TownB = [27, 15, 4, 41, 49, 25, 10, 30]
Rural = [8, 14, 12, 15, 30, 32, 21, 20, 34, 7, 11, 24]
tv_viewing = TownA + TownB + Rural
labels = np.array(["TownA", "TownB", "Rural"])
stratum = np.repeat(labels, [len(TownA), len(TownB), len(Rural)], axis=0)
Population = {"TownA": 155, "TownB": 62, "Rural": 93}

#tests for when user doesn't provide a table but instead supplies strautum means, size and population sizes

M = {"TownA": np.mean(TownA), "TownB": np.mean(TownB), "Rural": np.mean(Rural)}
V = {"TownA": np.var(TownA, ddof=1), "TownB": np.var(TownB, ddof=1), "Rural": np.var(Rural, ddof=1)}
n = {"TownA": len(TownA), "TownB": len(TownB), "Rural": len(Rural)}

#for mean
np.testing.assert_almost_equal(float(strat.mean(N = Population, M = M)), 27.675)
#for variance
np.testing.assert_almost_equal(float(strat.var(N = Population, n = n, V = V)), 1.969519, decimal= 5)

#Tests for when data is presented vertically (all stratum are in one column), x (what column to group data with) is given:

sample1 = pd.DataFrame()
sample1["viewership"] = tv_viewing
sample1["stratum"] = stratum
sample1.head()

#for mean
np.testing.assert_almost_equal(float(strat.mean(data = sample1, N = Population, x = "stratum")), 27.675)
#for variance
np.testing.assert_almost_equal(float(strat.var(data = sample1, N = Population, x = "stratum")), 1.969519, decimal= 5)

#Tests for when data is presented horizontally (each stratum is a column), and x is not given:

sample2 = pd.DataFrame()
sample2["TownA"] = pd.Series(TownA)
sample2["TownB"] = pd.Series(TownB)
sample2["Rural"] = pd.Series(Rural)
sample2.head()

#for mean
np.testing.assert_almost_equal(float(strat.mean(data = sample2, N = Population)), 27.675)
#for variance
np.testing.assert_almost_equal(float(strat.var(data = sample2, N = Population)), 1.969519, decimal= 5)

