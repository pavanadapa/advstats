import pandas as pd 

class clust():
  def mean(M = None, data = None, x = None):
    if M is not None:
      return pd.Series(M).sum()/len(M)
    elif data is not None and x is not None:
      g = data.groupby(x)
      return (g.mean()/g.ngroups).sum()
    else:
      return (data.mean()/data.shape[1]).sum()

  def var(N, T = None, M = None, C = None, data = None, x = None):
    if T and M is not None:
      n = len(T)
      s = (1/(n-1)*(pd.Series(T)-M*C)**2).sum()
      return (1-n/N)*s/(n*C**2)
    elif data is not None and x is not None:
      g = data.groupby(x)
      n = g.ngroups
      N = N
      c = g.count().mean()
      s = (((g.sum()-clust.mean(data = data, x = x)*c)**2)/(n-1)).sum()
      return (1-n/N)*s/(n*c**2)
    else:
      g = data
      N = N
      n = data.shape[1]
      c = data.count().mean()
      s = (((g.sum()-clust.mean(data = data)*c)**2)/(n-1)).sum()
      return (1-n/N)*s/(n*c**2)