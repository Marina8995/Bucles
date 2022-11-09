# Haz un programa que pregunte al usuario un número y muestre por pantalla "Hola mundo" ese número de veces.

num=int(input("Introduce un número: "))
numero_veces=num
acumulador=0

while acumulador < numero_veces:
    acumulador=acumulador+1
    
    print ("Hola mundo")

#               0   1   2   3
# num           3   3   3   3
# num veces     3   3   3   3
# acumulador    0   1   2   3