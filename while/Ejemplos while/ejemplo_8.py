# Haz un programa que pida números 10 números y solo sume los positivos.

#mientras se introduzcan menos de 10 numeros:
    #pedir un numero
    #si es positivo
        #sumarlo

numeros_introducidos=0
suma=0        

while numeros_introducidos<10:
    
    num=int(input("Introduzca un numero: ")) 
    numeros_introducidos+=1     
    if num>0:
        suma=suma+num
        
print(suma)        

        #           0   1   2
        #   ni      0   0   0  
        #suma       0   2   2
        #num        x   2   -1