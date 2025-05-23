def validar_numero():

    try:
        numero = int(input("Ingresa un número entero: "))
        numero/2
        if numero is not int:
            print(f"El numero {numero} es impar")
            
        else:
            print(f"El número {numero} es par")
            
            
    except ValueError:
        print("El número que estás ingresando no es número :c")
        
