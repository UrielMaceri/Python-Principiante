n=int(0)
mult=int(0)
promult=int(0)
divisor=int(0)
anteante=int(0)
anterior=int(0)
secuencia=int(0)

n=int(input("Introduzca un número (el programa se cierra con 0): "))

while n!=0:
    if n%6==0:  #solo se guardan los numeros multiplos de 6
        mult=mult+n
        promult=promult+1
    
    if anterior%n==0:  #si el numero nuevo es divisor del anterior, se guarda uno en el contador
        divisor=divisor+1

    if n%2!=0:
        if anteante%2!=0 and anterior>anteante and anterior%2!=0 and n>anterior:  #si el numero ante anterior y el anterior son impares Y ademas la secuencia es ascendente, se suma al contador
            secuencia=secuencia+1

    anteante=anterior    #actualizo las variables conforme el programa avanza
    anterior=n

    n=int(input("Introduzca otro (el programa se cierra con 0): "))

if promult!=0:  #esta condicion es para que el programa no tire error al dividir por 0
    print(f"A) El promedio entre los {promult} números que son {mult/promult}.")
else:
    print("No hubo multiplos de 6.")

print(f"B) {divisor} numeros son divisores exactos del número anterior.")
print(f"C) La cantidad de veces que se generó una secuencia de 3 numeros impares ascendente fue {secuencia}.")