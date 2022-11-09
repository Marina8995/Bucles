#Crea un programa que pida números positivos indefinidamente. El programa termina cuando se introduce un número negativo. 
# Finalmente el programa muestras la suma de todos los números introducidos

numero=int(input("Introduce un número positivo: "))
suma=0

while numero>0:
    suma=suma+numero
    print("El número introducido es: " +str(numero))
    numero=int(input("Introduce un número positivo: "))

print("El número introducido es un número negativo")  


print("La suma de los números es: " +str(suma))  