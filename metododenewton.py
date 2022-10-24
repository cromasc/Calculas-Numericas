from numpy import log

def _f(x: float) -> float: return round(950*log(200/(200-3*x)) - 9.8*x - 500, 5)
def _flinha(x: float) -> float: return round((4450+147*x)/(1000-15*x), 5)

def erro(x0: float,x1: float) -> float: return round(abs(x1-x0)/x1, 7)

def newton(x0: float, f: function, flinha: function, E: float, k: int = -1) -> tuple[float, int]:
    k += 1

    x = x0 - f(x0)/flinha(x0)
    return (round(x,5),k) if erro(x0,x) <= E else newton(x, f, flinha, E, k)

print(newton(17.5, _f, _flinha, 10**-6))