def division():
    
    try:
        
        numero = int(input("Ingresas un númerp: "))
        resultado = 10 / numero
        
        print("REsultado:", resultado)
        
    except ZeroDivisionError:
        
        print("Error: División entre cero")
        
    except ValueError:
        
        print("Error: Debes ingresar un número entero.")
        
        
    finally:
        print("Se acabaron los intentos")
        
division()   