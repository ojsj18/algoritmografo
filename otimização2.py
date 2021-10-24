# -*- coding: utf-8 -*-
import sys
import numpy as np

entrada = sys.stdin.read().split()
n, l = int(entrada[0]), int(entrada[1])
del(entrada[0],entrada[0])
iniciofimpeso = entrada[0:3]
ini = int(iniciofimpeso[0])
fim = int(iniciofimpeso[1])
peso = int(iniciofimpeso[2])
del(entrada[0:3])

lista = np.zeros((l,n))
lista = np.copy(entrada)
cezinho =[lista[i] for i in range(2, len(lista), 3)]
bezinho = np.zeros(n,int)
azinho = []
no = 1
#    12 13 23
c = [0,-1,-1]
a = [[1,0,0],[0,1,0],[0,0,1],[1,0,-1]]
b = [2, 6, 3,0]
[4,4,6,1,4,4,3,1,3,9]
from scipy.optimize import linprog
res = linprog(c, A_ub=a[0:3],A_eq=a[3:4], b_ub=b[0:3],b_eq=b[3:4], method='simplex')
print(res)