#En este caso, continue está ignorando la h
for letra in "Python":
    if letra=="h":
        continue

    print("Viendo la letra: " + letra)



#Ejemplo para contar nº de caracteres 

nombre="Mi nombre es Marina"
print(len(nombre))
#####################################################

#Ejemplo para contar nº de caracteres sin contar lo espacios

nombre="Mi nombre es Marina"
contador=0


for i in nombre:
    if i==" ":
        continue
    contador+=1

print(contador)