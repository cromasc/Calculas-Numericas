def x1(x2,x3): return round(7/5 - 2*x2/5 - x3/5 ,6)
def x2(x1,x3): return round(3/4 + x1/4 - x3/2 ,6)
def x3(x1,x2): return round(-1/10 - x1/5 + 3*x2/10 ,6)

def erro(xk0: list, xk1: list): return [abs(xk1[i]-xk0[i]) for i in range(len(xk0))]

def iteracao(E, xk0 = [0,0,0], k = -1):

    a = x1(xk0[1], xk0[2])
    b = x2(a, xk0[2])
    c = x3(a, b)
    
    xk1 = [a, b, c]
    k += 1

    return (xk1,k) if max(erro(xk0,xk1)) < E else iteracao(E, xk1, k)

print(iteracao(10**-2))