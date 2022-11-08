from numpy import mean, e, log, cos

def _f(x: float) -> float: return (e**(-2*x)) - x
def _f2(x: float) -> float: return round(950*log(200/(200-3*x)) - 9.8*x - 500, 5)
def _f3(x: float) -> float: return round(x - cos(x), 7)
def _f4(x: float) -> float: return round(x**2 - 2, 7)

def bissecao(intervalo: list, f, E) -> (tuple | str):
    if f(intervalo[0])*f(intervalo[1]) > 0: return "Não existe raíz no intervalo"

    i = 0
    while intervalo[1] - intervalo[0] > E:
        i += 1

        xbarra = round(mean(intervalo),6)
        ...
        if f(xbarra) < 0 and f(intervalo[0]) < 0:
            intervalo[0] = xbarra
        elif f(xbarra) < 0 and f(intervalo[0]) > 0:
            intervalo[1] = xbarra
        elif f(xbarra) > 0 and f(intervalo[1]) > 0:
            intervalo[1] = xbarra
        elif f(xbarra) > 0 and f(intervalo[1]) < 0:
            intervalo[0] = xbarra
        else:
            break
    ...
    return mean(intervalo), i

print(bissecao([0.25,2], _f4, 10**-4))