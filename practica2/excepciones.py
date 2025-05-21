try:    
    
    numero = int(input("Introduce un número: "))
    resultado = 10 /numero

    print("Resultado:", resultado)

except ValueError:
    print("Error: Se ngresó algo que no es número entero.")
    
except ZeroDivisionError:
    print("Error: Estás intentando dividir entre 0")