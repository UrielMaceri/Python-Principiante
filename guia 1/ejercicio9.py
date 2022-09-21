#declaor variables
num=int(0)
res=int(0)

num=int(input("Introduzca un número entero: "))
for x in range(10):
    res=num*(x+1)
    print(f"{num}*{x+1} = {res}")