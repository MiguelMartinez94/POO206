
    
try:
        
        año = int(input("Ingresa el año que más te guste: "))
        
        
        if año%4 == 0:
                print(f"El año {año} es bisiesto")
                
        else:
            print(f"El año que ingresaste: {año} no es bisiesto")
            
except ValueError:
        print("No ingresaste un año.")
        