n = int(input("ingresa un numero: "))
m =  int(input("ingresa un numero: "))
total = 0
if n < m:
    for i in range(n,m):
        total = total + i
        print(total)
else:
    print("por favor el primer numero debe ser menor al segundo")