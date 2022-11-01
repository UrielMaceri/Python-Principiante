#declaro valiables
lista1=list()
lista2=list()
lista3=list()
n=int(0)

lista1=[]
lista2=[]
lista3=[]

#pido que se introduzcan 5 enteros por lista
for x in range(5):
    n=int(input("Introduzca el {x}º numero de la lista 1: "))
    lista1.append(n)

for i in range(5):
    n=int(input("Introduzca el {x}º numero de la lista 2: "))
    lista2.append(n)

#anido ambas listas para que queden en una sola de 10 valores
lista3=lista1+lista2

print(f"\nPrimer lista: {lista1}")
print(f"Segunda lista: {lista2}")
print(f"Lista anidada: {lista3}")