n = int(input("ingresa un numero(no mayor a 100000: "))
cont = 0
while n > 0:
    if n < 100000:
        n //= 10
        cont = cont + 1
    else:
        print("por favor ingrese un numero menor a 100000")
print(f"tiene {cont} digitos5")