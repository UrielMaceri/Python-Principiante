#declaración de variables
ingreso=float
ahorro=float
numes=int
mes=str

numes=1
ingreso=0.0
ahorro=0.0
#ciclo repetitivo de los 12 meses
for x in range (12):
    if numes==1:
        mes="Enero"
    elif numes==2:
        mes="Febrero"
    elif numes==3:
        mes="Marzo"
    elif numes==4:
        mes="Abril"
    elif numes==5:
        mes="Mayo"
    elif numes==6:
        mes="Junio"
    elif numes==7:
        mes="Julio"
    elif numes==8:
        mes="Agosto"
    elif numes==9:
        mes="Septiembre"
    elif numes==10:
        mes="Octubre"
    elif numes==11:
        mes="Noviembre"
    elif numes==12:
        mes="Diciembre"
    print("Mes de ", mes)
    ingreso=float(input("Introduzca el ingreso correspondiente al mes (si no hay ingresos, introduzca 0): "))
    ahorro=ahorro + ingreso*0.10 #se suma el ahorro anterior (que la primera vez será 0) mas el nuevo de cada mes

    numes=numes+1 #se suma uno al mes anterior para que el condicional muestre el mes que corresponde

#se muestra por pantalla el total ahorrado
print("El ahorro total de este año es de: $", ahorro)
