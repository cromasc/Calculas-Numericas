def gauss(matriz: list):
    if len(matriz) != len(matriz[1])-1: return None
    else:
        for pivot in range(len(matriz)-1):
            for linha in range(pivot+1,len(matriz)):
                if matriz[pivot][pivot] != 0: 
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
            
def somalinha(linha: list, solucoes: list):
    n = 0

    intervalo = list(range(len(linha)-len(solucoes), len(linha)))
    intervalo.reverse()

    for i in intervalo:
        n += linha[i]*solucoes[i]
    return n

def resolver(matriz: list):
    if matriz[len(matriz)-1][len(matriz)-1] == 0: return "Sistema Impossível"
    elif matriz[len(matriz)-1][0] == matriz[len(matriz)-1][0] == 0:
        n = list(range(len(matriz)))
        n.reverse()

        solucao = [0 for _ in range(len(matriz))]

        for i in n: solucao[i] = round((matriz[i][len(matriz)]-(somalinha(matriz[i][:len(matriz)],solucao)))/matriz[i][i],3)

        return solucao
    else: return None

sistema = [
    [3,1,1],
    [2,4,-1]
]

print(resolver(gauss(sistema)))