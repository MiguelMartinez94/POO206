
try:
    numero = int(input("Ingresa un número entero: "))
    
    if numero%2 == 0:
            print(f"El numero {numero} es par")
            
    else:
            print(f"El número {numero} es impar")
            
            
except ValueError:
        print("El número que estás ingresando no es número :c")

