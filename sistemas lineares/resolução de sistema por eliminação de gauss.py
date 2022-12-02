def gauss(matriz: list):
    if len(matriz) != len(matriz[1])-1: return None
    else:
        for pivot in range(len(matriz)-1):
            for linha in range(pivot+1,len(matriz)):
                if matriz[pivot][pivot] != 0: m = matriz[linha][pivot]/matriz[pivot][pivot]
                else: pass

                for coluna in range(len(matriz[linha])):
                    matriz[linha][coluna] = matriz[linha][coluna] - m*matriz[pivot][coluna]

        for i in matriz: print(i)
        return matriz


def somalinha(linha: list, solucoes:list):
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

        for i in n: solucao[i] = (matriz[i][len(matriz)]-(somalinha(matriz[i][:len(matriz)],solucao)))/matriz[i][i]

        return solucao
    else: return None

sistema = [
    [1,2,3,10],
    [4,5,6,10],
    [7,8,9,10]
]

print(resolver(gauss(sistema)))