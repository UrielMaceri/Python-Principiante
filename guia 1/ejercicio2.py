#variable
nombre=str
nombre=str(input("Introduzca su nombre sin espacios: "))
caracteres=int

#contar los caracteres
caracteres = len(nombre)

#condicional par o impar
if int(caracteres)%2 == 0:
    print("Par.")
else:
    print("Impar.")