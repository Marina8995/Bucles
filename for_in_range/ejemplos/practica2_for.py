#El end indica como queremos que termine la impresión.
#En este caso estamos indicando que no haga salto de línea y que lo escriba todo junto

for i in ["Marina", "Iglesia", 3]:
    print("Hola", end="")

    
#Aquí indicamos que deje un espacio

for i in ["Marina", "Iglesia", 3]:
    
    print("Hello", end=" ")

#Si escribimos un texto se imprimirá la palabra Hi tantas veces como caracteres haya    

for i in "iglesiaperezmarina@gmail.com":
    print("Hi", end=" ")   


#Para comprobar si un email esta escrito correctamente:

email=False
for i in "iglesiaperezmarina@gmail.com":
    if(i=="@"):
        email=True

if email==True:
    print("Email es correcto")
else:
    print("Email es incorrecto")    

#Se puede simplificar omitiendo ==True en la condicional if   

email=False
for i in "iglesiaperezmarina@gmail.com":
    if(i=="@"):
        email=True

if email:
    print("Email es correcto")
else:
    print("Email es incorrecto")    

#Ejemplo 1. Comprobar que mi dirección emial es correcta

email=False
miEmail=input("Introduce tu correo: ")

for i in "iglesiaperezmarina@gmail.com":
    if(i=="@"):
        email=True

if email:
    print("Email es correcto")
else:
    print("Email es incorrecto")      

#Ejemplo 2. Comprobar dirección de email es correcta si tiene @ y .   

contador=0
miEmail=input("Introduce tu correo: ")

for i in "iglesiaperezmarina@gmail.com":
    if(i=="@" or i=="."):
        contador=contador+1

if contador==2:
    print("Email es correcto")
else:
    print("Email es incorrecto")   