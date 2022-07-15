#Marcos Herrero
# Ejercicio 2.4: Bolas en cajas

def resolver(numCajas):
    confInicial = numCajas * [1]  # la guardamos aparte para comparar
    
    #inicio
    conf = numCajas * [1] 
    #turno 1
    conf[0]= 0
    conf[1%numCajas] += 1
    ind = 1 % numCajas #índice del que toca sacar en el sigueinte turno
    
    turno = 1
    while conf != confInicial : # si no se ha obtenido la configuración inicial, simulamos otro turno
        turno += 1 # turno que se inicia
        
        bolas = conf[ind] #sacamos las bolas
        conf[ind] = 0
        
        for i in range(bolas): # distribuimos las bolas
            ind = (ind + 1) % numCajas
            conf[ind] += 1        
            #el valor de ind al salir del bucle ya es el requerido para el sigueinte turno
    
    return turno
    
print("La solución es "+str(resolver(100)))
