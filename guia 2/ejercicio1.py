#declaro variables
competidores=int
nombre=str
tiempo=int
record=int
promedio=int
promedio=0
ganador=str
ganadorT=float
ganadorT=0.0


#pido los datos correspondientes para luego iniciar el ciclo for
print("---Final Ciclismo----")
competidores=0
competidores=int(input("Introduzca el número de competidores: "))

for x in range(competidores): #se repetirá según la cantidad de competidores
    nombre=input(f"Introduzca el nombre del competidor {x+1}: ")
    tiempo=int(input("Introduzca el tiempo del competidor (en minutos aproximados, sin decimales): "))
    promedio=promedio+tiempo

    #guardo la primera entrada como el timepo ganador y si hay alguna entrante que sea mejor, se reemplaza
    if x==0 or tiempo<ganadorT:
        ganador=nombre
        ganadorT=tiempo

#resultados finales
print(f"¡El ganador es {ganador} con un tiempo de {ganadorT} minutos!")

#tiempo record
record=int(input("Introduzca el timepo record de esta carrera (en minutos aproximados, sin decimales):"))
if ganadorT<record:
    print(f"¡Felicidades a {ganador}, rompió el record anterior!")
else:
    print(f"{ganador} ganó la carrera, pero no rompió el record anterior.")

#promedio
promedio=promedio/competidores
print(f"El tiempo promedio entre los {competidores} competidores es de {promedio}.")