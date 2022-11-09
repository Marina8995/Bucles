#3. Haz un programa que pida números y los sume hasta que se introduzca uno negativo.

#Ejemplo con break

suma=0

while True:
    num=int(input("Introduce un numero: "))
    if num < 0:
        break
    suma=num+suma
    

print(suma)    

