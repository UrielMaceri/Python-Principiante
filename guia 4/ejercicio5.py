import random

#declaro la lista
lista_random=list()
lista_random=[]

for x in range(10): #en el bucle se agregan 10 numeros aleatorios a la lista
    lista_random.append(random.randint(1, 999)) 

print(f"\nLista original: {lista_random}")
#ordeno la lista y la imprimo ya ordenada de menor a mayor
lista_random.sort()
print(f"Lista ordenada: {lista_random}")