import random

lista_random=list()
lista_random=[] #inicio la lista

for x in range(10):  #creo un bucle con 10 repeticiones 
    lista_random.append(random.randint(1, 10)) #para añadir cada num aleatorio nuevo a la lista uso .append()

for n in lista_random:  #ingreso cada valor de la lista y lo potencio al cuadrado y al cubo
    print(f"Número: {n}")
    print(f"{n}² = {n**2}")
    print(f"{n}³ = {n**3}")
    print("-----------------")
