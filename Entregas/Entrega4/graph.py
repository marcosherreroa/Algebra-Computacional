
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from mult_strassen import *

M = 100
x = list(range(1,M+1))
y = M*[0]
numEnsayos = 10

# Calculamos los tiempos para el algoritmo de Strassen
for k in range(M):
    A = [[1 for j in range(k+1)] for i in range(k+1)]
    
    start = timer() 
    for z in range(numEnsayos):
        mult_strassen(A,A) 
   
    end = timer()
    y[k] = (end - start)/numEnsayos

plt.plot(x,y)

plt.title("Complejidad de algoritmos de mutiplicación de matrices")
plt.xlabel("Dimensión de la matriz")
plt.ylabel("Tiempo en s")
plt.show()

