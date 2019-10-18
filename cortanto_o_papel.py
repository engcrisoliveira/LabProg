
#Calcular o número máximo de pedaços possível, com um único corte horizontal

#Entrada de dados
alturas = []                                       #Criar uma lista de tuplas (com as alturas dos retângulos e suas respectivas posições)
N = int(input('Inserir o número de retângulos: ')) #Receber o número de retângulos
h = [int(i) for i in input().split()]              #Receber as alturas
for i in range(len(h)): 
    alturas.append((h[i],i+1))                     #Adicionar as tuplas, a partir das alturas e suas posições
alturas.sort()                                     #Ordenar a lista de tuplas, pelas alturas, começando pela menor altura


#Criar um marcador para identificar os retângulos já verificados com 0
mark = [1 for i in range(N+2)] #1 representa os ainda não visitados
mark[0] = 0                    #Marcar com 0 a primeira posição para representar a borda inicial
mark[N+1] = 0                  #Marcar com 0 a última posição para representar a borda final

#Contar a quantidade de pedaços
#A partir da ideia da diferença entre alturas dos retângulos
pieces_max = 2      #Quantidade máxima de pedaços(resultado global)
pieces_cur = 2      #Quantidade máxima de pedaços(índice corrente)
                    #Quantidade máxima de pedaços é a partir de 2 
for i in alturas:
     h, index = i                                   #Para acessar os índices h (altura)e index (posição) das tuplas
     pieces_max = max(pieces_max, pieces_cur)       #Quantidade de cortes é o maior valor entre o valor acumulado e o valor corrente
     mark[index] = 0                                #Marcar o retângulo a ser verificado
     if mark[index-1]==1 and mark[index+1]==1:      #Quando o retângulo verificado for menor que o anterior e o posterior
        pieces_cur+=1                               #Soma um pedaço
     if mark[index-1]==0 and mark[index+1]==0:      #Quando o retângulo verificado for maior que o anterior e o posterior
        pieces_cur-=1                               #Subtrair um pedaço

#Imprimir a quantidade máxima de pedaços
print(pieces_max)
