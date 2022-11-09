# Haz un programa que pregunte al usuario "¿Cuanto quieres ahorrar?". 
# Después preguntará al usuario "Introduzca una cantidad: ", hasta que 
# la suma de las cantidades superen a la cantidad inicial.

#preguntar cuanto quiere ahorrar

#mientras la suma de las cantidades sea menor que la cantidad inicial:
    #se pide una cantidad
    #suma

#muestra suma total

cuanto_quiere_ahorrar=int(input("Cuanto quieres ahorrar?: "))   
suma=0

while suma<cuanto_quiere_ahorrar:
    cantidad=int(input("Introduzca una cantidad: ")) 
    suma=suma+cantidad

print(suma)    