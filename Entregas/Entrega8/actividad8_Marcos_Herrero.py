# Marcos Herrero
# Actividad 8 : problema 10.7

'''
Tarda algo más de lo que permitían tus restricciones de tiempo. Los tres primeros 
test tardan, sumados, menos de un minuto,pero el test4 tarda entre 10 y 20 minutos. 
Creo que aplico correctamente el algoritmo, pero no he conseguido hacer el programa
más rapido.
'''


#Suma los polinomios v y w en Zp[x]
def sumaPol(v,w,p):
    return [(v[i] + w[i]) % p for i in range(len(v))]

#Resta los polinomios v y w en Zp[X]
def restaPol(v,w,p):
    return [(v[i] - w[i]) % p for i in range(len(v))]

#Producto coordenada a coordenada de dos vectores de polinomios
def prodCoordaCoord(u1,u2,k,p):
    return [mult_ss_mod(u1[i],u2[i],k,p) for i in range(len(u1))]

#Coeficientes de la identidad de Bezout de a y b
def bezoutCoefs(a,b):
    if b == 0:
        return 1,0
    
    x,y = bezoutCoefs(b,a%b)
    return y, x-a//b*y

#Inverso de n en Zp
def invZP(n,p):
    x, y = bezoutCoefs(n,p)
    return x

