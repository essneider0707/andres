cadena = str(input("ingresa una palabra: "))
for i in range(len(cadena)-1,-1,-1):
    print(cadena[i],end ="")
print()
# solucion 2
print(cadena[::-1])