
try:
    for i in range(10, 201, 5):
        print(i)
except ValueError:
    print("Ha ocurrido un error!!")
else:
    print("Se han mostrado los múltiplos de 5 entre el 10 y el 200.")