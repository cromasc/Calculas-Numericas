from numpy import cos

def _f(x: float) -> float: return round(cos(x), 7)

def erro(x0,x1): return round(abs(x1-x0)/x1, 7)

def iteracao(x0, f, E, k = -1):
    k += 1

    x = f(x0)
    return (round(x,10),k) if erro(x0,x) <= E else iteracao(x, f, E, k)


print(iteracao(1.25, _f, 10**-6))