
try:
    contrasena = input("Ingresa una contraseña: ")
        
    if len(contrasena) < 10:
        print("Tu contraseña debe ser de al menos 10 caracteres")
        pass
    elif not any(c.isdigit() for c in contrasena):
        print("Tu contraseña debe tener un número.")
        
    elif not any(c in "@!#$%&?¿+." for c in contrasena):
        print("Tu contraseña debe tener un carácter especial")
            
    else: 
        print("Tu contraseña es válida!")
        
except Exception:
    print("Error!")