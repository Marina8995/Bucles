#Cálculo de raíz cuadrada de un número positivo. Máximo número de intentos 3

import math

print("Programa de cálculo raíz cuadrada de un número positivo")
numero=int(input("Introduce un número positivo: "))

intentos=0

while numero<0:
    print("No se puede calcular la raíz cuadrada de un número negativo")
    if intentos==2:
        print("Número máximo de intentos alcanzado. El programa ha finalizado")
        break;

    numero=int(input("Introduce un número positivo: "))
    if numero<0:
        intentos=intentos+1

if intentos<2:        
    solucion=math.sqrt(numero)
    print("La raíz cuadrada del número " +str(numero) + " es " +str(solucion) )   