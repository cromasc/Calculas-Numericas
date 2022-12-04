from numpy import linalg

def matriz_aumentada(matriz: list[list]):
    if len(matriz) != len(matriz[0]): 
        print("Matriz não quadrada")
        exit()
    elif round(linalg.det(matriz),5) == 0: 
        print("Matriz singular")
        exit()
    else:
        for i in range(len(matriz)):
            for j in range(len(matriz),2*len(matriz)):
                matriz[i].append(0) if i != j-len(matriz) else matriz[i].append(1)
    
        return matriz

def gauss(matriz: list[list]):
    for pivot in range(len(matriz)):
            for linha in range(len(matriz)):
                if matriz[pivot][pivot] != 0 and pivot != linha: 
                    m = matriz[linha][pivot]/matriz[pivot][pivot]

                    for coluna in range(len(matriz[linha])): 
                        matriz[linha][coluna] = round(matriz[linha][coluna] - m*matriz[pivot][coluna],3)
                else: pass
    zeros = 0
    for n in range(len(matriz)-1): 
        if matriz[n][n] == 0: zeros += 1
    
    while zeros>0:
        for n in range(len(matriz)-1):
            if matriz[n][n] == 0:
                aux = matriz[n]
                matriz[n] = matriz[n+1]
                matriz[n+1] = aux
                zeros -= 1
    
    return matriz

def balanceamento(matriz: list[list]):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] != 1 and matriz[i][j] != 0:
                m = matriz[i][j]

                for coluna in range(len(matriz[i])): 
                    matriz[i][coluna] = round(matriz[i][coluna]/m,3)
    return matriz


def inversa(m: list[list]) -> list[list]: 
    resultado = []
    for i in balanceamento(gauss(matriz_aumentada(m))):
        resultado.append(i[len(m):2*len(m)])
    return resultado

l = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for i in inversa(l):
    print(i)