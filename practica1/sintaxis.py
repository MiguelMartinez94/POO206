
#1-. Comentarios

#comentarios de una sola linea

"""
Si tu comentario es mayor a dos lieas van dentro de 3 comillas
"""

#2. Strings

print("Hola mundo")
print('Hola soy una linea de comando')

variable1 = "Hola soy una cadena"
print(len(variable1))
print(variable1[2:5])
print(variable1[2:])
print(variable1[:4])

#3. Variables

#5Mike = o #no puedes crear variables con números al inicio


x = "Miguel"
x = 5.5
x =4

print (x)

x = int(3)
y = float(3)
z = str(3)

print(x, y, z)

print(type(x))
print(type(y))
print(type(z))

#4. Solicitud de datos

a = input("Introduce cualquier dato: ")

b = int(input("Introduce un número entero: "))

c = float(input("Introduce un número decimal: "))

d = str(input("Introduce cualquier texto: "))


#5. Boolean, comparacion y logicos

print(10>9)
print(10<9)
print(10==9)
print(10>=9)
print(10<=9)
print(10!=9)

x = 1

print(x<5 and x<10)
print(x<5 or x<10)
print(not(x<5 and x<10))
