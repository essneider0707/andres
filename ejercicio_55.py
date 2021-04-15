def pidenumero():
    lista=[]
    while True :
        n =float(input("ingresa el valor numerico\n"))
        if n == 0:
            break
        else:
            lista.append(n)
    return lista
#########################################
def parImpar(lista):
    cont = 0
    contt = 0
    for i in lista:
        if i % 2 ==0:
            cont = cont + 1
        elif i % 2 != 0 :
            contt = contt + 1
    return cont ,contt
######################################
def siEs5 (lista):
    n5=0
    for k in lista:
        if k == 5:
            n5 = n5 + 1
    return n5
############################
lista =pidenumero()
cont,contt= parImpar(lista)
n5 = siEs5(lista)
print(f"{cont} fueron pares {contt} fueron impares {n5} fueron n5")

