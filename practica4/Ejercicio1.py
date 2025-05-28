while True:
    numero = int(input("Ingresa un número entero positivo mayor de 10: "))
    try:
        if numero > 10:
            for n in range(numero + 1):
                if n>2:
                    if n%2 != 0:
                            
                        print(f"{n},")
                    
        else:
                print("\n======No ingresaste un número mayor de 10======")
    except (TypeError, ValueError):
        print("Error: No ingresaste un número")