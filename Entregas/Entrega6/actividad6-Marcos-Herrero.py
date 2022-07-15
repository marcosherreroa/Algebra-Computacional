# Marcos Herrero
# Actividad 6: Problema 7.10

import random

def primo(N):
    if N < 2:
       return False
   
    i = 2
    while i*i <= N:
       if N % i == 0:
           return False
       
       i += 1
    
    return True
 
def mcd(a,b):
   
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


def potencia_mod(a,k,N):
    if k == 0:
        return 1
    
    if k % 2 == 0:
        r = potencia_mod(a,k//2,N)
        return (r*r)% N
    
    return (a * potencia_mod(a,k-1,N))%N
   
''' 
Versión iterativa de potencia_mod_iter. Para la forma 2

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
    
def logsup(base,arg):
    sol = 1
    pot = base
    
    while pot < arg:
        sol += 1
        pot *= base
    
    return sol
    

#Datos
N = 1542201487980564464479858919567403438179217763219681634914787749213
B = 100


#Calculamos beta y nos guardamos las bases y exponentes de las potencias de primos que lo forman 
beta = 1
bases = []
exponentes = []
for p in range(B+1):
    if primo(p):
        expo = logsup(p,N)
        
        bases.append(p)
        exponentes.append(expo)
        
        beta *= p**expo

y = N

# Repetir hasta encontrar un factor y de N no trivial
while y == N:

    #Tomamos a al azar (uniformemente) entre 1 y N-1
    a = random.randint(1,N-1)

    x = mcd(a,N)

    if x != 1:
        y = x

    else:
        
        # Forma 1:
        # z = pow(a,beta,N)
        
        # Forma 2:
        # z = potencia_mod_it(a,beta,N)
        
        #Forma 3: usando los primos guardados
        z = a
        
        for p in bases:
            for i in exponentes:
                z = potencia_mod(z,p,N)
        
        y = mcd(z-1,N)

print('Factorización encontrada:')
print(str(N)+' = '+str(y)+' * '+str(N//y))
