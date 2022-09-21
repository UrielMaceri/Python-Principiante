import random #importo el modulo

#declaro variables
num=int(0)
menor=int(0)
prom=int(0)
total=int(0)
res=float(0.0)

#el ciclo se repetirá tantas veces como el enunciado marca
for x in range(5000):
    num=random.randint(0, 100000)
    if x==0 or num<menor: #se guarda el primer ciclo y luego solo si se cumple la conducion
        menor=num
    if num<10000: #sumo todos los valores menores a 10000 para realizar un promedio de los mismos
        prom=prom+num
        total=total+1 #el contador es para usarlo de divisor 

#muestro el menor numero obtenido
print("El menor numero aleatorio generado fue: ",menor)

#calculo y muestro el promedio de todos los numeros menores a 10000, solo si hay alguno
if prom!=0:
    res=prom/total
    print("El promedio entre los numeros aleatorios menores de 10.000 es de ",round(res, 2))
    