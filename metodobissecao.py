from numpy import mean, e

def _f(x): return e**(-2*x) - x

def bissecao(intervalo, f):
    if f(intervalo[0])*f(intervalo[1]) > 0: return "Não existe raíz no intervalo"

    i = 0
    while intervalo[1] - intervalo[0] > 10**-5:
        i += 1
        xbarra = round(mean(intervalo),6)

        if f(xbarra) < 0:
            intervalo[0] = xbarra
        elif f(xbarra) > 0:
            intervalo[1] = xbarra
        else:
            break

    return mean(intervalo), i

print(bissecao([-1,0.5], _f))