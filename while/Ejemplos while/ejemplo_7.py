# Haz un programa que pida un número "Introduce un número".
# A continuación el programa pedirá tantos números cómo se haya indicado 
# y devovlerá la media de ellos.

numeros_que_necesitamos=int(input("Introduce un número: "))
numeros_que_llevamos=0
suma=0

while numeros_que_llevamos < numeros_que_necesitamos:
    #pedir un numero
    numero_que_recibo=int(input("Introduce un número: "))
    #sumar los numeros
    suma=numero_que_recibo+suma

    numeros_que_llevamos+=1

print(suma/numeros_que_necesitamos)   