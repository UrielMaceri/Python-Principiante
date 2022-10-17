n=int(0)
cinco=int(0)
primer=int(0)
primer_total=int(0)
mayor=int(0)
anterior=int(0)
anterior_total=int(0)
seguir=str("si")
cont=int(0)

while seguir.lower()=="si" or seguir.lower()=="s":
    n=int(input("Introduzca un número: "))
    while n<=0:
        n=int(input("El número debe ser mayor a 0: ")) 

    if n%10==5:
        cinco=cinco+1 #Contador que solo suma si el ultimo numero es 5

    if n==primer:
        primer_total=primer_total+1 #contador que solo suma si el numero ingresado es igual al primero
    if cont==0:  
        primer=n #guardo la información de la primera iteración luego del contador, para que no sume 1 por el primer "n" (al ser este igual a "primer")

    if anterior!=0 and n>anterior:
        anterior_total=anterior_total+1 #contador que solo suma si el numero nuevo es mayor al anterior
    anterior=n #mse guarda siempre sin condiciones

    cont=cont+1
    seguir=str(input("Desea seguir introduciendo números? (si/no): "))
    while seguir.lower()!="no" and seguir.lower()!="si":
        seguir=str(input("Esa no es una opción válida. Solo SI o NO: "))

print("\nR E S P U E S T A S")
print(f"A) La cantidad total de numeros terminados en 5 es {cinco}.")
print(f"B) La cantidad total de veces extra que aparece el primer número ({primer}) es {primer_total}.")
print(f"C) La cantidad total de números que fueron mayores a su anterior es {anterior_total}.")