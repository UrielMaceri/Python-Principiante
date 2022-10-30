#declaro la lista
lista_numeros=list()
lista_numeros=[]
numero=int(0)

print("---------------------------------------------------------------------")
print("La carga de números finalizará con la entrada de un número negativo.")
print("---------------------------------------------------------------------\n")
while numero>=0:  
    numero=int(input("Introduzca un número: "))
    if numero>=0:  #esta condicion es para que el numero negativo introducido no se agregue a la lista
        lista_numeros.append(numero) 

print(f"\nLista obtenida: {lista_numeros}")
