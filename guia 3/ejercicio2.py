opcion=str("")
n=int(0)
numsuma=int(0)
suma=int(0)
texto=str("")
letra=str("")
vocales=("a","e","i","o","u")
palvocal=int(0)
par=int(0)
impar=int(0)

print("Bienvenido.")
print("""Introduzca una de las opciones:
a) Generar cantidad a ingresar de números y mostrar la suma de los cuadrados.
b) Ingresar un texto (finalizado por un punto) y determinar la cantidad de palabras que finalizan con vocales.
c) Ingresar una serie de números (la carga finaliza con cero) y determinar si hay mayor cantidad de valores pares o de impares.
d) Salir.""")
opcion=str(input(">Opcion: "))

while opcion.lower()!="d":
    if opcion.lower()=="a":
        n=0
        numsuma=0
        suma=0
        n=int(input("Introduzca la cantidad de numeros a calcular"))
        for x in range(n):
            numsuma=int(input(f"Introduzca el {x+1}º número: "))
            suma=suma+(numsuma**2)
        print(f"La suma de los cuadrados de los numeros ingresados es: {suma}")
    elif opcion.lower()=="b":
        texto=""
        letra=""
        palvocal=0
        texto=str(input("Introduzca el texto (debe estar terminado por un punto): ")).lower()
        while texto.endswith(".")==False: #el ciclo es para evitar que no se introduzca un texto sin un punto al final
            texto=str(input("El texto DEBE terminar con un punto: ")).lower()
        texto=texto[0: len(texto)-1] #elimino el punto para contar tambien la ultima palabra
        for x in texto.split(): #repito un ciclo por la cantidad de palabras que se cuentan con la funcion .split()
            letra=x[len(x)-1] #se cuenta solo la ultima letra de x y luego se comprueba si esta es una de las vocales estipuladas
            if letra in vocales:
                palvocal=palvocal+1
        print(f"{palvocal} palabras terminan en vocal.")
    elif opcion.lower()=="c":
        n=int(input("Introduzca un número (si introduce 0, se terminará la carga de numeros): "))
        while n!=0:
            if n%2==0:
                par=par+1
            else:
                impar=impar+1
            n=int(input("Introduzca otro número, o 0 para finalizar: "))
        if par>impar:
            print("Hay mas cantidad de numeros pares en la secuencia introducida.")
        elif impar>par:
            print("Hay mas cantidad de numeros impares en la secuencia introducida.")
        else:
            print("La cantidad de numeros pares e impares es la misma.")        
    else:
        print("Esa no es una opción válida.")
    
    print("""Introduzca una de las opciones:
a) Generar cantidad a ingresar de números y mostrar la suma de los cuadrados.
b) Ingresar un texto (finalizado por un punto) y determinar la cantidad de palabras que finalizan con vocales.
c) Ingresar una serie de números (la carga finaliza con cero) y determinar si hay mayor cantidad de valores pares o de impares.
d) Salir.""")
    opcion=str(input(">Opción: "))

print("Muchas gracias!")