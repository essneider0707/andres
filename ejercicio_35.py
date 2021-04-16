print("el usuario es goku y la contraseña es 12345 ")
print("inicia sesion por favor ")
while True:
    user = str (input("ingresa el usuario: "))
    password = int(input("ingresa la contraseña: "))
    if user == "goku" and password == 12345:
        print(f"has iniciado sesion exitosamente {user}")
        break
    else:
        print("datos incorrectos")