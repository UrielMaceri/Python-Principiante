#declaro variables
sueldo=int(0)
mejor=int(0)
peor=int(0)
mes=int(0)
promedio=int(0)
aguinaldo=float(0)

print("Aguinaldo del primer semestre")
for x in range(6): #el ciclo es solo por un semestre, se repite solo 6 veces
    sueldo=int(input(f"Introduzca el sueldo del mes {x+1}: "))
    promedio=promedio+sueldo

    if x==0 or sueldo>mejor: #este if es para calcular el aguinaldo y guardarlo en su variable
        mejor=sueldo
        aguinaldo=mejor/2
    
    if x==0 or sueldo<peor: #este es para guardar, en sus respsctivas variables, el peor sueldo y el mes en el que se consiguó
        peor=sueldo
        mes=x+1

print(f"El mejor sueldo del semestre fue de ${mejor}, por lo que corresponde un aguinaldo de ${aguinaldo}.")
print(f"El peor sueldo del semestre fue ${peor}, obtenido el mes nº {mes}.")
print(f"El promedio de su sueldo durante todo el semestre es de ${promedio/6}.")
