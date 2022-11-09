#Programa que pide la edad por teclado, la cual esté comprendida entre 0 y 100, de lo contrario siempre aparecerá el mensaje de 
#"Edad correcta, vuelve a intentarlo" y pedirá de nuevo introducir la edad

edad=int(input("Introduce tu edad: "))

while edad<0 or edad>100:
    print("Edad incorrecta. Vuelve a intentarlo")
    edad=int(input("Introduce tu edad: "))

print("Edad correcta")    
print("Edad del usuario " +str(edad) )