# Haz un programa que pida 10 numeros y sume por un lado los
# pares y por otro los impares y muestre ambas sumas.

# mientras el numero de numeros pedidos sean menor que 10:
    #pedir un numero

    #si el numero es par:
        #sumar pares

    #si no:
        #sumar impares
        
#print suma pares
#print suma impares

numero_de_veces=0
suma_pares=0
suma_impares=0

while numero_de_veces<10:   
    numero_de_veces+=1     
    numeros_pedidos=int(input("Introduce un número: "))  

    if numeros_pedidos % 2 == 0:
        suma_pares=suma_pares+numeros_pedidos

    else:
        suma_impares=suma_impares+numeros_pedidos 

print(suma_pares)
print(suma_impares)        