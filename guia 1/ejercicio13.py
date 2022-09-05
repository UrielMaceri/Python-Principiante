#declaracion de variables
actual=float
peso=float
dolar=float

actual=float(input("Introduzca el valor actual del peso: "))

#Convertidor peso a dolar
peso=0
peso=float(input("Introduzca el monto en pesos a convertir: "))
dolar=0
dolar=peso/actual
print("Son aproximadamente: USD $",dolar)

#convertidor dolar a peso
dolar=0
dolar=float(input("Introduzca el monto en dolares a convertir: "))
peso=0
peso=dolar*actual
print("Son aproximadamente: $",peso)