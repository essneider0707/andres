suma_impares,suma_pares = 0,0
cont1,cont2 = 0,0
while True:
    n = int(input("ingresa la cantidad de numeros :  "))
    if n == 0:
        break
    if n % 2 == 0:
        suma_pares = suma_pares + n
        cont1 = cont1  + 1
        promedio = suma_pares / cont1
    elif n % 2 != 0 :
        suma_impares = suma_impares + n
        cont2 = cont2 + 1
        promedio2 = suma_impares / cont2
print(f"el promedio de los numero pares es {promedio}\nel promedio de los numeros impares es {promedio2}")