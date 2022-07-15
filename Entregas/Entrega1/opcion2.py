# Marcos Herrero
# Ejercicio 1.5 : Producto de dígitos de la constante de Champerown
# Versión 2 : Versión algo más complicada y más eficiente. Se generan y recorren los números sin necesidad de alamacenarlos

target = 1 # índice del digito buscado
sol = 1 # dígito 1
actual = 1 # número por el que vamos
cont = 1 # número de dígitos que hemos pasado 
sigDec = 10 # siguiente decena
numDigitsAct = 1 # número de digitos del número por el que vamos


for i in range(1,7):
    target *= 10 # indice del dígito buscado en esta iteracion
    
    while cont < target: # recorremos números hasta que nos pasemos de la posición buscada
        actual += 1
        
        if actual == sigDec:
            numDigitsAct += 1
            sigDec *= 10
        
        cont += numDigitsAct

    extraDig = cont - target # tenemos que compensar cuánto nos hemos pasado de la posición target
    copiaAct = actual
    
    while extraDig > 0:
        copiaAct //= 10
        extraDig -= 1
    
    sol *= copiaAct % 10 #copiaAct % 10 es el dígito en la posición target

print("La solución es: "+str(sol))
