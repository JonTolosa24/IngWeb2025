intentos = 3

while intentos > 0:
    usuario = input("Introduce el nombre de usuario: ")
    contraseña = input("Introduce la contraseña: ")

    if usuario == "root" and contraseña == "toor":
        print("¡Bienvenido!")
        break
    else:
        intentos -= 1
        if intentos > 0:
            print(f"Datos incorrectos. Le quedan {intentos} intentos.")
        else:
            print("Has agotado todos tus intentos.")
