#variables
pies=float
pulg=float
yar=float
cm=float
mts=float

#pedimos por teclado la medida
pies=float(input("Introduzca la medida en pies a convertir: "))

#hacemos las conversiones
pulg=12*pies
yar=3*pies
cm=2.54*pulg
mts=cm/1000

#imprimimos por pantalla los resultados
print(pies, "pies equivalen a:")
print(pulg," Pulgadas.")
print(yar," Yardas.")
print(cm," Centímetros.")
print(mts," Metros.")