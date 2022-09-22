#declaro las variables
num=int(0)
total=int(0)
par=int(0)
impar=int(0)
cero=int(0)
alter=int(0)
alterT=int(0)
cont=int(0)

#pido por pantalla la primera entrada, para entrar en el bucle 
num=int(input("Introduzca un numero (si introduce uno negativo, el programa termina): "))
while num>=0: #este bucle solo suma a cada contdor dependiendo de si se cumple o no la condicion
    cont=cont+1
    if (num%2)!=(alter%2) or cont==0: #este condicional compara los restos del numero anterior (alter) con el actual (num) y suma un contador
        alterT=alterT+1
    if num>=50 and num<=100:
        total=total+num
    if (num%2)==0:
        par=par+1
        alter=num
    if (num%2)!=0:
        impar=impar+1
        alter=num
    if num==0:
        cero=cero+1
    num=int(input("Introduzca otro (si introduce uno negativo, el programa termina): "))

print("\n------------------------------------------------------------") #separador
#con condiciones, muestro solo los resultados que sean mayores a 0
if total!=0: 
    print("El total de la suma de todos los valores comprendidos entre 50 y 100 es: ",total)
if par!=0:
    print("El total de números pares ingresados es: ",par)
if impar!=0:
    print("El total de números impares ingresados es: ",impar)
if cero!=0:
    print("Se introdujeron un total de ",cero," ceros.")
#con el contador que esta al principio del ciclo
#comparo las veces totales que se repitió 
#con las veces seguidas que se introdujo un numero par y luego uno impar
if alterT==cont: 
    print("La serie de números introducida solo contiene pares e impares alterados.")