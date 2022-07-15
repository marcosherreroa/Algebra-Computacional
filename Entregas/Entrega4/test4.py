# Test4

from mult_strassen import *
import random

def prodUsual (A,B):
    n = len(A)
    C = [[0 for j in range(n)] for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] = C[i][j] + A[i][k]*B[k][j]
    
    return C
    
    
ncasos = 50
n = 200
A = [[0 for j in range(n)] for i in range(n)]
B = [[0 for j in range(n)] for i in range(n)]

for i in range(ncasos):
    
    print("Caso {}".format(i))

    for i in range(n):
        for j in range(n):
            A[i][j] = random.randint(1,100)
            B[i][j] = random.randint(1,100)
            
    C1 = prodUsual(A,B)
    C2 = mult_strassen(A,B)
    
    for i in range(n):
        for j in range(n):
            if C1[i][j] != C2[i][j]:
                print("Mal. i:{}, j:{}".format(i,j))
