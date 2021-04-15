n = int(input("ingresa un numero: "))
for i  in range(1,n):
    if i % 2 == 0:
        i = i - (2*i)
    print(i)