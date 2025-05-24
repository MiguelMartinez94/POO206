try:

    palabra = str(input("Ingresa cualquier palabra: "))

    if palabra.isalnum():
        raise ValueError("Debes ingresar sólo cadenas de texto, no números")
        pass
    elif palabra != palabra[::-1]:
        print("No es palíndroma")

    else:
        print("Es palindroma")
        
except ValueError:
    print("Debes ingresar sólo cadenas de texto, no números")