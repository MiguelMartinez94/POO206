numero = int(input("Ingresa un numero entero: "))

if numero >0:
            
    for n in range(numero, -1,-1):
        
        print(f"{n},")
        
else:
    print("No estás ingresnado un numero enteero")