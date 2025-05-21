def verificarEdad(edad):
    
    if edad < 18:
        
        raise ValueError("Debes ser mayor de edad para continuar")

    else:
        print(f"Tu edad es válida: {edad}")
        

try:
    
    edad_Usuario = int(input("Introduce tu edad: "))
    
    verificarEdad(edad_Usuario)
    
except ValueError:
    print("Error en la edad")
    
finally:
    
    print("El programa ha finalizado")
