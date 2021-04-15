def pidenumero():
    lista=[]
    while True :
        n =int(input("ingresa el valor numerico(0 para terminar)\n"))
        if n == 0:
            break
        else:
            lista.append(n)
    return lista
#:)
def mayorMenor(lista):
    cont = 0
    contt = 0
    for i in lista:
        if i > 100:
            cont = cont + 1
        if i < 100:
            contt = contt + 1
    return cont ,contt
#:)
lista =pidenumero()
cont,contt= mayorMenor(lista)
print(f"{cont} fueron los numeros mayores a 100 y {contt} fueron los numeros menores a 100") 