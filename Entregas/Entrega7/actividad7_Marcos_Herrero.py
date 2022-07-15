# Marcos Herrero
# Actividad 7: Problema 8.5

import random
import matplotlib.pyplot as plt

def mcd(a,b):
    if a < 0:
        a = -a
    
    if b < 0:
        b = -b
   
    pot = 1
    while b != 0:
        if a < b :
            a,b = b,a
    
        if a % 2 == 0 and b % 2 == 0:
            pot *= 2
            a//= 2
            b//= 2
        
        elif a % 2 == 0:
            a//=2
    
        elif b % 2 == 0:
            b//=2
    
        else:
            a,b = b, a-b
    
    return a*pot
    
    
def potencia_mod_iter(a,k,N):
    aaux = a%N
    kaux = k
    sol = 1
    
    while kaux > 0:
        if kaux % 2 == 1:
            sol = (sol * aaux)%N
            kaux -= 1
        else:   
            aaux = (aaux*aaux)%N
            kaux//= 2
        
    return sol

'''

Versión recursiva de cálculo del símbolo de Jacobi, en la que me base para hacer la iterativa


    
def jacobi(a,n): # debe ser n positivo e impar
    if n == 1:
        return 1
    
    if a == 0:
        return 0
    
    if a == 1:
        return 1
    
    
    if a == -1:
        if ((n-1)//2) % 2 == 0:
            return 1
        else:
            return -1
    
    if a == 2:
        if ((n*n-1)//8) % 2 == 0:
            return 1
        else:
            return -1
    
    if a < 0 or a >= n:
        return jacobi(a%n, n)
    
    if a % 2 == 0:
        return jacobi(2,n)*jacobi(a//2,n)
    
    if mcd(a,n) != 1:
        return 0
        
    if((a-1)*(n-1))%8 == 0:
        return jacobi(n,a)
    
    return - jacobi(n,a)
    
'''

# Calcula el símbolo de jacobi sin recursión profunda        
def jacobiit(a,n): #debe ser n positivo e impar
    if n == 1:
        return 1
    
    aaux = a % n
    naux = n
    
    if mcd(aaux, naux) != 1:
        return 0
    
    acum = 1
    
    while aaux != 1:
        if aaux % 2 == 0:
            # llamamos j2 a jacobi(2,naux)
            j2 = 1 
            if (naux*naux-1)%16 != 0:
                j2 = -1
            
            while aaux % 2 == 0:
                acum *= j2
                aaux //= 2
        
        elif ((aaux-1)*(naux-1))%8 == 0:
            aaux, naux = naux, aaux
            aaux = aaux % naux
        
        else :
            aaux, naux = naux, aaux
            aaux = aaux % naux
            acum = -acum
    
    return acum
    

def test_de_solovay_strassen(n,k):
    # Se aplican k iteraciones del test de Solovay-Strassen sobre el entero n >= 1
    # Devuelve compuesto si se demuestra que es compuesto y probablemente primo en caso contrario
    if n == 1 or n == 2:
        return "probablemente primo"
    
    if n % 2 == 0: # n es par y distinto de 2 : n no es primo
        return "compuesto"
    
    # n es impar : aplicamos el test de Solovay-Strassen
    
    for i in range(k):
        # Elegimos a aleatoriamente en {1,...,n-1}
        a = random.randint(1,n-1)
        
        #Calculamos el número de jacobi de a y n (será 0 si y solo a y n no son coprimos)
        jac = jacobiit(a,n)
        
        if jac == 0: # a y n no son coprimos
            return "compuesto" 
        
        else:
            potencia = potencia_mod_iter(a,(n-1)//2,n)
            
            if jac == 1 and potencia != 1:
                return "compuesto"
            
            if jac == -1 and potencia != n-1:
                return "compuesto"
    
    return "probablemente primo"

def generar_aleatorio(n): # genera un numero aleatorio de n digitos
    pot = 1
    sol = 0
    for i in range(n):
        sol += pot* random.randint(0,9)
        pot*=10
    
    return sol

def generar_primo(n,k): # busca, generando aleatoriamente, un numero de n digitos que pase k veces el test de Solovay-Strassen
    # generamos un numero aleatorio de n digitos
    p = generar_aleatorio(n)
    
    # numero de intentos hasta encontrar un numero que cumpla lo pedido
    cnt = 1
    
    while test_de_solovay_strassen(p,k) == "compuesto":
        cnt += 1
        p = generar_aleatorio(n)
    
    # al salir del bucle necesariamente el test devuelve probablemente primo
        
    return (p,cnt)

def generar_histograma():
    data = []
    
    for i in range(100):
        _ , cnt = generar_primo(300,20)
        print("Primo {} generado".format(i))
        
        data.append(cnt)
    
    plt.title("Test de Solovay-Strassen")
    plt.xlabel("cnt")
    plt.ylabel("frecuencia")
    plt.hist(data)
    plt.show()
             
print(generar_primo(1000,100))    
#generar_histograma()
