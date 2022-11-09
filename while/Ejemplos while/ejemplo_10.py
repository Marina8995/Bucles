# Haz un programa que pida números indefinidamente hasta que se
# introduzcan cinco numeros pares.

#pedir un numero

#mientras los numeros introducidos no sean 5 pares:
    #pedir un numero
 
numeros_pares=0


while numeros_pares<5:
    
    
    numero=int(input("Introduce un numero: "))  
    

    if numero % 2 == 0:         #Para comprobar si un numero es par utilizamos %. Nos devuelve el resto de la division de numero entre 2
        numeros_pares+=1