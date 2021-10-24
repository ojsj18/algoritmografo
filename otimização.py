# -*- coding: utf-8 -*-
import sys
import numpy as np

# tratamento de entradas
entrada = sys.stdin.read().split()
n, e = int(entrada[0]), int(entrada[1]) #numero de nos e arestas
del(entrada[0],entrada[0])

iniciofimpeso = entrada[0:3]
ini = int(iniciofimpeso[0])
fim = int(iniciofimpeso[1])
peso = int(iniciofimpeso[2])
del(entrada[0:3])

#criando representação do grafo em uma matriz
lista = np.copy(entrada)

#b tem saida um apenas na entrada e na saida, onde a soma das entradas e das saidas tem que ser ==1
bezinho = np.zeros(n,int)
bezinho[0]=1
bezinho[n-1] = 1

azinho = []
cezinho = dict()
nos = dict()

#criando as linhas correspondentes para cada nó


#criando um dicionario com os indices das arestas como keys
for i in range (0,len(lista),3):
    aux = lista[i:i+3]
    x = str(aux[0]+aux[1])
    nos[x]=0
    cezinho[x]=lista[i+2]

#um vetor correspondente para cada possibilidade de aresta
for i in range(0,n):
    azinho.append(nos.copy())

# se estiver saindo do nó == -1 se estiver chegando no nó == 1
for i in range (0,len(lista),3):
    aux=lista[i:i+3]
    j=aux[0]+aux[1]
    for no in range(1,n+1):
        if int(aux[0])==no:
            azinho[no-1][j]= -1
        if int(aux[1])==no:
            azinho[no-1][j]= 1

#transformando o dicionario em um array
nokeys= list()
nokeys2= list()

for i in range(0,len(azinho)):
    nokeys.append(azinho[i].values())


nokeys2.append(cezinho.values())

#as entradas e as saidas são uma soma, arruma com o -1
azinho = np.copy(nokeys)
azinho[0] = -1 * azinho[0]
cezinho = np.copy(nokeys2)

a = azinho
b = bezinho
c = cezinho

print(nos)
print(azinho)
print(bezinho)
print(cezinho)

from scipy.optimize import linprog
res = linprog(c, A_eq=a, b_eq=b, method='simplex')
print(res.fun)