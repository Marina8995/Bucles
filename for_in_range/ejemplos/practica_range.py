
email=False
miEmail=(input("Escribe tu email: "))

for i in range(len(miEmail)):
    if miEmail [i]=="@":
        email=True

if email:
    print("email correcto") 

else:
    print("email incorrecto")       

