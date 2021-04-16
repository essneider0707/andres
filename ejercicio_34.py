from math import sqrt 
################################################################
a = int(input("ingresa un numero a:   "))
b = int (input("ingresa un numero b:  "))
c = int (input("ingresa un numero c:  "))
################################################################
determiante =( b**2)-4*a*c
if determiante > 0:
    x_1 = -b+sqrt(b**2-4*a*c)/(2*a)
    x_2 = -b-sqrt(b**2-4*a*c)/(2*a)
    print(x_1, x_2)
elif determiante == 0:
    x_1 = -b / ("2*a")
    print (x_1)
elif determiante < 0:
    print("la solucion de la ecuacion es con numeros complejos")