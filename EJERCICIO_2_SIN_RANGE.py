#Crea un programa que pida por teclado introducir una contraseña. La contraseña no podrá tener menos de 8 caracteres ni espacios en blanco. 
#Si la contraseña es correcta, el programa imprime “Contraseña OK”. En caso contrario imprime “Contraseña errónea”

contrasena=(input("Introduce una contraseña correcta: "))

contador=0

for letra in contrasena:
    if letra == " ":
        contador += 1  

if len (contrasena)<8 or contador>0:
    print("Contraseña errónea")
else:
    print("Contraseña correcta")         

    
       