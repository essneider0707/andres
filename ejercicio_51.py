n = int(input("ingresa la cantidad de numeros :  "))
suma_impares,suma_pares = 0,0
cont1,cont2 = 0,0
for i  in range(1,n+1):
    if i % 2 == 0:
        suma_pares = suma_pares + i
        cont1 = cont1  + 1
        promedio = suma_pares / cont1
    elif i % 2 != 0 :
        suma_impares = suma_impares + i
        cont2 = cont2 + 1
        promedio2 = suma_impares / cont2
print(f"el promedio de los numero pares es {promedio}\nel promedio de los numeros impares es {promedio2}")