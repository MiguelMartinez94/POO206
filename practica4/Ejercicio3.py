
while True:
    try:
        
        frase = str(input("Ingresa cualquier frase: "))
        letra = str(input("Ingresa la letra que quieras buscar: "))

        if any(f.isdigit() for f in frase):

            print("No debes de ingresar números.")
            
        contador = 0

        for c in frase:
            if c == letra:
                contador +=1


        print(f"El la cantidad de veces que aparece {letra} en {frase} es: {contador}")
        
    except (ValueError, TypeError):
        
        print("Hemos encontrado un error en tu frase, vuelve a intentarlo :c")