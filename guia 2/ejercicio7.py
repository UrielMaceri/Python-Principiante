#declaracion de variables
cant=int(0)
total=int(0)
descuento=str
con=int(0)
sin=int(0)
funciones=int(0)
porc=float(0.0)

#se pide por teclado la primera introducción de valores para entrar o no al ciclo
cant=int(input("Introduzca la cantidad de espectadores de la función (si quiere cancelar, introduzca 0): "))

#en el bucle se suman los valores correspondientes al si hubo descuento o no, hasta que se introduzca 0
while cant!=0:
    descuento=str(input("¿Hubo descuento de entradas en la misma? (S/N): "))
    if descuento.lower()=="si" or descuento.lower()=="s":
        total=total+cant*50
        con=con+1
    else:
        total=total+cant*75
        sin=sin+1
    cant=int(input("Introduzca la cantidad de espectadores de otra función (si la anterior fue la última, introduzca 0): "))

#calculo las funciones totales
funciones=con+sin

#creo un if para que no se realicen los calculos si las funciones son iguales a 0
if funciones!=0:
    print(f"El total recaudado de las {funciones} funciones fue de ${total}.")
    #calculo el porcentaje según los datos obtenidos
    porc=(con*100)/funciones
    #y muuestro por pantalla los datos
    print(f"[{con}] Funciones fueron efectuadas con descuento. ")
    print(f"Estas componen un {round(porc, 2)}% de las funciones totales.") #usando la funcion round() muestro solo 2 numeros decimales
else:
    print("No se realizaron funciones, por lo que la recaudación es de $0.")