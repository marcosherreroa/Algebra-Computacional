# Entrega 4: Ejercicio 4.4 ( multiplicación de matrices por método de Strassen)

# Función que comprueba que la matriz A es nxm
def comprobarMatriz(A,n,m):

    if len(A) != n:
        return False
    
    for fila in A:
        if len(fila) != m:
            return False
    
    return True

#Función que suma dos matrices
def suma(A,B):
    n = len(A)
    m = len(A[0])
    
    if not comprobarMatriz(A,n,m) or not comprobarMatriz(B,n,m):
        print("Las matrices a sumar deben ser de la misma dimensión")
        return None
    
    S = [[ A[i][j]+B[i][j] for j in range(m)] for i in range(n)]
    return S

#Función que resta dos matrices
def resta(A,B):
    n = len(A)
    m = len(A[0])
    
    if not comprobarMatriz(A,n,m) or not comprobarMatriz(B,n,m):
        print("Las matrices a sumar deben ser de la misma dimensión")
        return None
    
    S = [[ A[i][j]-B[i][j] for j in range(m)] for i in range(n)]
    return S
    

def mult_strassen(A,B):
    n = len(A)
    
    # Comprobamos que A y B son matrices cuadradas de la misma dimensión
    if not comprobarMatriz(A,n,n) or not comprobarMatriz(B,n,n):
        print ("Las matrices a multiplicar deben ser cuadradas y de la misma dimension")
        return None
    
    
    C = [[0 for j in range(n)] for i in range(n)]
    
    
    if n <= 32:
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    C[i][j] += A[i][k]*B[k][j]
    
        return C          
    
    Aaux = [ fila[:] for fila in A]
    Baux = [fila[:] for fila in B]
    impar = False
    
    if n % 2 == 1:
        impar = True
        n+= 1
        
        for fila in Aaux:
            fila.append(0.0)
        Aaux.append(n*[0])
        
        for fila in Baux:
            fila.append(0.0)
        Baux.append(n*[0])
    
    m = n//2
    
    A11 = [[Aaux[i][j] for j in range (m)] for i in range(m)]
    A12 = [[Aaux[i][j] for j in range (m,n)] for i in range(m)]
    A21 = [[Aaux[i][j] for j in range (m)] for i in range(m,n)]
    A22 = [[Aaux[i][j] for j in range (m,n)] for i in range(m,n)]
    
    B11 = [[Baux[i][j] for j in range (m)] for i in range(m)]
    B12 = [[Baux[i][j] for j in range (m,n)] for i in range(m)]
    B21 = [[Baux[i][j] for j in range (m)] for i in range(m,n)]
    B22 = [[Baux[i][j] for j in range (m,n)] for i in range(m,n)]
    
   
    M1 = mult_strassen(suma(A11,A22), suma(B11,B22))
    M2 = mult_strassen(suma(A21,A22),B11)
    M3 = mult_strassen(A11,resta(B12,B22))
    M4 = mult_strassen(A22,resta(B21,B11))
    M5 = mult_strassen(suma(A11,A12),B22)
    M6 = mult_strassen(resta(A21,A11),suma(B11,B12))
    M7 = mult_strassen(resta(A12,A22),suma(B21,B22))
    
    C11 = suma(resta(suma(M1,M4),M5),M7)
    C12 = suma(M3,M5)
    C21 = suma(M2,M4)
    C22 = suma(suma(resta(M1,M2),M3),M6)
    
    if impar:
        n -= 1
        
  
    
    for i in range(m):
        for j in range(m):
            C[i][j] = C11[i][j]

    for i in range(m):
        for j in range(m, n):
            C[i][j] = C12[i][j-m]
    
    for i in range(m,n):
        for j in range(m):
            C[i][j] = C21[i-m][j]
    
    for i in range(m,n):
        for j in range(m,n):
            C[i][j] = C22[i-m][j-m]
    
    return C
