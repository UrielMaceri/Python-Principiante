#declaro las variables y las pido por teclado
a=int
b=int

a=int(input("Introduzca el primer número entero: "))
b=int(input("Introduzca el segundo número entero: "))

#creo un if así da igual qué numero se pone primero
if a<b:
    print(f"Secuencia de impares ascendente entre {a} y {b}")
    for x in range(a, b+1): #ordeno el rango y a b le sumo 1 por si este es un numero impar
        if (x%2!=0):
            print(x, end="  ")
    x=0
    print(f"\nSecuencia impares descendente entre {a} y {b}")
    for x in range(b, a-1, -1): #ordeno el rango al revés y con paso -1 para que se imprima de manera decreciente
        if (x%2!=0):
            print(x, end="  ")
else: #esta parte es igual que la anterior, solo que invierto "a" y "b", por si "a" es el numero mayor
    print(f"Secuencia de impares ascendente entre {b} y {a}")
    for x in range(b, a+1):
        if (x%2!=0):
            print(x, end="  ")
    x=0
    print(f"\nSecuencia impares descendente entre {b} y {a}")
    for x in range(a, b-1, -1):
        if (x%2!=0):
            print(x, end="  ")