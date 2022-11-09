# 2. Haz un programa que pida 5 números y muestre el resultado de sumarlos


num_veces=3
acumulador=0
suma=0

while acumulador<num_veces:
    acumulador+=1
    num=int(input("Introduce un número: "))
    suma=suma+num
print(suma)

#               0   1   2   3
# num           1   2   3   4
# num veces     3   3   3   3
# acumulador    0   1   2   3