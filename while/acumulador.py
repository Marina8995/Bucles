# Programa que pida 4 números y al finalizar muestre la suma

numero1=int(input("Introduce un número: "))
suma=numero1
contador=1 #si ponemos 0 nos pide 5 números en vez de 4

while contador<4:
    numero=int(input("Introduce un número: "))
    suma+=numero # suma=suma+numero
    contador+=1 # contador=contador+1

print(suma)    