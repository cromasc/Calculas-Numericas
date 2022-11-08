from numpy import log, cos, sin

def _f(x): return round(950*log(200/(200-3*x)) - 9.8*x - 500, 5)
def _flinha(x): return round((4450+147*x)/(1000-15*x), 5)

def _f2(x): return round(x**2 - 2, 7)
def _f2linha(x): return round(2*x,7)

def _f3(x): return round(x - cos(x), 7)
def _f3linha(x): return round(1 + sin(x),7)

def raiz5(x): return (x**2 - 5)
def raiz5l(x): return 2*x

def erro(x0,x1): return round(abs(x1-x0)/x1, 7)

def newton(x0, f, flinha, E, k = -1):
    k += 1

    x = x0 - f(x0)/flinha(x0)
    return (round(x,10),k) if erro(x0,x) <= E else newton(x, f, flinha, E, k)

x, e = newton(1.25, raiz5, raiz5l, 10**-10)

print((1+x)/2)