# Haz un programa que pregunte un número. 
# El usuario introduce ese número y el programa pide tantos números como el usuario haya indicado y los suma


num=(int(input("Introduce un numero: ")))
num_veces=num
contador=0
suma=0

while contador<num_veces:
    
    contador+=1
    num1=(int(input("Introduce un numero: ")))
    num=num1
    suma=suma+num1

print(suma)    