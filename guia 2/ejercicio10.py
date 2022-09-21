import random #importo el modulo

#declaro variables
num=int(0)
mayor=int(0)

#creo el ciclo de 10000 numeros aleatorios guardando solo el mayor de todos
for x in range(10000):
    num=random.randint(0, 100000)
    if num>mayor: #el primer numero generado se va a guardar si o si, ya que mayor=0
        mayor=num

print("El mayor numero aleatorio generado fue: ",mayor)
