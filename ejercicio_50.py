n = int(input("ingresa la cantidad de notas que deseas ingresar : "))
total= 0
cont = 1
while True:
    notas = int(input("ingresa una calificacion: "))
    total = total + notas
    cont = cont + 1
    if cont == n +1:
        break
promedio =total / (cont - 1)
print(promedio , " es su promedio" )
