usuarios = {  
    "iperurena": {  
        "nombre": "Iñaki",  
        "apellido": "Perurena",  
        "password": "123123"  
    },  
    "fmuguruza": {  
        "nombre": "Fermín",  
        "apellido": "Muguruza",  
        "password": "654321"  
    },  
    "aolaizola": {  
        "nombre": "Aimar",  
        "apellido": "Olaizola",  
        "password": "123456"  
    }  
}

intentos = 3  

while intentos > 0:
    usuario = input("Introduce tu usuario: ")
    contraseña = input("Introduce tu contraseña: ")

    if usuario in usuarios and usuarios[usuario]["password"] == contraseña:
        print(f"¡Bienvenido {usuarios[usuario]['nombre']} {usuarios[usuario]['apellido']}!")
        break
    else:
        intentos -= 1
        if intentos > 0:
            print(f"Datos incorrectos. Te quedan {intentos} intentos.")
        else:
            print("Has agotado todos tus intentos.")
