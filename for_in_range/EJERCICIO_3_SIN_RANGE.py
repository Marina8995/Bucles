#Crea un programa que evalúe si una dirección de correo electrónico es válida o no en función de si tiene “@” o “.” 
# Hay que tener en cuenta que la dirección se considera correcta si solo tiene una “@” y si tiene uno o más “.”

correo=input("Introduce un correo correcto: ")
contadorArroba=0
contadorPunto=0

for i in (correo):
    if i=="@":
        contadorArroba=contadorArroba+1
    if i==".":
        contadorPunto=1

if contadorArroba<1 or contadorArroba>1 or contadorPunto==0:
    print("Correo incorrecto")

else:
    print("Correo correcto")          
