#importo el modulo random para nuimeros aleatorios
import random

#declaro variables
n=int(0)
decimal=int(0)
hexa=int(0)

#pido por teclado la cantidad de valores a convertir
n=int(input("Introduzca LA CANTIDAD de números que desea convertir a hexadecimal: "))

#dentro del for se crean los numeros aleatorios, se convierten a hexadecimal con la funcion "hex()" y se muestran ambos valores en todas las repeticiones
for x in range(n):
    decimal=random.randint(5000, 450000)
    hexa=hex(decimal)
    print(f"DECIMAL={decimal} - HEXADECIMAL={hexa}")
