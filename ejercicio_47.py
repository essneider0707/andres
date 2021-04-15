n = int(input("ingresa un numero: "))
m =  int(input("ingresa un numero: "))
if n < m:
    for i in range(n,m):
        print(i)
else:
    print("por favor el primer numero debe ser menor al segundo")