# Marcos Herrero
# Actividad 5: Problema 6.6

''' Un número N >= 2 es de Carmichael si y solo es compuesto y para todo a en Z : 
      (C) mcd(a,N) = 1 =>  a^(N-1) es congruente con 1 mod N
   
   Veamos que, para ver si un número N >= 2 compuesto es de Carmichael, basta comprobar la condición (C)
   para todo a en {0,1,...,N-1}. Es claro que si N es de Carmichael, entonces se verifica la condición (C) para tod a en Z y,
   en particular, para todo a en {0,1,...,n-1}
   
   Sea N >= 2 un número compuesto, y supongamos que se cumple la condición (C) para todo a en {0,1,...,n-1}. Veamos que N es de Carmichael
   
   Dado a en Z coprimo con N, por el teorema de la división euclídea, existe un b en {0,1,...,N-1} y k en Z tales que
   a = kN + b  (es decir, a es congruente con b mod n). Si existiera un número primo p que dividiera a b y a N, necesariamente
   dividiría a a = kN + b, en contradicción con que a y N sean coprimos. Por tanto, b y N han de ser coprimos. Dado que b está en {0,1,...N-1}
   y es coprimo con N, aplicando la hipótesis tenemos que b^(N-1) es congruente con 1 mod N. Pero, como a es congruente con b mod N, necesariamente 
   a^(N-1) es congruente con b^(N-1) mod N y, por tanto, congruente con 1 mod N.
   Como a es arbitrario, esto prueba que N es de Carmichael
   
   Por consiguiente, para comprobar si un número N >=2 es de Carmichael es necesario y suficiente ver que no es primo y que para todo a en {0,1,...,N-1}
   se verifica la condición (C) 
'''
   
   
   
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
    if a < b :
        return mcd (b,a)
    
    if b == 0:
        return a
    
    if a % 2 == 0 and b % 2 == 0:
        return 2*mcd(a//2,b//2)
    
    if a % 2 == 0:
        return mcd(a//2,b)
    
    if b % 2 == 0:
        return mcd(a,b//2)
    
    return mcd(b, a-b)
   
def potencia_mod(a,k,N):
    if k == 0:
        return 1
    
    if k % 2 == 0:
        r = potencia_mod(a,k//2,N)
        return (r*r)% N
    
    return (a * potencia_mod(a,k-1,N))%N
   
def carmichael(N):
   if N < 2:
       return False
   
   if primo(N):
       return False
    
   for a in range(1,N):
       if mcd(a,N) == 1 and potencia_mod(a,N-1,N) != 1:
           return False
   
   return True
       
    
cont = 0
i = 2

while cont < 10:
    if carmichael(i):
        print(i)
        cont += 1
    
    i +=1
