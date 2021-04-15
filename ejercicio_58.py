n = int(input("ingresa la cantidad de numeros :  "))
suma_impares,suma_pares = 0,0
for i  in range(1,n+1):
    if i % 2 == 0:
        print(i,"par")
    if i % 2 != 0 :
        print(i,"impar")