# leemos el numero del cual queremos saber sus factores
n = int(input("ingresa un numero: ")) 
#definimos un for que tenga el rango del numero 
for i in range(1,n+1):
#condicional que nos permite conocer si su resto es = 0 es factor del numero 
    if n % i == 0:
        print(i)