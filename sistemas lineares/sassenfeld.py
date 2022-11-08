from numpy import absolute, matrix

m = [
    [1, -1/5, 3/5],
    [-1/4, 1, 3/4],
    [2/6, 4/6, 1]
]

def ssf(m):
    b1 = abs(m[0][1]) + abs(m[0][2])
    b2 = b1*abs(m[1][0]) + abs(m[1][2])
    b3 = b1*abs(m[2][0]) * b2*abs(m[2][1])

    return "Funciona" if max((b1,b2,b3)) < 1 else "Não Funciona"

print(ssf(m))