dias = [0,"lunes","martes","miercoles","jueves","viernes","festivo","festivo"]
dia = int(input(" presiona 1 : para iniciar \n presiona 0 : para finalizar\n"))
while dia != 0 :
    try:
        dia = int(input("ingresa un dia de la semana (1 a 7) y (0 para salir)"))
        if dia != 0:
            if dia < 0 or dia > 7 :
                print("por favor ingresa un numero entre 1 y 7")
            elif dia > 0 and dia <=5:
                temp ="."
                print("el dia es {0} {1}".format(dias[dia],temp))
            elif dia == 6 or dia == 7:
                print("es festivo")
        else:
            print("fin")
    except:
            print("ingresa un valor valido")