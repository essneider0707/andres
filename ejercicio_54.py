# funcion que pide cantidad n de numeros y 0 para salir
def pidenumero():
    lista=[]
    while True :
        n =float(input("ingresa el valor numerico(0 para terminar)\n"))
        if n == 0:
            break
        else:
            lista.append(n)
    return lista
#
# funcion que  compara si son pares o impares
def parImpar(lista):
    cont = 0
    contt = 0
    for i in lista:
        if i % 2 ==0:
            cont = cont + 1
        elif i % 2 != 0 :
            contt = contt + 1
    return cont ,contt
#
# funcion que compara si son menores a 0 o mayores a 0
def me0Ma0 (lista):
    me0= 0
    ma0 = 0
    for j in lista:
        if j > 0:
            ma0=ma0+1
        else:
            me0 = me0 + 1
    return me0 , ma0
#
# funcion que compara si son multiplo de 8 
def multiplo8 (lista):
    mult8 = 0
    for k in lista:
        if k % 8 ==0:
            mult8 = mult8 + 1
    return mult8
#
# bloque de asignacion 
lista =pidenumero()
cont,contt= parImpar(lista)
me0,ma0 = me0Ma0(lista)
mult8 = multiplo8(lista)
#
#bloque de mostrar resultados a pantallas
print(f"{cont} son pares y {contt} fueron impares") 
print(f"{ma0} son mayores a 0 y {me0} fueron menores a 0")
print(f"{mult8} son multiplos de 8")
#:)