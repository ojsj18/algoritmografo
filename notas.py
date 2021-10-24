# -*- coding: utf-8 -*-
import sys
import numpy as np

n= 3
azinho = []
for i in range(0,n):
    azinho.append(np.zeros(n,int))


# 2x12 + 6x13 + 3x23
# restrição
# 1x12 + 0x23 + 1x13 = 1 nó 1 [1,0, 1]
# 1x12 - 1x23 + 0x13 = 0  nó 2 [1,-1,0]
# 0x12 + 1x23 + 1x13 = 1  nó 3 [0,1,1]
a = [[1, 0, 1],[ 1, -1,  0],[0, 1, 1]]
b = [1, 0, 1]
#[6, 2, 3]

azinho[0][0]= 1
azinho[0][2]= 1

azinho[1][0]= 1
azinho[1][1]= -1

azinho[2][1]= 1
azinho[2][2]= 1

print(azinho)