#variable
nombre=str
nombre=str(input("Introduzca su nombre sin espacios: "))
caracteres=int

#contar los caracteres
caracteres = int(len(nombre))

#condicional par o impar
if caracteres%2 == 0:
    print("Las letras de su nombre son pares.")
else:
    print("Las letras de su nombre son impares.")