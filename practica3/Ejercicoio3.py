try:

    palabra = str(input("Ingresa cualquier palabra: "))

    if any(p.isdigit() for p in palabra):
        raise ValueError("Debes ingresar sólo cadenas de texto")
        
    elif palabra != palabra[::-1]:
        print("No es palíndroma")
        
        print(f"{palabra} no es igual a {palabra[::-1]}")

    else:
        print("Es palindroma")
        
        print(f"WOW, la palabra que ingresaste: {palabra} se escibe igual al derecho y al revés, mira {palabra} vs {palabra[::-1]}")
        
except ValueError:
    print("Debes ingresar sólo cadenas de texto, no números")