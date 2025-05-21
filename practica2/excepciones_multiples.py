try:    
    
    numero = int(input("Introduce un número: "))
    resultado = 10 /numero

    print("Resultado:", resultado)

except (ValueError, ZeroDivisionError) as e:
    print("Error: Se ingresó algo que no es número entero.")
    
else:
    print("Error: Estás intentando dividir entre 0")