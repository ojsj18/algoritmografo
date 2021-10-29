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

azinho = []
cezinho = dict()
nos = dict()

#criando um dicionario com os indices das arestas como keys
for i in range (0,len(lista),3):
    aux = lista[i:i+3]
    x = str(aux[0]+aux[1])
    nos[x]=0
    cezinho[x]=lista[i+2]
    x = str(aux[1]+aux[0])
    nos[x]=0
    cezinho[x]=lista[i+2]

#um vetor correspondente para cada possibilidade de aresta
for i in range(0,n):
    azinho.append(nos.copy())

# se estiver saindo do nó == -1 se estiver chegando no nó == 1
for i in range (0,len(lista),3):
    aux=lista[i:i+3]
    j=aux[0]+aux[1]
    k=aux[1]+aux[0]
    for no in range(1,n+1):
        if int(aux[0])==no:
            azinho[no-1][j]= "+1" # os if definem a orientação do grafo baseado do ponto de saida e entrada
            azinho[no-1][k]= -1
        if int(aux[1])==no:
            azinho[no-1][j]= -1
            azinho[no-1][k]= "+1"

#transformando o dicionario em um array
nokeys= list()
nokeys2= list()

for i in range(0,len(azinho)):
    nokeys.append(azinho[i].values())

nokeys2.append(cezinho.values())

#as entradas e as saidas são uma soma, arruma com o -1
azinho = np.copy(nokeys)
cezinho = np.copy(nokeys2[0])
#restrições
a = azinho
#respostas das equações das restrições
b = bezinho
#função objetivo
c = cezinho

indices = nos.keys()
linha = str()
objetiva = "min:("
for j in range(0,e*2):
    objetiva = objetiva+"+"+cezinho[j]+"x"+indices[j]+" "
objetiva = objetiva+")"
print(objetiva)
for j in range(0,n):
    for i in range(0,e*2):
        if int(azinho[j][i]) != 0:
            linha = linha+str(azinho[j][i])+"x"+indices[i]+" "
    linha= linha+"= "+str(bezinho[j])+";"+"\n"
print(linha)