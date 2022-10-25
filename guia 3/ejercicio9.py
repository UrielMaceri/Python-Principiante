import random

opcion=int(0)
seguir=str("si")

#opción1
numero=int(0)
numeros_totales=int(0)
promedio=int(0)

#opción2
cantidad_random=int(0)
num_rand=int(0)
positivos=int(0)
negativos=int(0)

#opción3
nota_alumno=int(0)

print("""Bienvenido
Elija una de las opciónes:

1. Ingresar números (la carga finaliza cuando se ingresa el -1) y calcular su promedio.
2. Generar una cantidad ingresada de valores aleatorios entre -100 y 100.
Determinar la cantidad de valores negativos y positivos.
3. Cargar la nota de un alumno e informar si está aprobado.
Teniendo en cuenta que la nota es un valor entre 0 y 10, siendo mayor o igual a 4 si está aprobado.""")

while seguir.lower()=="si":
    opcion=int(input("\nOpción > "))
    if opcion==1:
        numeros_totales=0
        promedio=0
        numero=int(input("Introduzca un número (si es negativo, se termina la carga): "))
        while numero>-1:
            numeros_totales=numeros_totales+1
            promedio=promedio+numero
            numero=int(input("Introduzca otro número: "))
        print(f"El promedio entre los {numeros_totales} ingresados es de {promedio/numeros_totales}.")
        seguir=input("Desea volver al menú de opciones? (si/no): ")
    elif opcion==2:
        positivos=0
        negativos=0
        cantidad_random=int(input("Introduzca la cantidad de números aleatorios a calcular: "))
        for x in range(cantidad_random):
            num_rand=random.randint(-100, 100)
            print(f"{x+1}º número: {num_rand}")
            if num_rand>=0:
                positivos=positivos+1
            else:
                negativos=negativos+1
        print(f"La cantidad de números positivos es {positivos} y de negativos es {negativos}.")
        seguir=input("Desea volver al menú de opciones? (si/no): ")
    elif opcion==3:
        nota_alumno=int(input("Introzuca la nota del alumno: "))
        if nota_alumno>=0 and nota_alumno<=10:
            if nota_alumno>=4:
                print("Este alumno está aprobado.")
            else:
                print("Este alumno está desaprobado.")
        else: 
            print("Ese numero no es una nota válida.")
        seguir=input("Desea volver al menú de opciones? (si/no): ")
    else: #es una condición para evitar que se introduzcan datos no deseados
        print("Esa no es una opción válida.")
        seguir=input("Desea volver al menú de opciones? (si/no): ")

print("El programa se terminará. Muchas gracias.")