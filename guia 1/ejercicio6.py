#declaracion de variables
base=int
altura=int
area=float

#se pide por teclado el valor de la base
base=int(input("Introduzca el valor de la base del triangulo: "))

#se calcula la altura y el area
altura=base**2
area=(base*altura)/2

#se muestra en pantalla el resultado
print("El area de tu triangulo es igual a ", area)
