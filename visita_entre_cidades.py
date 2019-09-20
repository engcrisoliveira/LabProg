#Implementar o Algoritmo de Dijkstra a partir de uma matriz de adjacência

#Receber os dados de entrada 
N, A, B = map(lambda i: int(i), input().split())

A-=1
B-=1

#Criar uma matriz de adjacências com as distâncias
G = [[0 for i in range(N)] for j in range(N)]
for i in range(N-1):
        P, Q, D = map(lambda i: int(i), input().split())
        P-=1
        Q-=1
        G[P][Q]=D
        G[Q][P]=D
        
#Atribuir um valor da distância a todos os vértices no gráfico de entrada 
DIC = {0:0} #{vértice, distância}
DIC = {str(i):float("inf") for i in range(N)} #Iniciar todos os valores de distância como infinito 
DIC[str(A)]=0 #Atribuir 0 ao valor da distância do vértice de origem, para que seja o primeiro

#Lista com os valores da distância e vértices 
L= [(0,A)]

#Função para calcular a distância entre os vértices (cidades)
def Distancia():
    while L!=[]:
        Custo,Va=L.pop(0) #Retirar os vértices já visitados
                          #Custo é a distância entre as cidades
                          #Va é o vértice atual
        for i in range(N):
            if G[Va][i]: #Quando os vértices são vizinhos:
                if DIC[str(i)]>G[Va][i]+Custo: #Comparar os valores da distância do dicionário e do calculado
                    DIC[str(i)]=G[Va][i]+Custo #Substituir os valores da distância do dicionário pelo calculado
                    L.append((DIC[str(i)],i)) #Adicionar o novo valor da distância e o vértice na Lista
 
Distancia()

#Imprimindo o resultado da distância entre as duas cidades
print(DIC[str(B)])
