num=int(0)
porc=float(0.0)
numant=int(0)
cuad=int(0)
mayor=int(0)
nummayor=int(0)
contador=int(0)

num=int(input("Introduzca un numero (la carga termina si introduce 0): "))

while num!=0:
    contador=contador+1 #agrego un contador al principio para indicar la posicion del numero
    
    if num%3==0:
        porc=porc+1 #simplemente si el resto del numero dividido por 3 es 0, se suma 1 al contador

    if num==numant**2:
        cuad=cuad+1 #si numero nuevo es igual al cuadrado del numero anterior, se suma 1 al contador

    if contador==1 or (num%2!=0 and num>numant): #se guarda el primer valor y luego solo si el num nuevo es impar y mayor al anterior
        mayor=contador
        nummayor=num

    numant=num #se guarda el num nuevo como num anterior 

    num=int(input("Introduzca un nuevo numero (la carga termina si introduce 0): "))

porc=porc*100/contador #hago la cuenta para mostrar el porcentaje
print(f"Los numeros divisibles por 3 conforman un {porc}%")

#muestro por pantalla el resto de resultados
print(f"{cuad} números fueron igual al cuadrado del número anterior.")

print(f"El mayor numero el impar fue el nº {mayor}, con un valor de {nummayor}.")
    

