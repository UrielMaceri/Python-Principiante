#delcaro las variables, en este caso, son solo dos listas
lista=list()
lista=[]
lista_inversa=list()
lista_inversa=[]

for x in range(5):    
    lista.append(input(f"Introduzca la {x+1}º palabra: "))  #guardo las palabras de cada bucle directamente en un lugar nuevo de la lista

lista_inversa=lista  #copio la lista original
lista_inversa.reverse()  #la invierto con la funcion .reverse()

print("-----------------------------------")
print(f"Lista original: {lista}")
print(f"Lista invertida: {lista_inversa}")
print("-----------------------------------")
