#Crea un programa que pida números infinitamente. Los números introducidos deben ser cada vez mayores 
# El programa finalizará cuando se introduce un número menor que el anterior.

numero1=int(input("Introduce un número: "))
numero2=int(input("Introduce un número mayor que " +str(numero1)+ " : "))


while numero2>numero1:
    numero1=numero2
    print("El número introducido es " +str(numero2))
    numero2=int(input("Introduce un número mayor que " +str(numero2)+ " : "))

print("El número " +str(numero2) + " es menor que " +str(numero1))
    




  