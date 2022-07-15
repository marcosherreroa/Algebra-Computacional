# Marcos Herrero
# Ejercicio 1.5 : Producto de dígitos de la constante de Champerown
# Versión 1: Versión simple, pero ineficiente. Las concatenaciones son costosas y la cadena ocupa mucha memoria

lim = 1000000 # posición hasta la que hay que generar dígitos
cadena = "" 

for i in range(lim): # guardamos los dígitos de Champerown hasta el dígito 1000000 en una cadena (en la posición 0 estamos guardando un 0)
    cadena += str(i)

# una vez tenemos todos los dígitos, multiplicamos los que nos piden
sol = int(cadena[1])*int(cadena[10])*int(cadena[100])*int(cadena[1000])*int(cadena[10000])* int(cadena[100000])*int(cadena[1000000])

# mostramos la solución
print("La solución es: "+str(sol))


