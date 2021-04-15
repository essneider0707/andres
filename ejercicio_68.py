while True:
    try:
        n1= int(input("ingresa un numero: "))
        n2= int(input("ingresa un numero: "))
        if n2 != 0:
            print(n1/n2)
            break
    except ZeroDivisionError:
        print("“Madre mía, Willy, no puedes dividir por cero”")
    except:
        print("“Madre mía, Willy , ingresa un numero joder!!!!")