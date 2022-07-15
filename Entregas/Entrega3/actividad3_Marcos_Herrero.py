# Marcos Herrero
# Entrega 3: Problema 3.4

""" Versión recursiva: es útil para entender la idea, pero
    solo funciona con números muy pequeños
    
def es_posible_ganar_con_n_piedras(n):
    if n == 1: # solo puedes quitar una piedra, y con ello pierdes
        return False
    
    if not es_posible_ganar_con_n_piedras(n-1): # quitas 1 piedra y el otro no tiene estategia ganadora
        return True
    
    if n > 2 and not es_posible_ganar_con_n_piedras(n-2): # quitas 2 piedras y el otro no tiene estrategia ganadora
        return True
    
    if n > 6 and not es_posible_ganar_con_n_piedras(n-6): # quitas 6 piedras y el otro no tiene estrategia ganadora
        return True
    
    else :
        return False
"""

""" Versión con memoization: sería lo bastante eficiente para permitirnos calcular el valor buscado
    si no fuera porque excede el límite de la recursión, que solo nos permite llegar hasta cerca de 1000.
    Necesitamos una versión iterativa
    
def es_posible_ganar_con_n_piedras_aux(n, posible): 
    #posible es una lista con los valores ya calculados.
    # 1 significa True y 0 False. Está inicializada a -1
    # De esta manera, sabemos qué partes de la lista están sin rellenar
    
    if n == 1:
        return 0
    
    if posible[n-1] == -1:
        posible[n-1] = es_posible_ganar_con_n_piedras_aux(n-1,posible)
    if posible[n-1] == 0:
        return 1
    
    if n > 2:
        if posible[n-2] == -1:
            posible[n-2] = es_posible_ganar_con_n_piedras_aux(n-1,posible)
        if posible[n-2] == 0:
            return 1
    
    if n > 6:
        if posible[n-6] == -1:
            posible[n-6] = es_posible_ganar_con_n_piedras_aux(n-1,posible)
        if posible[n-6] == 0:
            return 1
     
    return 0 
    
def es_posible_ganar_con_n_piedras(n):
    posible = (n+1)* [-1]
    return es_posible_ganar_con_n_piedras_aux(n,posible)== 1 """
    
"""Versión con tabulation ( versión iterativa de la anterior). Esta es la buena"""

def es_posible_ganar_con_n_piedras(n):
    posible = (n+1)*[False]
    
    # Resolvemos el problema para todo m entre 1 y n. Vamos de menor a mayor, ya que
    # cada instancia solo requiere soluciones de problemas con número menor de piedras
    ## El caso base posible[1] ya está a False
    for i in range(2,n+1):
        if not posible[i-1]:  # quitas 1 piedra y el otro no tiene estategia ganadora
            posible[i] = True
            
        elif i > 2 and not posible[i-2]: # quitas 2 piedras y el otro no tiene estrategia ganadora
            posible[i] = True
            
        elif i > 6 and not posible[i-6]: # quitas 6 piedras y el otro no tiene estrategia ganadora
            posible[i] = True
      
    return posible[n]

print(es_posible_ganar_con_n_piedras(10**6))
