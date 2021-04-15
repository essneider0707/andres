total= 0
cont = 1
while True:
    notas = int(input("ingresa una calificacion: "))
    total = total + notas
    cont = cont + 1
    if cont == 11:
        break
promedio =total / 10
print(promedio)
    