#declaración de variables
from pickletools import float8


turno=int
horas=int
pago=float
dia=float
noche=float

#constantes de los pagos por hora
noche=40.60
dia=35.50


#se pide al usuario que introduzca un valor para luego entrar en el condicional
turno=int(input("""Introduzca el numero correspondiente al turno en el que trabajó: 
(1) Turno NOCHE
(2) Turno MAÑANA
- """))

#se crea la condicion y dentro se multiplican las horas segun el turno elegido
if turno==1:
    horas=0
    pago=0
    horas=int(input("Introduzca la cantidad de horas trabajadas (numeros enteros, sin decimales): "))
    pago=horas*noche
    print("A usted le corresponden aproximadamente $",pago)
elif turno==2:
    horas=0
    pago=0
    horas=int(input("Introduzca la cantidad de horas trabajadas (numeros enteros, sin decimales): "))
    pago=horas*dia
    print("A usted le corresponden aproximadamente $",pago)
else:
    print("Ese número no corresponde a ninguna opción, por favor reinicie el programa.")