#3. Haz un programa que pida números y los sume hasta que se introduzca uno negativo.

num=int(input("Introduce un numero: "))

suma=0

while num>0:
    suma=num+suma
    
    num=int(input("Introduce un numero: "))

print(suma)    

#          0    1   2   3
# num      5    1   2  -1  
# suma     0    5   6   8   
