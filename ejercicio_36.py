numeros = ["no joda es cero","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve","diez"]
n = int(input ("ingresa un numero del 1 al 10 y se imprimira como se escribe : "))
if n > 0 and n <= 10:
    print(numeros[n])
else:
    print("ingresa un numero entre 1 y 10")