def gauss(matriz: list):
    if len(matriz) != len(matriz[1])-1: return None
    else:
        for pivot in range(len(matriz)-1):
            for linha in range(pivot+1,len(matriz)):
                if matriz[pivot][pivot] != 0: m = matriz[linha][pivot]/matriz[pivot][pivot]
                else: pass

                for coluna in range(len(matriz[linha])):
                    matriz[linha][coluna] = round(matriz[linha][coluna] - m*matriz[pivot][coluna],3)

        t = 0
        for i in range(len(matriz)-1): 
            if matriz[i][i] == 0: t += 1
        while t>0:
            for i in range(len(matriz)-1):
                if matriz[i][i] == 0:
                    aux = matriz[i]
                    matriz[i] = matriz[i+1]
                    matriz[i+1] = aux
                    t -= 1
        return matriz
            
def somalinha(linha: list, solucoes: list):
    n = 0

    intervalo = list(range(len(linha)-len(solucoes), len(linha)))
    intervalo.reverse()

    for i in intervalo:
        n += linha[i]*solucoes[i]
    return n

def resolver(matriz: list):
    if matriz[len(matriz)-1][len(matriz)-1] == 0: return "Sistema Impossível"
    elif matriz[1][0] == matriz[2][0] == matriz[2][1] == 0:
        n = list(range(len(matriz)))
        n.reverse()

        solucao = [0 for _ in range(len(matriz))]

        for i in n: solucao[i] = round((matriz[i][len(matriz)]-(somalinha(matriz[i][:len(matriz)],solucao)))/matriz[i][i],3)

        return solucao
    else: return None

sistema = [
    [3,3,1,7],
    [2,2,-1,3],
    [1,-1,5,5]
]

for i in gauss(sistema): print(i)

print(resolver(gauss(sistema)))