import pandas as pd


class strat:
    def mean(N, M=None, data=None, x=None):
        SumN = sum(N.values())
        if M is not None:
            return (pd.Series(N) * pd.Series(M)).sum() / SumN
        elif x is not None and data is not None:
            return data.groupby(x).mean().mul(N, axis=0).sum() / SumN
        else:
            return (data.mean() * pd.Series(N)).sum() / SumN

    def var(N, n=None, V=None, data=None, x=None):
        SumN = sum(N.values())
        NSquared = {k: v**2 for (k, v) in N.items()}
        SumNSquared = SumN**2
        if V is not None:
            V = pd.Series(V)
            N = pd.Series(N)
            n = pd.Series(n)
            NSquared = pd.Series(NSquared)
            a = 1 - n / N
            b = V * NSquared / n
            return (a * b).sum() / (SumNSquared)
        elif x is not None and data is not None:
            g = data.groupby(x)
            n = g.count()
            a = 1 - n.div(N, axis=0)
            b = g.var().mul(NSquared, axis=0) / n
            return (a * b).sum() / SumNSquared
        else:
            a = 1 - data.count() / pd.Series(N)
            b = data.var() * pd.Series(NSquared) / data.count()
            return (a * b).sum() / SumNSquared

    def prop(N, P=None, data=None, x=None, y=None, aff="Yes"):
        SumN = sum(N.values())
        if P is not None:
            return (pd.Series(N) * pd.Series(P)).sum() / SumN
        if data is not None and x is not None:
            return (
                (data[data[y] == aff].groupby(x).count() / data.groupby(x).count()).mul(
                    N, axis=0
                )
            ).sum() / SumN
        else:
            return (
                data[data == aff].count() / data.count() * pd.Series(N)
            ).sum() / SumN

    def propvar(N, n=None, P=None, data=None, x=None, y=None, aff="Yes"):
        NSquared = {k: v**2 for (k, v) in N.items()}
        SumNSquared = sum(N.values()) ** 2
        if P is not None and N is not None:
            P = pd.Series(P)
            N = pd.Series(N)
            n = pd.Series(n)
            NSquared = pd.Series(NSquared)
            return (NSquared * (1 - n / N) * (P * (1 - P)) / (n - 1)).sum() / (
                SumNSquared
            )
        if data is not None and x is not None:
            n = data.groupby(x).count()
            P = data[data[y] == aff].groupby(x).count() / n
            return ((1 - n.div(N, axis=0)) * (P * (1 - P)) / (n - 1)).mul(
                NSquared, axis=0
            ).sum() / SumNSquared
        else:
            NSquared = pd.Series(NSquared)
            N = pd.Series(N)
            n = data.count()
            P = data[data == aff].count() / n
            return (NSquared * (1 - n / N) * (P * (1 - P)) / (n - 1)).sum() / (
                SumNSquared
            )

    def optimal(data, N, C=None, x=None):
        pass
