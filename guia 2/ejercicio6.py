#declaración de variables
ingreso=int(0)
promedio=float(0.0)
contador=int(0)

#pido por teclado el primer numero, si es 0, envía directamente al promedio que será 0
ingreso=int(input(""""Ingrese un número (el programa concluirá si introduce "0"): """))
if ingreso!=0:
    promedio=promedio+ingreso
    contador=contador+1
    ingreso=int(input(""""Ingrese otro número (el programa concluirá si introduce "0"): """))
    while ingreso!=0:
        promedio=promedio+ingreso
        contador=contador+1
        ingreso=int(input(""""Ingrese otro número (el programa concluirá si introduce "0"): """))
    print(f"El promedio de los {contador} números ingresados es de {promedio/contador}")
else:
    print("No se ingresó ningun número, por lo tanto el promedio es 0.")
