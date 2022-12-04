# sistema = [
#     [1,1,3,5],
#     [1,3,1,6],
#     [1,3,6,1]
# ]

def x1(x2,x3): return round((14 - (-2*x2 - 4*x3))/20 ,6)
def x2(x1,x3): return round((25 - (-4*x1 + 4*x3))/25 ,6)
def x3(x1,x2): return round((38 - (-4*x1 - 8*x2))/50 ,6)

def erro(xk0: list, xk1: list): return [abs(xk1[i]-xk0[i]) for i in range(len(xk0))]

def iteracao(E, xk0 = [0,0,0], k = -1):
    
    xk1 = [x1(xk0[1], xk0[2]), x2(xk0[0], xk0[2]), x3(xk0[0], xk0[1])]
    k += 1

    return (xk1,k) if max(erro(xk0,xk1)) < E else iteracao(E, xk1, k)

print(iteracao(10**-2))

# a = [round(x1(a[1], a[2]),6), round(x2(a[0], a[2]),6), round(x3(a[0], a[1]),6)]