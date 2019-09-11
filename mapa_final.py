vertices = int(input("Digite aqui o número de vértices: "))
matriz = [[0 for i in range(vertices)] for j in range(vertices)]

for i in range(vertices):
    matriz[i] = [int(n) for n in input().split(' ')]

# Converter matriz em dicionário
dicionario = {}
for i,j in enumerate(matriz): # nesse caso o i são as listas internas e o j é o índice dos elementos
    res = []
    for r in range(len(j)):
        if j[r] != 0:
            res.append(r)
        dicionario[i] = res
print(dicionario)

# Algoritmo de Welsh and Powell
def cores(dicio):
    global colors
    colors = {}
    vizinhos = sorted(list(dicio.keys()), key=lambda x: len(dicio[x]), reverse=True) #colocar os vizinhos em ordem decrescente
    for i in vizinhos:
        coresdisponiveis = [True] * len(vizinhos) #Isso retorna a quantidade de cores máximas que podemos usar a partir do tamanho da nossa lista de vizinhos
        for j in dicio[i]:
            if j in colors:
                cor = colors[j]
                coresdisponiveis[cor] = False
        for cor, disponivel in enumerate(coresdisponiveis):
            if disponivel:
                colors[i] = cor
    return colors
print(cores(dicionario))

# Lista com a quantidade de cores usadas
quantidadecores = []
for i in colors.values():
    quantidadecores.append(i)
print(len(set(quantidadecores)))
