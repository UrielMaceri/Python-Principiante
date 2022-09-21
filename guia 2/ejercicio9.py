import random #importo el modulo random para los numeros aleatorios

num=int(0)
prom=int(0)
res=int(0)

for x in range(1000):
    num=random.randint(0, 100000)
    prom=prom+num


res=prom/(x+1)
print("El promedio de los 1000 numeros aleatorios es: ", round(res, 2))
