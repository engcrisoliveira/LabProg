#Calcular a menor diferença possível no número de cidades entre os dois impérios resultantes

#Receber a entrada de dados (número de cidades no império)
[N] = [int(c) for c in input().split()]

#Criar uma matriz de adjacências com as distâncias entre as cidades A e B
Distances = [[] for i in range(N+1)] 
for i in range(1,N):
    [A,B] = [int(c) for c in input().split()]
    Distances[A].append(B)
    Distances[B].append(A)

#Função para calcular a distância entre as cidades
def DFS(i,X):
    global result
    weight = 1                
    for j in Distances[i]:
        if (j!=X):
            weight+=DFS(j,i)
    difference = abs(N-(2*weight))
    if (difference<result): 
        result = difference 
    return weight

result=N
DFS(1,-1)

#Imprimir a menor diferença possível
print(result)