#Multiplicar el polinomio v por el polinomio c*x^i en (Zp[x])/(1+x^l))
def multvxi(v,c,i,p):
    l = len(v)
    sol = [0 for j in range(l)]
    
    for j in range(l):
        if ((j+i)//l)%2 == 0:
            sol[(j+i)%l] = (c*v[j])%p
        
        else:
            sol[(j+i)%l] = (-c*v[j])%p
    
    return sol

#Para cada i, multiplicar el polinomio v[i] por c*x^j donde a[i]=(c,j)
def multvxiCoordaCoord(v,a,p):
    return  [multvxi(v[i],a[i][0],a[i][1],p) for i in range(len(v))]
    

#Devuelve c,z donde a*x^i * b*x^j = c*x^z en (Zp[x])/(1+x^l)
def multxixj(a,i,b,j,l,p):
    if ((i+j)//l)%2 == 0:
        return (a*b)%p , (i+j)%l
    
    else:
        return (-a*b)%p, (i+j)%l

#Devuelve (c,z) si (a*x^i)^j = c*x^z en (Zp[x])/(1+x^l)
# a debe ser 1 o -1, pero j puede ser negativo
def potxij(a,i,j,l):
    if j % 2 == 0:
        if ((i*j)//l)%2 == 0:
            return 1,(i*j)%l
        else:
            return -1,(i*j)%l
    
    else:
        if ((i*j)//l)%2 == 0:
            return a,(i*j)%l
        else:
            return -a,(i*j)%l

#Transformada de Fourier de v donde v esta en ((Z/pZ)[u]/<x^n+1>)[x]
def fft (v,cRaiz,indRaiz,k,p):
    n = len(v) #longitud del polinomio al que le vamos a calcular la transformada
    l = len(v[0]) #longitud de los polinomios coeficientes
    
    if n == 1:
         return v

    v_even = [v[2*i] for i in range(n//2)]
    v_odd = [v[2*i+1] for i in range(n//2)]
    
    cCuadrado, indCuadrado = potxij(cRaiz,indRaiz,2,l)
    a_even = fft(v_even,cCuadrado,indCuadrado,k,p)
    a_odd = fft(v_odd,cCuadrado,indCuadrado,k,p)
    
    a = n*[0]
    
    for i in range(n//2):
        cpoti,indpoti = potxij(cRaiz,indRaiz,i,l)
        
        prod = multvxi(a_odd[i],cpoti,indpoti,p)
        
        a[i] = sumaPol(a_even[i],prod,p)
        a[i+n//2] = restaPol(a_even[i],prod,p)
    
    return a

#Transformada de Fourier inversa de a
def ifft(a,cRaiz,indRaiz,k,p):
    n = len(a)
    l = len(a[0])
    
    cInv, indInv = potxij(cRaiz,indRaiz,-1,l)
    v = fft(a,cInv,indInv,k,p)
    
    invn = invZP(n,p)
    
    for i in range(n):
        for j in range(l):
            v[i][j] = (v[i][j]* invn)%p
    
    return v
        

#Negaconvolucion
#Importante: la raiz siempre tiene unico coeficiente 1 o -1 y todos los demás 0
#En lugar de pasar la raiz, pasamos el coeficiente no nulo y su indice
def negaconv(v,w,k,p,cRaiz,indRaiz):
    n = len(v) # longitud de los vectores v y w (== n2 de antes)
    l = len(v[0]) # longitud de los polinomios coeficientes (== 2*n1 == 2**k)
    
    a = [potxij(cRaiz,indRaiz,i,l) for i in range(n)]
    inva = [potxij(cRaiz,indRaiz,-i,l) for i in range(n)]

    # raiz es una raiz 2n-esima primitiva de la unidad, asi que su cuadrado
    # sera raiz n-esima de la unidad, que es lo que requiere la fft
    # Aplicamos la segunda formula de la negaconvolucion

    fft1 = fft(multvxiCoordaCoord(v,a,p),a[2][0],a[2][1],k,p)
    fft2 = fft(multvxiCoordaCoord(w,a,p),a[2][0],a[2][1],k,p)

    sol = multvxiCoordaCoord(ifft(prodCoordaCoord(fft1,fft2,k,p),a[2][0],a[2][1],k,p),inva,p)

    return sol
    

#[f] y [g] en (Z/pZ)[x]/< x^(2^k) + 1 >
# Calcula el producto de [f] y [g] con Schonhage-Strassen
# Las listas f y g son de longitud exactamente 2^k
def mult_ss_mod(f,g,k,p):
    n = 2 ** k

    if k == 0:
        return [(f[0]*g[0]) % p]
    
    if k == 1:
        return [(f[0]*g[0] - f[1]*g[1]) % p, (f[0]*g[1]+f[1]*g[0]) % p]
    
    
    if k == 2:
        coef0 = (f[0]*g[0]-f[1]*g[3]-f[2]*g[2]-f[3]*g[1])% p
        coef1 = (f[0]*g[1]+f[1]*g[0]-f[2]*g[3]-f[3]*g[2])% p
        coef2 = (f[0]*g[2]+f[1]*g[1]+f[2]*g[0]-f[3]*g[3])% p
        coef3 = (f[0]*g[3]+f[1]*g[2]+f[2]*g[1]+f[3]*g[0])% p
        return [coef0, coef1, coef2, coef3]
    
    
    fnocero = False
    gnocero = False
    for i in range(n):
        if f[i] != 0:
            fnocero = True
        
        if g[i] != 0:
            gnocero = True
    
    if not(fnocero) or not(gnocero):
        return [0 for i in range(n)]
    
        
    if k % 2 == 0:
        k1 = k//2
        k2 = k1
    
    else:
        k1 = (k-1)//2
        k2 = (k+1)//2
    
    n1 = 2**k1
    n2 = 2**k2
    
    ftilde = [[0 for j in range(2*n1)] for i in range(n2)]
    
    for i in range(n2):
        for j in range(n1):
            ftilde[i][j] = f[i*n1+j]
        
    gtilde = [[0 for j in range(2*n1)] for i in range(n2)]
    
    for i in range(n2):
        for j in range(n1):
            gtilde[i][j] = g[i*n1+j]
    
    htilde = negaconv(ftilde,gtilde,k1+1,p,1,(2*n1)//n2)
    
    h = n*[0]
    
    for i in range(n2):
        for j in range(2*n1):
            ind = (i*n1+j)%n
            
            if ((i*n1+j)//n)% 2 == 0:
                h[ind] += htilde[i][j]
            else:
                h[ind] -= htilde[i][j]
                
            h[ind] %= p
    
    return h

#Calcula el producto de f y g en (Z/pZ)[x] utilizando mult_ss_mod
def mult_pol_mod(f,g,p):
    if f == [] or g == []:
        return []
        
    degf = len(f) - 1
    degg = len(g) - 1
    suma = degf + degg
    
    pot = 1
    k = 0
    while pot <= suma:
        pot *= 2
        k += 1
    
    n = 2**k
    
    fext = n*[0]
    for i in range(len(f)):
        fext[i] = f[i]
    
    gext = n*[0]
    for i in range(len(g)):
        gext[i] = g[i]
     
    hext = mult_ss_mod(fext,gext,k,p)
    
    m = len(hext)
    while m > 0 and hext[m-1] == 0:
        m -= 1
    
    h = m*[0]
    
    for i in range(m):
        h[i] = hext[i]
    
    return h
