# -*- coding: utf-8 -*-
import sys
import numpy as np

# tratamento de entradas
entrada = sys.stdin.read().split()
n, e = int(entrada[0]), int(entrada[1]) #numero de nos e arestas
del(entrada[0],entrada[0])

if int(entrada[0])<int(entrada[1]):
    ini = int(entrada[0])
    fim = int(entrada[1])
else:
    ini = int(entrada[1])
    fim = int(entrada[0])

peso = int(entrada[2])
del(entrada[0:3])

#criando representação do grafo em uma matriz
lista = np.copy(entrada)

#b tem saida um apenas na entrada e na saida, onde a soma das entradas e das saidas tem que ser ==1
bezinho = np.zeros(n,int)
bezinho[ini-1]= -1*peso
bezinho[fim-1]= peso

azinho = np.zeros((n,e),int)
cezinho = dict()  
# se estiver saindo do nó == -1 se estiver chegando no nó == 1
for i in range (0,len(lista),3):
    aux=lista[i:i+3]
    j=int(aux[0])
    k=int(aux[1])
    x = str(aux[0]+aux[1])
    z = str(aux[1]+aux[0])
    for no in range(1,n+1):
        if int(aux[0])==no:
            azinho[no-1][k-1]= 1 # os if definem a orientação do grafo baseado do ponto de saida e entrada
        if int(aux[1])==no:
            azinho[k-1][j-1]= 1
    cezinho[x]=aux[2]
    cezinho[z]=aux[2]

#restrições
a = azinho
#respostas das equações das restrições
b = bezinho
#função objetivo
c = cezinho
linha = str()
objetiva = "min:"
lista = cezinho.values()
lista2 = cezinho.keys()

for i in range(0,e*2):
    objetiva = objetiva+str(lista[i])+"x"+str(lista2[i])+" "
objetiva = objetiva+";"
print(objetiva)

for i in range(0,n):
    for j in range(0,e):
        if int(azinho[i][j]) != 0:
            linha = linha+" x"+str(i+1)+str(j+1)+" "
            linha = linha+"- x"+str(j+1)+str(i+1)+" "
    linha= linha+"= "+str(bezinho[i])+";"+"\n"
print(linha)