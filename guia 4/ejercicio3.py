#declaro las variables y la lista
notas=list()
notas=[]
nota_valor=int(0)
nota_maxima=int(0)
nota_minima=int(0)
promedio=float(0.0)
total=int(5)

#creo un bucle por el total de notas
for x in range(total):  
    nota_valor=int(input(f"Introduzca la {x+1}ª nota obtenida: "))
    while nota_valor<0 or nota_valor>10:  #bucle condicional para evitar que se introduzcan valores no deseados
        print("Esa no es una nota válida.")
        nota_valor=int(input("Por favor introduzca un número válido: "))
    if x==0 or nota_valor>nota_maxima:  #utilizo un maximo para la nota mas alta
        nota_maxima=nota_valor
    if x==0 or nota_valor<nota_minima:  #y un minimo para la nota mas baja
        nota_minima=nota_valor
    promedio=promedio+nota_valor  #sumo los valores para el promedio
    notas.append(nota_valor)  #agrego las notas una a una en la lista

print(f"\nLas notas de este alumno son: {notas}")
print(f"La nota mas alta es de {nota_maxima}")
print(f"La nota mas baja es de {nota_minima}")
print(f"El promedio de las notas es de {promedio/total}")